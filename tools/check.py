"""Check links, formula delimiters, figures and the textbook's numerical examples."""
from pathlib import Path
from urllib.parse import unquote
import re
import math
import json
import xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]
errors=[]
files=[ROOT/"README.md",ROOT/"BOOK.md",ROOT/"SOURCES.md",*sorted((ROOT/"chapters").glob("*.md"))]
for path in files:
    txt=path.read_text(encoding="utf-8")
    if "\ufffd" in txt:
        errors.append(f"{path.name}: invalid replacement character")
    if len(re.findall(r"^\$\$\s*$",txt,re.M))%2:
        errors.append(f"{path.name}: unmatched display math")
    in_math=False
    for line_no,line in enumerate(txt.splitlines(),1):
        if line.strip()=="$$":
            in_math=not in_math
        elif not in_math and len(re.findall(r"(?<!\\)\$",line))%2:
            errors.append(f"{path.name}:{line_no}: unmatched inline math")
    ids=re.findall(r'<a id="([^"]+)"',txt)
    if len(ids)!=len(set(ids)):
        errors.append(f"{path.name}: duplicate explicit anchors")
    for target in re.findall(r"!?\[[^\]]*\]\(([^)]+)\)",txt):
        if re.match(r"^(https?://|mailto:)",target):
            continue
        target=unquote(target)
        filepart,_,anchor=target.partition("#")
        resolved=(path.parent/filepart).resolve() if filepart else path
        if not resolved.exists():
            errors.append(f"{path.name}: broken link {target}")
        elif anchor and resolved.suffix==".md":
            dst=resolved.read_text(encoding="utf-8")
            if f'id="{anchor}"' not in dst:
                errors.append(f"{path.name}: missing explicit anchor {target}")
    for left in ["TODO","待补充","待完善","此处略去","占位符"]:
        if left in txt:
            errors.append(f"{path.name}: unfinished marker {left}")

for p in (ROOT/"assets").glob("*.svg"):
    ET.parse(p)
    if not p.with_suffix(".png").exists():
        errors.append(f"missing PNG for {p.name}")

def softmax(xs):
    m=max(xs)
    es=[math.exp(x-m) for x in xs]
    return [v/sum(es) for v in es]
a=softmax([1/math.sqrt(2),1/math.sqrt(2),2/math.sqrt(2)])
out=[a[0]+a[2],2*a[1]+a[2]]
assert abs(out[0]-.7517)<1e-4 and abs(out[1]-1)<1e-12
assert 2*1*32*8192*8*128*2==2**30
assert abs(.5*(1.8*2-6)**2-2.88)<1e-12
assert abs(-math.log(1/(1+math.exp(-math.log(4))))-.22314355)<1e-7
assert abs(5+.1*(1+.9*6-5)-5.14)<1e-12
assert abs(sum(softmax([2,1,0,-1]))-1)<1e-12
I=[[0,0,1],[0,1,1],[1,1,1]]
K=[[1,-1],[1,-1]]
conv=[[sum(I[y+i][x+j]*K[i][j] for i in range(2) for j in range(2)) for x in range(2)] for y in range(2)]
assert conv==[[-1,-1],[-1,0]]
report={"markdown_files_checked":len(files),"diagrams_checked":len(list((ROOT/"assets").glob("*.svg"))),
        "numerical_examples":"passed","errors":errors}
outdir=ROOT/".build"
outdir.mkdir(exist_ok=True)
(outdir/"validation.json").write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding="utf-8")
print(json.dumps(report,ensure_ascii=False,indent=2))
raise SystemExit(bool(errors))
