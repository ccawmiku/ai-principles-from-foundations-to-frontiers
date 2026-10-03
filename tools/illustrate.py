"""Generate original, editable SVG diagrams and matching PNGs for the book."""
from pathlib import Path
from html import escape
import math
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets"
OUT.mkdir(exist_ok=True)
FONT = Path("C:/Windows/Fonts/msyh.ttc")
BOLD = Path("C:/Windows/Fonts/msyhbd.ttc")
if not FONT.exists():
    FONT = Path("/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc")
    BOLD = Path("/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc")
if not FONT.exists():
    raise RuntimeError("Install a Chinese font; set FONT and BOLD paths in this script.")

INK="#142e45"
MUTED="#4f6375"
BLUE="#e9f3ff"
PURPLE="#f0eafb"
GOLD="#fff2d6"
GREEN="#e7f4ed"
PALE="#f0f3f6"
EDGE="#69829a"

class Diagram:
    def __init__(self,name,title,subtitle,height=720,width=1500):
        self.name=name
        self.w=width
        self.h=height
        self.im=Image.new("RGB",(width,height),"white")
        self.d=ImageDraw.Draw(self.im)
        self.svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img">',
                  f'<title>{escape(title)}</title>',
                  '<rect width="100%" height="100%" fill="white"/>']
        self.text(45,30,title,38,True)
        self.text(45,85,subtitle,24,color=MUTED)
    def font(self,size,bold=False):
        return ImageFont.truetype(str(BOLD if bold else FONT),size)
    def text(self,x,y,t,size=25,bold=False,color=INK):
        self.d.text((x,y),t,font=self.font(size,bold),fill=color)
        self.svg.append(f'<text x="{x}" y="{y+size}" font-family="Microsoft YaHei,Noto Sans CJK SC,sans-serif" font-size="{size}" font-weight="{700 if bold else 400}" fill="{color}">{escape(t)}</text>')
    def rect(self,x,y,w,h,fill=BLUE):
        self.d.rounded_rectangle((x,y,x+w,y+h),radius=14,fill=fill,outline=EDGE,width=2)
        self.svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="{fill}" stroke="{EDGE}" stroke-width="2"/>')
    def box(self,x,y,w,h,title,lines=(),fill=BLUE):
        self.rect(x,y,w,h,fill)
        size=29
        while self.d.textlength(title,font=self.font(size,True))>w-28:
            size-=1
        self.text(x+14,y+12,title,size,True)
        cursor=y+size+28
        for line in lines:
            s=24
            while self.d.textlength(line,font=self.font(s))>w-28:
                s-=1
            if s<17:
                raise ValueError((self.name,title,line,"text too small"))
            self.text(x+14,cursor,line,s,color=MUTED)
            cursor+=s+10
        if cursor>y+h+8:
            raise ValueError((self.name,title,"box overflow"))
    def arrow(self,points,label=None,labelxy=None,color=EDGE):
        self.d.line(points,fill=color,width=3)
        x,y=points[-1]
        px,py=points[-2]
        angle=math.atan2(y-py,x-px)
        wing=[(x,y),
              (x-13*math.cos(angle-.5),y-13*math.sin(angle-.5)),
              (x-13*math.cos(angle+.5),y-13*math.sin(angle+.5))]
        self.d.polygon(wing,fill=color)
        pts=" ".join(f"{a},{b}" for a,b in points)
        tri=" ".join(f"{a},{b}" for a,b in wing)
        self.svg.append(f'<polyline points="{pts}" fill="none" stroke="{color}" stroke-width="3"/>')
        self.svg.append(f'<polygon points="{tri}" fill="{color}"/>')
        if label:
            self.text(*labelxy,label,22,color=MUTED)
    def note(self,y,lines):
        for i,line in enumerate(lines):
            self.text(45,y+34*i,line,23,color=MUTED)
    def save(self):
        self.svg.append("</svg>")
        (OUT/f"{self.name}.svg").write_text("\n".join(self.svg),encoding="utf-8")
        self.im.save(OUT/f"{self.name}.png",optimize=True)

def row(name,title,subtitle,nodes,notes):
    a=Diagram(name,title,subtitle,height=600)
    gap=35
    w=(1410-gap*(len(nodes)-1))//len(nodes)
    for i,(head,lines,fill) in enumerate(nodes):
        x=45+i*(w+gap)
        a.box(x,210,w,170,head,lines,fill)
        if i:
            a.arrow([(x-gap,295),(x,295)])
    a.note(435,notes)
    a.save()

