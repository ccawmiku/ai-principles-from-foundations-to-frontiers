"""Build navigation, source notes and the single-file edition without dependencies."""
from pathlib import Path
import json
import re
import hashlib

ROOT=Path(__file__).resolve().parents[1]
CH=ROOT/"chapters"
DATE="2026-10-03"
TITLE="AI 原理：从早期方法到现代智能系统"
MARKER_RE=r"<!-- generated:(?:nav|toc|footer):start -->.*?<!-- generated:(?:nav|toc|footer):end -->\n?"

def clean(s):
    s=re.sub(MARKER_RE,"",s,flags=re.S)
    s=re.sub(r'<a id="s\d+"></a>\n',"",s)
    s=re.sub(r"\n{3,}","\n\n",s)
    return s.strip()+"\n"

files=sorted(CH.glob("*.md"))
texts={p.name:clean(p.read_text(encoding="utf-8")) for p in files}
titles={n:t.splitlines()[0].removeprefix("# ") for n,t in texts.items()}
keys={n:("chapter-"+n[:2] if n[:2].isdigit() else n.removesuffix(".md")) for n in texts}
groups=json.loads((ROOT/"structure.json").read_text(encoding="utf-8"))
refs=json.loads((ROOT/"references.json").read_text(encoding="utf-8"))
main=[n for n in texts if n[:2].isdigit()]
cjk=sum(len(re.findall(r"[\u4e00-\u9fff]",texts[n])) for n in main)
chars=sum(len(texts[n]) for n in main)
diagrams=len(list((ROOT/"assets").glob("*.svg")))

sources=[
"# 方法与事实核查说明\n",
f"核查日期：{DATE}。以下用于追溯正文的方法定义和公开案例，不是推荐阅读清单。\n",
"基础数学与教学数值例子由本书独立展开。代表论文用于核对方法的结构、目标与公开边界；不把报告中的局部榜单结论扩写成普遍优势。未公开的商业实现不作推断。\n",
"同一名称的后续实现可能采用不同细节。公式明确标为典型、简化或教学配置时，应按相应范围理解。\n"
]
for name in main:
    num=name[:2]
    used=[r for r in refs if num in r[0].split(",")]
    if not used:
        continue
    sources += [f'<a id="chapter-{num}"></a>\n',f"## {titles[name]}\n"]
    for _,url,title,topic in used:
        if not url.startswith("http"):
            url="https://arxiv.org/abs/"+url
        sources.append(f"- [{title}]({url})：{topic}。")
    sources.append("")
sources += [
"## 版本与时效\n",
"正文重点解释可稳定复用的原理，并纳入公开资料足以核查的现代方法与部分2026年研究实例。资料核查到上述日期，不代表穷尽当日所有模型发布，也不构成性能榜单。\n",
"教学中所用分词、参数规模、向量和概率均按正文标注理解；未声称它们来自某个实际商业模型。\n"
]
(ROOT/"SOURCES.md").write_text("\n".join(sources),encoding="utf-8")

readme=[
f"# {TITLE}\n",
"一部以连续理解为目标的中文长篇教材。早期方法交代思想与边界，Transformer 和现代技术沿着真实的数据、计算、训练与运行过程展开。\n",
f"当前版本：**{DATE}**。包含 **{len(main)} 章正文、2 份附录、{diagrams} 幅原创图解**。正文约 **{cjk:,} 个汉字**，计入公式、英文、标点等约 **{chars:,} 个字符**；统计不重复计算合并版。\n",
"**[从开篇开始阅读](chapters/00-map.md)**　｜　**[合并全文 BOOK.md](BOOK.md)**　｜　**[概念关系索引](chapters/appendix-b-index.md)**\n",
"![全书知识地图](assets/map.png)\n",
"## 怎样读这本书\n",
"按下方顺序阅读即可。每章都有上一篇、下一篇和可展开的本章目录。数学知识随用随解释，保留核心公式和具体数字例子；不要求编程，不安排习题、实验或额外论文阅读任务。\n",
"正文里的“进一步深入”仍属于当前问题，沿着同一机制继续展开。比喻只作辅助，解释会回到参数、向量、分布和实际操作。图像、语音、视频、强化学习与机器人均有独立专题。\n",
"GitHub 在线阅读支持本书使用的公式与图片。合并版用于全文查找或下载保存；较慢设备可优先使用分章版。\n",
'<a id="contents"></a>\n',
"## 全书目录\n"
]
for heading,lo,hi in groups:
    readme.append(f"### {heading}\n")
    for name in main:
        if lo<=int(name[:2])<=hi:
            readme.append(f"- [{titles[name]}](chapters/{name})")
    readme.append("")
