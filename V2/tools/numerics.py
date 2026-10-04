"""Independently compute the textbook's worked numbers and a gradient check."""
from pathlib import Path
import math,json,hashlib,re
ROOT=Path(__file__).resolve().parents[1]
checks=[]
def verify(ch,name,actual,expected,tol=1e-10):
    actual=actual if isinstance(actual,(list,tuple)) else [actual]
    expected=expected if isinstance(expected,(list,tuple)) else [expected]
    err=max(abs(a-b) for a,b in zip(actual,expected))
    checks.append({'chapter':ch,'example':name,'computed':actual,'printed_or_exact_target':expected,'tolerance':tol,'max_error':err,'pass':len(actual)==len(expected) and err<=tol})
def sm(xs):
 e=[math.exp(x-max(xs)) for x in xs];return [x/sum(e) for x in e]
verify(2,'shortest route',[1+2+2,2+4],[5,6])
verify(3,'Bayes single alarm',90/(90+495),.15384615384615385)
verify(3,'two conditionally independent alarms',324/(324+99),.7659574468085106)
verify(3,'changed prevalence',1800/(1800+400),.8181818181818182)
for w,mse in [(.2,168),(.4,56/3),(.5,0)]:
 verify(4,f'regression w={w}',sum((w*x+40-y)**2 for x,y in zip([20,40,60],[50,60,70]))/3,mse)
verify(5,'class score construction',[.8*1.5-.2*2+.8,.9*2-.1*1.5+.35],[1.6,2])
verify(5,'class probabilities',sm([1.6,2,0]),[.371,.554,.075],.001)
verify(5,'negative log losses',[-math.log(p) for p in [.9,.5,.1,.01]],[.105,.693,2.303,4.605],.001)
verify(7,'Gini reduction',.5-.375,.125)
verify(8,'PCA projected coordinates',[(x-2+2*(y-4))/math.sqrt(5) for x,y in [(1,2),(2,4),(3,6)]],[-math.sqrt(5),0,math.sqrt(5)])
verify(10,'imbalanced classification',[16/65,16/20,947/1000,4*100+49*2],[.246,.8,.947,498],.001)
def forward(p):
 w11,w12,b1,w21,w22,b2,v1,v2,bout=p
 h1=max(0,w11*2+w12+b1);h2=max(0,w21*2+w22+b2)
 return v1*h1+v2*h2+bout
params=[1,.5,-1,-.5,2,0,2,-1,.5]
verify(11,'network forward',forward(params),2.5)
def loss(p):return .5*(forward(p)-4)**2
verify(12,'network initial loss',loss(params),1.125)
analytic=[-6,-3,-3,3,1.5,1.5,-2.25,-1.5,-1.5]
grad=[]
for i in range(len(params)):
 a=params[:];b=params[:];a[i]+=1e-5;b[i]-=1e-5
 grad.append((loss(a)-loss(b))/(2e-5))
verify(12,'finite difference all network gradients',grad,analytic,1e-8)
for lr,target in [(.1,.405),(.05,.045)]:
 p=params[:];p[0]-=lr*analytic[0];verify(12,f'one weight step {lr}',loss(p),target)
