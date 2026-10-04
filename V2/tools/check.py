"""Read-only validation of V2 links, formulas, coverage and original protection."""
from pathlib import Path
import json,re,subprocess,sys
from urllib.parse import unquote
ROOT=Path(__file__).resolve().parents[1]
config=json.loads((ROOT/'structure.json').read_text())
errors=[]
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
report={'errors':errors,'markdown_files':len(list(ROOT.rglob('*.md'))),'original_unchanged':not any(not p.startswith('V2/') for p in changed)}
print(json.dumps(report,ensure_ascii=False,indent=2))
raise SystemExit(bool(errors))