a=Diagram("training","一次训练：前向、梯度与参数更新","蓝色：本次数据与中间结果　紫色：可训练参数　黄色：监督与损失")
a.box(45,185,210,130,"输入 x",["当前样本"])
a.box(340,185,250,130,"模型 fθ",["读取参数计算"])
a.box(675,185,240,130,"预测 ŷ",["本次前向结果"])
a.box(1050,185,350,130,"损失 L(ŷ,y)",["将预测与目标比较"],GOLD)
a.box(1050,365,350,105,"训练目标 y",["来自数据或反馈"],GOLD)
a.box(340,495,250,120,"参数 θ",["长期保存的权重"],PURPLE)
a.box(690,495,270,120,"优化器",["依据梯度更新 θ"],PURPLE)
for p in [[(255,250),(340,250)],[(590,250),(675,250)],[(915,250),(1050,250)],[(1225,365),(1225,315)],[(1225,315),(1225,550),(960,550)],[(690,550),(590,550)],[(465,495),(465,315)]]:
    a.arrow(p)
a.text(980,510,"反向传播得到梯度",22,color=MUTED)
a.note(650,["常规推理固定参数；训练才会执行损失、反向传播与参数更新。"])
a.save()

a=Diagram("attention","注意力：先决定比例，再传递内容","本图省略批次和多头轴；每行对应一个接收位置。",height=720,width=1600)
a.box(40,300,190,120,"输入 X",["n × d"])
a.box(335,150,215,105,"Q = XWQ",["n × dk"])
a.box(335,310,215,105,"K = XWK",["n × dk"])
a.box(335,505,215,105,"V = XWV",["n × dv"])
a.box(665,260,235,150,"分数 S",["QKᵀ / √dk","n × n"])
a.box(1000,260,255,150,"权重 A",["掩码 + 逐行 Softmax","n × n"])
a.box(1330,405,230,140,"输出 O",["O = AV","n × dv"])
for p in [[(230,360),(280,360),(280,202),(335,202)],[(230,360),(335,360)],[(230,360),(280,360),(280,557),(335,557)],[(550,202),(615,202),(615,305),(665,305)],[(550,362),(665,362)],[(900,335),(1000,335)],[(1255,335),(1445,335),(1445,405)],[(550,557),(1210,557),(1210,475),(1330,475)]]:
    a.arrow(p)
a.note(640,["WQ、WK、WV 是参数；Q、K、V 和 A 随当前输入变化。",
            "注意力 Softmax 沿位置归一化；输出词表的 Softmax 是另一处运算。"])
a.save()

a=Diagram("block","一个 Pre-Norm Transformer 层","序列长度 n 与主干宽度 d 保持一致；不同模块更新同一残差表示。",height=630)
items=[("X",["n × d"],BLUE),("Norm",["按位置归一化"],PALE),("Attention",["跨位置汇集"],BLUE),("+",["得到 U"],GREEN),("Norm + FFN",["位置内非线性"],BLUE),("+",["得到 Y"],GREEN)]
xs=[45,255,465,735,945,1270]
ws=[155,155,215,155,270,155]
for x,w,(h,ls,c) in zip(xs,ws,items):
    a.box(x,250,w,140,h,ls,c)
for i in range(5):
    a.arrow([(xs[i]+ws[i],320),(xs[i+1],320)])
a.arrow([(120,250),(120,170),(810,170),(810,250)],"保留 X",(390,130))
a.arrow([(810,390),(810,460),(1345,460),(1345,390)],"保留 U",(1040,470))
a.note(540,["输出投影保证注意力回到 d 维；FFN 内部可扩宽，输出仍回到 d 维。"])
a.save()

a=Diagram("kv-cache","KV Cache：复用固定前缀的计算","每一层拥有自己的缓存；新 token 只产生该位置的新 Q/K/V。",height=650)
a.box(45,190,290,140,"已有前缀",["位置 1 … n","先进行 prefill"])
a.box(440,190,410,140,"各层 K/V 缓存",["K1…Kn　V1…Vn","历史位置无需重复投影"],PURPLE)
a.box(1030,190,360,140,"新 token 的 Q",["与所有可见 K 匹配","按权重汇总 V"])
a.arrow([(335,260),(440,260)])
a.arrow([(850,260),(1030,260)])
a.box(1030,405,360,120,"新 K、V",["追加到对应层缓存"])
a.arrow([(1210,330),(1210,405)])
a.arrow([(1030,465),(645,465),(645,330)])
a.note(560,["缓存减少重复计算，但新查询仍需读取历史；缓存长度增加仍有成本。"])
a.save()

a=Diagram("moe","稀疏专家：选择内部模块，不是让完整模型投票","一个 token 可以在不同层被路由到不同专家。",height=760)
a.box(45,295,205,140,"当前表示 x",["单个 token"])
a.box(325,295,250,140,"路由器",["计算各专家分数","选择 Top-k"],PURPLE)
for i,y in enumerate([145,285,425,565]):
    a.box(740,y,270,105,f"专家 {i+1}",["独立 FFN 参数"],BLUE if i<2 else PALE)