verify(13,'quadratic descent .25',[0-.25*(-6),1.5-.25*(-3)],[1.5,2.25])
m=0;out=[]
for g in [4,4,-1]:m=.9*m+.1*g;out.append(m)
verify(13,'momentum history',out,[.4,.76,.584])
verify(13,'gradient norm clipping',[3/5,4/5],[.6,.8])
verify(14,'convolution window',1-2+3-4,-2)
verify(15,'LSTM memory',.9*1.5+.2*.4,1.43)
a=sm([0,2/math.sqrt(2),1/math.sqrt(2)])
verify(17,'attention weights',a,[.140,.576,.284],.001)
verify(17,'attention weighted values',[a[0]+a[2],2*a[1]+a[2]],[.424,1.436],.001)
a=sm([0,2/math.sqrt(2)])
verify(17,'masked attention',[a[0],2*a[1]],[.196,1.609],.001)
verify(18,'residual then layer norm',[(x-2.75)/.25 for x in [2.5,3]],[-1,1])
verify(20,'state recurrence',[.2,.8*.2,.8*.8*.2],[.2,.16,.128])
verify(21,'four token average loss',sum(-math.log(p) for p in [.4,.5,.2,.8])/4,.860,.001)
verify(21,'logit loss gradients',[.2,.5-1,.3],[.2,-.5,.3])
verify(23,'reward model pair',1/(1+math.exp(-2)),.881,.001)
verify(23,'DPO relative pair',1/(1+math.exp(-.2*((-8+9)-(-10+10.5)))),.525,.001)
verify(24,'temperature .5',sm([math.log(p)/.5 for p in [.6,.3,.1]]),[.783,.196,.022],.001)
verify(24,'temperature 2',sm([math.log(p)/2 for p in [.6,.3,.1]]),[.473,.334,.193],.001)
verify(25,'independent five attempts',1-.8**5,.67232)
verify(27,'LoRA parameter fraction',(4096*8*2)/(4096**2),.00390625)
verify(28,'KV cache bytes',24*400*4*64*2*2,9830400)
verify(32,'intersection over union',9/(16+16-9),9/23)
verify(34,'VAE reparameterization',[.5+.2*1,-1+.3*(-2)],[.7,-1.6])
verify(35,'noise and reconstruction',[.8*2+.6*(-1),(1-.6*(-1))/.8],[1,2])
verify(36,'flow state and update',[(1-.25)*(-1)+.25*1,.25*2,-.5+.1*2,.5+.1*2],[-.5,.5,-.3,.7])
verify(38,'audio sample count and frame rate',[16000*60,1/.01],[960000,100])
verify(40,'visual block count',(224/16)**2,196)
verify(43,'discounted alternatives',[-1+.8*10,2+.8*(-10)],[7,-6])
verify(43,'current Bellman action estimates',[-2+.9*(.8*(-5)+.2*(-20)),-2.5+.9*(.95*(-5)+.05*(-20))],[-9.2,-7.675])
verify(44,'TD single step',5+.1*(1+.9*6-5),5.14)
qs=qa=0;rows=[]
for _ in range(3):qs+=.5*(-1+.9*qa-qs);qa+=.5*(5-qa);rows.extend([qs,qa])
verify(44,'three two-step episodes',rows,[-.5,2.5,.375,3.75,1.375,4.375])
verify(45,'policy good action probability',sm([math.log(2/3)+.072,-.072])[0],.435,.001)
verify(45,'PPO positive and negative clipped terms',[min(1.25*1.2,1.2*1.2),min(.7*(-.8),.8*(-.8))],[1.44,-.64])
verify(46,'serial and overlapped maintenance durations',[10+2+15+8+10+12,max(10+2,12)+15+8+10],[57,45])
verify(47,'standardized causal proportions',[.5*.2+.5*0,.5*.3+.5*.1],[.1,.2])
verify(47,'inverse propensity weighted proportions',[(18/.9+0/.1)/(90/.9+10/.1),(3/.1+9/.9)/(10/.1+90/.9)],[.1,.2])
rows=[]
for u0,u1 in [(0,0),(1,0),(0,1),(1,1)]:
 t=.9*30+2-.5*u0;rows.extend([t,.9*t+2-.5*u1])
verify(50,'four MPC action sequences',rows,[29,28.1,28.5,27.65,29,27.6,28.5,27.15])
verify(51,'coordinate rotation and translation',[-.1+1,.2],[.9,.2])
verify(52,'acquisition scores kappa 1',[80+2,77+8,72+1],[82,85,73])
verify(55,'deployment distribution reweighting',[.5*(66/80)+.5*(14/20),.5*(76/80)+.5*(6/20)],[.7625,.625])
verify(55,'Bernoulli standard error',math.sqrt(.8*.2/100),.04)
verify(56,'selective coverage and accuracy',[70/100,63/70],[.7,.9])
verify(58,'cost with retry and per success',[10000*(.02+.003+.005+.004)+1000*(.02+.005),345/9000],[345,.03833333333333333])
verify(3,'HMM observation and filter',[.09/(.09+.18),(.8/3+.1*2/3),(.1/3)/(.1/3+.8*2/3)],[1/3,1/3,1/17])
verify(57,'equal error rates unequal precision',[16/65,80/125],[.246,.64],.001)
verify(58,'energy and emissions',[2*1,2*.4],[2,.8])
config=json.loads((ROOT/'structure.json').read_text())
def cleaned(p):
 s=p.read_text();s=re.sub(r'<!-- v2:(?:nav|toc|footer):start -->.*?<!-- v2:(?:nav|toc|footer):end -->\n?','',s,flags=re.S)
 s=re.sub(r'<a id="section-\d+"></a>\n','',s)
 return re.sub(r'\n{3,}','\n\n',s).strip()+'\n'
report={'scope':'Worked numerical examples, not a proof of all prose or methods','passed':sum(c['pass'] for c in checks),'total':len(checks),'source_sha256':hashlib.sha256(''.join(cleaned(ROOT/c['path']) for c in config['chapters']).encode()).hexdigest(),'checks':checks}
(ROOT/'sources/numerical-audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k!='checks'},ensure_ascii=False))
for c in checks:
 if not c['pass']:print('FAILED',c)
raise SystemExit(report['passed']!=report['total'])
