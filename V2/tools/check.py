"""Validate V2 and record integrity findings inside V2 only."""
from pathlib import Path
import hashlib,json,re,subprocess,sys,struct,xml.etree.ElementTree as ET
from urllib.parse import unquote
ROOT=Path(__file__).resolve().parents[1]
config=json.loads((ROOT/'structure.json').read_text())
errors=[]
images=set()
for p in ROOT.rglob('*.md'):
    text=p.read_text()
    if '\ufffd' in text:errors.append(f'{p.relative_to(ROOT)}: invalid Unicode')
    if len(re.findall(r'^\$\$\s*$',text,re.M))%2:errors.append(f'{p.relative_to(ROOT)}: unbalanced display math')
    for target in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)',text):
        if re.match(r'^(https?://|mailto:)',target):continue
        file,_,anchor=unquote(target).partition('#')
        dest=(p.parent/file).resolve() if file else p
        if not dest.exists():errors.append(f'{p.relative_to(ROOT)}: missing {target}')
        elif anchor and dest.suffix=='.md' and f'id="{anchor}"' not in dest.read_text():errors.append(f'{p.relative_to(ROOT)}: missing anchor {target}')
        if dest.suffix in ['.png','.svg'] and dest.exists():images.add(dest)
    if text.count('```')%2:errors.append(f'{p.relative_to(ROOT)}: unbalanced code fence')
for p in images:
    if p.suffix=='.png':
        raw=p.read_bytes()
        if raw[:8]!=b'\x89PNG\r\n\x1a\n' or len(raw)<24:errors.append(f'{p.name}: invalid PNG')
        elif min(struct.unpack('>II',raw[16:24]))<1:errors.append(f'{p.name}: empty image')
    else:
        try:ET.parse(p)
        except ET.ParseError:errors.append(f'{p.name}: invalid SVG')
numbers=[c['number'] for c in config['chapters']]
if numbers!=list(range(1,61)):errors.append('Chapter coverage must be 01 through 60')
# Original files must have identical blobs to the baseline.
base='66ab669a777830a276b57d9643222739912b3619'
changed=subprocess.check_output(['git','diff',base,'--name-only'],cwd=ROOT.parent).decode().splitlines()
if any(not p.startswith('V2/') for p in changed):errors.append('Original files changed')
if '--final' in sys.argv:
    stats=json.loads((ROOT/'edition.json').read_text())
    if stats['body_cjk']<200000:errors.append(f"Body below minimum: {stats['body_cjk']}")
    if any(c['status']!='complete' for c in config['chapters']):errors.append('Incomplete chapter status')
    for c in config['chapters']:
        text=(ROOT/c['path']).read_text()
        if any(w in text for w in ['TODO','待补充','此处略去','占位符']):errors.append(f"{c['path']}: unfinished marker")
    def clean(text):
        text=re.sub(r'<!-- v2:(?:nav|toc|footer):start -->.*?<!-- v2:(?:nav|toc|footer):end -->\n?','',text,flags=re.S)
        text=re.sub(r'<a id="section-\d+"></a>\n','',text)
        return re.sub(r'\n{3,}','\n\n',text).strip()+'\n'
    texts=[clean((ROOT/c['path']).read_text()) for c in config['chapters']]
    intros=[clean((ROOT/'volumes'/v['slug']/'README.md').read_text()) for v in config['volumes']]
    actual=sum(len(re.findall(r'[\u3400-\u4dbf\u4e00-\u9fff]',re.sub(r'<!--.*?-->','',re.sub(r'^#{1,6} .*$','',t,flags=re.M),flags=re.S))) for t in texts+intros)
    if stats['body_cjk']!=actual:errors.append(f'Outdated size report: {stats["body_cjk"]} != {actual}')
    source_hash=hashlib.sha256(''.join(texts).encode()).hexdigest()
    numerical=json.loads((ROOT/'sources/numerical-audit.json').read_text())
    if numerical['source_sha256']!=source_hash:errors.append('Numerical audit is stale')
    if numerical['passed']!=numerical['total']:errors.append('Numerical verification failed')
    if stats['source_sha256']!=source_hash:errors.append('Build source hash is stale')
    index=json.loads((ROOT/'sources/chapter-sources.json').read_text())
    if [x['chapter'] for x in index]!=list(range(1,61)):errors.append('Source index coverage incomplete')
report={'errors':errors,'markdown_files':len(list(ROOT.rglob('*.md'))),'referenced_images':len(images),'original_unchanged':not any(not p.startswith('V2/') for p in changed)}
(ROOT/'sources/integrity-audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False,indent=2))
raise SystemExit(bool(errors))
