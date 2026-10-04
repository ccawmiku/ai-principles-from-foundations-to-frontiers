"""Build the V2 edition without writing outside V2."""
from pathlib import Path
import hashlib,json,re
ROOT=Path(__file__).resolve().parents[1]
CONFIG=json.loads((ROOT/'structure.json').read_text())
MARKERS=r'<!-- v2:(?:nav|toc|footer):start -->.*?<!-- v2:(?:nav|toc|footer):end -->\n?'
def clean(text):
    text=re.sub(MARKERS,'',text,flags=re.S)
    text=re.sub(r'<a id="section-\d+"></a>\n','',text)
    return re.sub(r'\n{3,}','\n\n',text).strip()+'\n'
def cjk_body(text):
    # Titles, generated navigation and all maintenance documents are excluded.
    text=clean(text)
    text=re.sub(r'^#{1,6} .*$', '',text,flags=re.M)
    text=re.sub(r'<!--.*?-->', '',text,flags=re.S)
    return len(re.findall(r'[\u3400-\u4dbf\u4e00-\u9fff]',text))
def link(path):return str(path).replace('\\','/')
chapters=CONFIG['chapters']
texts={c['path']:clean((ROOT/c['path']).read_text()) for c in chapters}
volumes=CONFIG['volumes']
report={'chapters':len(chapters),'complete_chapters':sum(c['status']=='complete' for c in chapters),'minimum_body_cjk':200000,'body_cjk':0,'volumes':[],'source_sha256':hashlib.sha256(''.join(texts.values()).encode()).hexdigest()}
for volume in volumes:
    members=[c for c in chapters if c['volume']==volume['slug']]
    intro=ROOT/'volumes'/volume['slug']/'README.md'
    intro_text=clean(intro.read_text()) if intro.exists() else ''
    size=sum(cjk_body(texts[c['path']]) for c in members)+cjk_body(intro_text)
    report['volumes'].append({'slug':volume['slug'],'chapters':len(members),'body_cjk':size})
    report['body_cjk']+=size
    for c in members:
        p=ROOT/c['path'];i=chapters.index(c)
        previous=chapters[i-1] if i else None;following=chapters[i+1] if i+1<len(chapters) else None
        import os
        relative=lambda other:link(Path(os.path.relpath(ROOT/other,p.parent)))
        nav=[f"[← {previous['number']:02d} {previous['title']}]({relative(previous['path'])})" if previous else '开篇',f'[全书目录]({relative("README.md")})',f"[{following['number']:02d} {following['title']} →]({relative(following['path'])})" if following else '正文结束']
        body=texts[c['path']]
        title,rest=body.split('\n',1)
        toc=[];lines=[];n=0
        for line in rest.splitlines():
            if line.startswith('## '):
                n+=1;anchor=f'section-{n:02d}'
                toc.append(f'- [{line[3:]}](#{anchor})')
                lines.append(f'<a id="{anchor}"></a>')
            lines.append(line)
        navigation='　｜　'.join(nav)
        rendered=title+'\n\n<!-- v2:nav:start -->\n'+navigation+'\n<!-- v2:nav:end -->\n\n<!-- v2:toc:start -->\n<details>\n<summary>本章目录</summary>\n\n'+'\n'.join(toc)+'\n\n</details>\n<!-- v2:toc:end -->\n'+'\n'.join(lines).strip()+'\n\n<!-- v2:footer:start -->\n---\n\n'+navigation+f'\n\n[方法与案例来源]({relative("sources/README.md")})\n<!-- v2:footer:end -->\n'
        p.write_text(rendered)
# 合并版只转相对链接，不重复计入正文统计。
book=['# AI 原理：从早期方法到现代智能系统 · V2\n','[返回分卷目录](README.md)\n']
import os
for volume in volumes:
    book.append(f"\n# {volume['title']}\n")
    ipath=ROOT/'volumes'/volume['slug']/'README.md'
    if ipath.exists():
        intro=clean(ipath.read_text())
        def intro_link(match):
            target=match.group(1)
            if re.match(r'^(https?://|mailto:|#)',target):return match.group(0)
            rel=ipath.relative_to(ROOT).parent/target
            return ']('+link(Path(os.path.normpath(str(rel))))+')'
        book.append(re.sub(r'\]\(([^)]+)\)',intro_link,intro))
    for c in [c for c in chapters if c['volume']==volume['slug']]:
        text=texts[c['path']]
        def replace(match):
            target=match.group(1)
            if re.match(r'^(https?://|mailto:|#)',target):return match.group(0)
            return ']('+link(Path(os.path.normpath(str(Path(c['path']).parent/target))))+')'
        text=re.sub(r'\]\(([^)]+)\)',replace,text)
        book.append(f"\n<a id=\"chapter-{c['number']:02d}\"></a>\n"+text+'\n---\n')
(ROOT/'BOOK.md').write_text('\n'.join(book))
(ROOT/'edition.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False,indent=2))