readme += [
"### 附录\n",
"- [符号与形状速查](chapters/appendix-a-symbols.md)",
"- [概念关系索引](chapters/appendix-b-index.md)",
"- [方法与事实核查说明](SOURCES.md)\n",
"## 文件说明\n",
"章节正文位于 chapters/；图解同时提供清晰的 PNG 与可编辑 SVG，位于 assets/；BOOK.md 是按阅读顺序合并的同一份内容。\n",
"仓库中的 tools/ 仅用于维护目录、图解和检查，不属于学习内容，阅读不需要运行代码。\n"
]
(ROOT/"README.md").write_text("\n".join(readme),encoding="utf-8")

book=[f"# {TITLE}\n",
f"合并全文 · {DATE} · 与分章版内容一致\n",
"[返回总目录](README.md)　｜　[方法出处](SOURCES.md)\n",
'<a id="contents"></a>\n',"## 合并版目录\n"]
for name in texts:
    book.append(f"- [{titles[name]}](#{keys[name]})")
book.append("\n")

for i,(name,raw) in enumerate(texts.items()):
    names=list(texts)
    previous=f"[← {titles[names[i-1]]}]({names[i-1]})" if i else "开篇"
    following=f"[{titles[names[i+1]]} →]({names[i+1]})" if i+1<len(names) else "全书结束"
    nav=f"{previous}　｜　[总目录](../README.md)　｜　{following}"
    toc=[]
    count=0
    lines=[]
    for line in raw.splitlines():
        if line.startswith("## "):
            count+=1
            anchor=f"s{count:02}"
            toc.append(f"- [{line[3:]}](#{anchor})")
            lines.append(f'<a id="{anchor}"></a>')
        lines.append(line)
    local="\n".join(lines)+"\n"
    first,rest=local.split("\n",1)
    top=(first+"\n\n<!-- generated:nav:start -->\n"+nav+
         "\n<!-- generated:nav:end -->\n\n<!-- generated:toc:start -->\n"+
         "<details>\n<summary>本章目录</summary>\n\n"+"\n".join(toc)+
         "\n\n</details>\n<!-- generated:toc:end -->\n"+rest)
    used=any(name[:2] in r[0].split(",") for r in refs) if name[:2].isdigit() else False
    foot="\n<!-- generated:footer:start -->\n---\n\n"+nav+"\n"
    if used:
        foot+=f"\n[本章方法出处](../SOURCES.md#chapter-{name[:2]})\n"
    foot+="<!-- generated:footer:end -->\n"
    (CH/name).write_text(top+foot,encoding="utf-8")
    merged=raw.replace("../assets/","assets/")
    merged=re.sub(r"^(#{1,5}) ",lambda m:"#"+m.group(1)+" ",merged,flags=re.M)
    for target,key in keys.items():
        merged=merged.replace("]("+target+")","](#"+key+")")
    book += [f'<a id="{keys[name]}"></a>\n',merged]
    if used:
        book.append(f"\n[本章方法出处](SOURCES.md#chapter-{name[:2]})\n")
    book.append("\n---\n")
(ROOT/"BOOK.md").write_text("\n".join(book),encoding="utf-8")

stats={"date":DATE,"main_chapters":len(main),"appendices":len(texts)-len(main),
       "main_cjk_characters":cjk,"main_characters":chars,"diagrams":diagrams,
       "sources":len(refs),"source_sha256":hashlib.sha256("".join(texts.values()).encode()).hexdigest()}
(ROOT/"edition.json").write_text(json.dumps(stats,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps(stats,ensure_ascii=False,indent=2))