a.box(1190,295,265,145,"加权合并",["输出回到 d 维","再进入残差流"],GREEN)
a.arrow([(250,365),(325,365)])
for y in [197,337]:
    a.arrow([(575,365),(645,365),(645,y),(740,y)])
    a.arrow([(1010,y),(1100,y),(1100,365),(1190,365)])
a.note(700,["浅灰专家未被本 token 选中；其他 token 仍可能使用它们。"])
a.save()

row("rag","RAG：先找证据，再条件生成","检索与生成是两个可分别出错的环节。",[
("文档库",["内容 + 来源","版本与元数据"],PALE),
("检索候选",["关键词 / 向量","按问题找片段"],BLUE),
("过滤与重排",["相关性与版本","补充上下文"],BLUE),
("组织上下文",["问题 + 证据","保留来源边界"],GOLD),
("生成与核查",["证据支持结论？","是否仍缺信息？"],GREEN)
],["向量相似不等于证据充分；长上下文也不能补回没有检索到的关键条款。"])

a=Diagram("agent","Agent：行动—观察闭环","参数通常不在每轮更新；改变的是上下文、环境与下一步决策。",height=650)
a.box(45,220,300,145,"模型策略",["读取目标与观察","生成动作或回答"])
a.box(480,220,310,145,"执行器",["验证参数与权限","实际调用工具"],PURPLE)
a.box(965,220,420,145,"外部环境",["文件、程序、网页或设备","动作造成实际结果"],GOLD)
a.arrow([(345,290),(480,290)])
a.arrow([(790,290),(965,290)])
a.arrow([(1175,365),(1175,490),(195,490),(195,365)],"结果与新观察",(610,450))
a.note(565,["说“已经完成”是文本；环境最终状态与独立验证才提供完成证据。"])
a.save()

row("vision","视觉表示：像素 → 图像块 → 特征","教学尺寸：224 × 224 的 RGB 图像，使用 16 × 16 图像块。",[
("像素数组",["224 × 224 × 3","空间排列有意义"],BLUE),
("切为图像块",["14 × 14 = 196 块","每块 768 个数"],BLUE),
("线性映射",["196 × d","加入位置信息"],PURPLE),
("视觉主干",["块之间交换信息","输出视觉表示"],BLUE),
("任务输出",["分类 / 区域特征","分割或多模态接口"],GREEN)
],["视觉 token 通常是连续向量，不必来自与文字相同的离散词表。"])

row("multimodal","视觉语言模型：图像不必先变成一句话","一种常见连接方案；其他模型可以使用交叉注意力或联合主干。",[
("图像",["像素与空间结构","可动态切块"],BLUE),
("视觉编码器",["m × dv 特征","保留区域信息"],PURPLE),
("连接模块",["映射 / 压缩","变成 m′ × dl"],PURPLE),
("语言主干",["视觉向量 + 问题","按掩码交互"],BLUE),
("文字输出",["生成条件分布","逐 token 回答"],GREEN)
],["训练让语言主干学会使用视觉证据；强语言先验也可能导致视觉幻觉。"])

a=Diagram("diffusion","扩散：训练与生成知道的东西不同","网络学习分布上的恢复信息；生成没有一张预先藏好的目标图。",height=740)
xs=[45,410,775,1140]
for x,h,ls,c in [
(xs[0],"真实样本 x₀",["训练数据"],BLUE),
(xs[1],"构造带噪 xₜ",["已知 x₀、噪声、阶段"],BLUE),
(xs[2],"预测噪声",["网络读 xₜ 与阶段"],PURPLE),
(xs[3],"训练损失",["与已知噪声比较"],GOLD)]:
    a.box(x,180,305,130,h,ls,c)
for i in range(3): a.arrow([(xs[i]+305,245),(xs[i+1],245)])
a.text(45,140,"训练",26,True)
for x,h,ls,c in [
(xs[0],"随机噪声 xT",["没有真实目标图"],BLUE),
(xs[1],"迭代采样",["预测 + 采样公式"],PURPLE),
(xs[2],"数据端潜在",["多步演化的结果"],BLUE),
(xs[3],"解码图片",["潜在扩散使用解码器"],GREEN)]:
    a.box(x,430,305,130,h,ls,c)
for i in range(3): a.arrow([(xs[i]+305,495),(xs[i+1],495)])
a.text(45,385,"生成",26,True)
a.note(625,["生成使用训练后的固定参数；不同初始噪声可以得到不同合理样本。",
            "网络、预测参数化、噪声日程与采样器必须相互匹配。"])
a.save()

