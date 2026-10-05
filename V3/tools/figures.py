"""Rebuild original V2 teaching diagrams and an analytic distribution plot."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'assets';OUT.mkdir(exist_ok=True)
font_manager.fontManager.addfont('/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc')
plt.rcParams.update({'font.family':'Noto Sans CJK JP','axes.unicode_minus':False,'font.size':11,'svg.fonttype':'path'})
colors=['#5c6bc0','#d08097','#2c8b87','#bd873a']
x=np.linspace(-5,5,1601)
fig,axs=plt.subplots(2,2,figsize=(10,6.8),sharex=True,sharey=True)
for ax,a,col in zip(axs.flat,[1,.8,.5,0],colors):
    sd=np.sqrt(a*a*.2*.2+1-a*a)
    pdf=sum(np.exp(-.5*((x-m)/sd)**2)/(sd*np.sqrt(2*np.pi))*.5 for m in [-2*a,2*a])
    ax.plot(x,pdf,color=col,lw=2.5);ax.fill_between(x,pdf,color=col,alpha=.12)
    ax.set_title(f'信号系数 a = {a:g}');ax.grid(alpha=.18);ax.set_ylim(0,1.1)
    ax.set_xlabel('扰动后数值');ax.set_ylabel('概率密度')
fig.suptitle('两个数据模式逐渐混入噪声',fontsize=17,y=.99)
fig.text(.5,.01,'教学解析分布：原数据为 ±2 附近、标准差 0.2 的等权高斯混合；ε ~ N(0, 1)',ha='center',fontsize=10)
fig.tight_layout(rect=[0,.04,1,.95])
for ext in ['svg','png']:fig.savefig(OUT/f'diffusion-mixture.{ext}',dpi=180,bbox_inches='tight')
plt.close(fig)

def diagram(name,title,boxes,edges,note,figsize=(11,5)):
    fig,ax=plt.subplots(figsize=figsize);ax.set_xlim(0,12);ax.set_ylim(0,6);ax.axis('off')
    ax.text(6,5.65,title,ha='center',fontsize=17,color='#293443')
    centers={}
    for key,xx,yy,label,c in boxes:
        w,h=2.35,.88;centers[key]=(xx,yy)
        ax.add_patch(FancyBboxPatch((xx-w/2,yy-h/2),w,h,boxstyle='round,pad=.12',facecolor=c,edgecolor='#8c9bac',lw=1))
        ax.text(xx,yy,label,ha='center',va='center',fontsize=11,color='#263441')
    for start,end,label in edges:
        x1,y1=centers[start];x2,y2=centers[end]; dx,dy=x2-x1,y2-y1
        if abs(dx)>abs(dy): x1+=np.sign(dx)*1.3;x2-=np.sign(dx)*1.3
        else:y1+=np.sign(dy)*.58;y2-=np.sign(dy)*.58
        ax.add_patch(FancyArrowPatch((x1,y1),(x2,y2),arrowstyle='-|>',mutation_scale=15,color='#63758b',lw=1.4))
        if label:ax.text((x1+x2)/2,(y1+y2)/2+.14,label,ha='center',fontsize=9,color='#506178',bbox={'facecolor':'white','edgecolor':'none','pad':1.5})
    ax.text(6,.22,note,ha='center',va='center',fontsize=10,color='#536277',wrap=True)
    for ext in ['svg','png']:fig.savefig(OUT/f'{name}.{ext}',dpi=180,bbox_inches='tight')
    plt.close(fig)
light='#eaf0ff';pink='#faeaf0';green='#e7f3ee';cream='#fff1da'
diagram('learning-cycle','一次学习：参数改变与独立检查',[('data',1.8,4.3,'输入与目标\n仅使用允许信息',light),('pred',5.8,4.3,'当前参数 → 预测\n与目标比较损失',pink),('grad',10,4.3,'梯度与优化器\n更新参数',green),('eval',5.8,2,'验证／测试数据\n检查新条件表现',cream)],[('data','pred','前向'),('pred','grad','反向'),('grad','eval','新参数'),('data','eval','独立划分')],'验证可用于选择；最终测试保持独立。运行时输入改变通常不等于权重更新。')
diagram('attention-flow','注意力：匹配关系与被汇集的信息',[('input',1.7,4.2,'位置表示 X\n学习投影',light),('qk',5.7,4.2,'Q 与 K → 匹配分数\n缩放、掩码、Softmax',pink),('weights',10,4.2,'注意力权重\n决定当前汇集比例',green),('values',1.7,2,'V：待汇集的向量\n也来自学习投影',cream),('out',8,2,'权重 × V → 输出\n多头拼接后再投影',light)],[('input','qk',''),('qk','weights',''),('input','values',''),('values','out',''),('weights','out','')],'权重表达当前位置的匹配分布，不是事实真值或整模型的完整解释。')
diagram('agent-boundary','Agent：候选动作跨过执行边界',[('model',1.8,4.3,'模型读取任务状态\n提出动作和参数',light),('runner',5.8,4.3,'运行器核查\n接口、范围、权限',pink),('world',10,4.3,'工具／外部环境\n真正执行与返回',green),('state',5.8,2,'状态与证据\n成功、未知、失败分开',cream)],[('model','runner','候选'),('runner','world','允许后执行'),('world','state','实际观察'),('state','model','下一轮条件')],'外部材料不产生授权；写出调用不等于执行成功；完成依据来自实际结果。')
diagram('multimodal-flow','多模态：信息连接与证据来源',[('image',1.8,4.3,'图片／视频／音频\n编码与位置、时间',light),('align',5.8,4.3,'连接／投影／对齐\n形成可用条件',pink),('model',10,4.3,'主干与输出\n理解或生成任务',green),('text',1.8,2,'问题与资料\n型号、版本和目标',cream),('check',10,2,'核对各模态证据\n不将先验当观察',light)],[('image','align',''),('align','model',''),('text','align',''),('model','check','')],'宽度匹配不等于语义对齐；缩放、压缩、采样可能丢失关键细节。')
print('Generated 5 teaching figures in PNG and SVG')