row("flow","流匹配：从端点构造监督，再学习速度场","本图 t=0 是噪声，t=1 是数据；与 DDPM 的编号习惯不同。",[
("采样两端",["噪声 xnoise","数据 xdata"],BLUE),
("选择 t",["xt = (1−t)xnoise","       + t xdata"],BLUE),
("预测速度",["vθ(xt,t,c)","监督：xdata−xnoise"],PURPLE),
("生成时积分",["x ← x + Δt · vθ","从噪声走向数据"],GREEN)
],["单条训练插值可为直线；汇总学习到的边缘速度场仍可能产生弯曲轨迹。"])

row("video","视频生成：时间是另一条必须建模的轴","T 个潜在时刻、每时刻 S 个空间块，共 TS 个 token。",[
("视频数据",["T × H × W × C","动作与相机运动"],BLUE),
("时空压缩",["空间与时间降采样","潜在视频数组"],PURPLE),
("时空 token",["时间 + 高度 + 宽度","文字与图像条件"],BLUE),
("DiT 迭代",["全局 / 分解 / 稀疏","预测噪声或速度"],PURPLE),
("解码与检查",["外观、运动、身份","跨帧与条件一致性"],GREEN)
],["全注意力交互约 (TS)²；分解计算改变信息路径，不能只看省下的运算数。"])

row("speech","语音的三种时间尺度","波形采样点、声学帧和文本 token 的数量通常相差很大。",[
("波形",["每秒数万采样点","包含相位与音色"],BLUE),
("声学表示",["频谱或学习特征","时间压缩后的帧"],BLUE),
("对齐 / 编码",["CTC、转导或注意力","处理长度差异"],PURPLE),
("文字或音频码",["内容与声学结构","不等于同一类 token"],BLUE),
("输出",["转写 / 理解 / 波形","按任务选择解码器"],GREEN)
],["CTC 对合法对齐路径求和；音频码本则服务于声学重建。两者职责不同。"])

row("world","行动与世界模型：预测必须接受真实反馈","语言目标与连续控制通过表示、策略和执行器连接。",[
("观察与目标",["图像 + 传感器","语言条件"],BLUE),
("状态与候选",["估计当前状态","提出动作序列"],BLUE),
("预测与选择",["世界模型推演","代价 / 奖励 / 约束"],PURPLE),
("执行一部分",["真实执行器","底层反馈控制"],GOLD),
("再次观察",["检测偏差与失败","重新规划"],GREEN)
],["虚拟轨迹可能利用模型误差；真实闭环成功不能只由生成视频的观感证明。"])

a=Diagram("state-space","两种历史信息组织方式","两条分支分别展示显式历史与压缩状态；也可以在同一模型中组合。",height=650)
a.box(45,270,275,140,"历史输入",["x1, x2, …, xt","顺序进入系统"])
a.box(515,160,390,140,"显式位置缓存",["保留多组 K/V","当前查询重新读取"],PURPLE)
a.box(515,390,390,140,"压缩状态",["ht = At ht−1 + Bt xt","状态大小可固定"],GOLD)
a.box(1100,270,330,140,"后续计算",["选择性检索或持续预测","按任务需求评价"],GREEN)
for p in [[(320,340),(410,340),(410,230),(515,230)],
          [(320,340),(410,340),(410,460),(515,460)],
          [(905,230),(1000,230),(1000,340),(1100,340)],
          [(905,460),(1000,460),(1000,340),(1100,340)]]:
    a.arrow(p)
a.note(580,["紧凑状态节约存储，显式位置便于回溯；二者的表达与成本需要分别比较。"])
a.save()

a=Diagram("map","现代 AI 的五条连接线","结构、训练目标和运行系统是不同层次，可以在一个模型中组合。",height=760)
data=[
("学习基础",["参数与表示","损失、梯度、泛化"],BLUE),
("序列计算",["RNN、注意力","Transformer、SSM"],PURPLE),
("训练与推理",["预训练、偏好、RL","搜索、验证、预算"],GOLD),
("感知与生成",["视觉、声音、视频","扩散、流、联合模型"],BLUE),
("环境与科学",["工具、动作、图结构","世界模型与验证"],GREEN)]
for i,(h,ls,c) in enumerate(data):
    x=45+i*292
    a.box(x,230,250,190,h,ls,c)
    if i:a.arrow([(x-42,325),(x,325)])
a.note(485,["贯穿问题一：当前处理的是哪一种数据，形状如何变化？",
            "贯穿问题二：哪些数字是参数，哪些只是本次计算的中间结果？",
            "贯穿问题三：训练信号从哪里来，怎样影响实际行为？",
            "贯穿问题四：哪些结果由模型产生，哪些由工具、采样或环境提供？"])
a.save()

print(f"Generated {len(list(OUT.glob('*.svg')))} SVG/PNG diagram pairs.")
