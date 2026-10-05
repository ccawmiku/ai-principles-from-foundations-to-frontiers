# 方法、案例与事实依据

这里用于追溯正文，不是给读者安排额外阅读任务。正文里的设备、数据、参数、动作与数值过程均为明确标注的教学配置；真实项目与公开方法另列来源。

## 核查范围

- `access-audit.json` 记录 60 项采用候选文献的公开题名、页面和摘要核查；不代表逐页审读全部全文。
- `additional-audit.json` 记录基础教材、历史概览、解释与隐私方法的网页或书目核查，失败请求也保留。
- `chapter-sources.json` 将这些依据对应到 V2 章节。跨卷重复引用说明同一方法在不同任务中使用。
- `numerical-audit.json` 与 `tools/numerics.py` 独立复算正文的 62 项数值检查，包括有限差分核对反向传播梯度；核算范围不扩展为全部事实证明。
- `original-references.json` 是原版文献归档，未核查条目不自动采用；其中未能验证的 Qwen-RobotWorld 条目未用于 V2 正文。

历史主张采用 DENDRAL、MYCIN 的公开概览与既有书目定位，以及 [IBM Deep Blue 历史页](https://www.ibm.com/history/deep-blue)。DENDRAL 用来说明化学领域知识参与候选结构处理；MYCIN 用来说明专家规则、推理与确定性因子，未把该因子等同严格概率，也未声称它普遍进入临床执行。MYCIN 另有 Buchanan 与 Shortliffe 主编的 *Rule-Based Expert Systems*（1984）这一可追溯书目。

本次斯坦福展览入口返回 Request Rejected，尝试的 MYCIN 书页地址返回 404；随后取得维基百科二手概览，只核对项目基本定位，不使用无法取得依据的细节或引语。Sutton 与 Barto 的个人站点请求失败，MIT Press 出版书目可取得。失败入口不标成已阅读全文。

正文对早期历史保持简要，对现代机制采用通用、可追踪的解释。涉及具体产品报告，只表述公开报告中相应任务和机制定位，不将报告性能自动推广成所有条件下的结论。前沿覆盖至本次实际可核查的公开条目，不宣称覆盖尚未验证的新版本。

## AI 怎样成为一门技术

| 章节 | 方法与案例依据 |
|---|---|
| [01 当知识被写成规则：早期 AI 到底在计算什么](../volumes/01-foundations/01.md) | [Dendral](https://en.wikipedia.org/wiki/Dendral)；[MYCIN](https://en.wikipedia.org/wiki/MYCIN)；[Artificial Intelligence: A Modern Approach](https://aima.cs.berkeley.edu/) |
| [02 规则告诉我们能做什么，搜索帮助我们选择怎么做](../volumes/01-foundations/02.md) | [Artificial Intelligence: A Modern Approach](https://aima.cs.berkeley.edu/) |
| [03 报警之后，故障到底有多可能](../volumes/01-foundations/03.md) | [Deep Learning](https://www.deeplearningbook.org/) |
| [04 从历史记录到预测：一个可调整的模型](../volumes/01-foundations/04.md) | [An Introduction to Statistical Learning](https://www.statlearning.com/)；[Deep Learning](https://www.deeplearningbook.org/) |
| [05 数值变成类别：分类、分数与概率](../volumes/01-foundations/05.md) | [An Introduction to Statistical Learning](https://www.statlearning.com/)；[Deep Learning](https://www.deeplearningbook.org/) |
| [06 数据不只是原料：标签、任务与质量](../volumes/01-foundations/06.md) | [An Introduction to Statistical Learning](https://www.statlearning.com/) |
| [07 一棵树怎样做判断，多棵树怎样互相帮助](../volumes/01-foundations/07.md) | [An Introduction to Statistical Learning](https://www.statlearning.com/) |
| [08 传统学习的其他路线：距离、边界、压缩与结构](../volumes/01-foundations/08.md) | [An Introduction to Statistical Learning](https://www.statlearning.com/) |
| [09 推荐、排序与检索：找到东西和猜对类别有什么不同](../volumes/01-foundations/09.md) | [An Introduction to Statistical Learning](https://www.statlearning.com/) |
| [10 学会了训练数据，为什么还要检查新数据](../volumes/01-foundations/10.md) | [An Introduction to Statistical Learning](https://www.statlearning.com/) |

## 神经网络怎样处理信息

| 章节 | 方法与案例依据 |
|---|---|
| [11 多层数字变换怎样形成可以学习的表示](../volumes/02-networks/11.md) | [Deep Residual Learning for Image Recognition](https://arxiv.org/abs/1512.03385)；[Deep Learning](https://www.deeplearningbook.org/) |
| [12 一次训练怎样改变参数](../volumes/02-networks/12.md) | [Deep Learning](https://www.deeplearningbook.org/) |
| [13 让深网络稳定训练：步长、批次与信息通路](../volumes/02-networks/13.md) | [Layer Normalization](https://arxiv.org/abs/1607.06450)；[Root Mean Square Layer Normalization](https://arxiv.org/abs/1910.07467)；[Deep Residual Learning for Image Recognition](https://arxiv.org/abs/1512.03385)；[Adam: A Method for Stochastic Optimization](https://arxiv.org/abs/1412.6980)；[Deep Learning](https://www.deeplearningbook.org/) |
| [14 图片的局部结构为什么催生卷积](../volumes/02-networks/14.md) | [Deep Residual Learning for Image Recognition](https://arxiv.org/abs/1512.03385) |
| [15 时间顺序为什么需要状态](../volumes/02-networks/15.md) | [Neural Machine Translation by Jointly Learning to Align and Translate](https://arxiv.org/abs/1409.0473) |
| [16 文字进入模型以前：token、嵌入与位置](../volumes/02-networks/16.md) | [RoFormer](https://arxiv.org/abs/2104.09864) |
| [17 把注意力完整算一遍](../volumes/02-networks/17.md) | [Neural Machine Translation by Jointly Learning to Align and Translate](https://arxiv.org/abs/1409.0473)；[Attention Is All You Need](https://arxiv.org/abs/1706.03762)；[GQA](https://arxiv.org/abs/2305.13245) |
| [18 一层 Transformer 怎样把信息继续处理下去](../volumes/02-networks/18.md) | [Attention Is All You Need](https://arxiv.org/abs/1706.03762)；[Layer Normalization](https://arxiv.org/abs/1607.06450)；[Root Mean Square Layer Normalization](https://arxiv.org/abs/1910.07467)；[GLU Variants Improve Transformer](https://arxiv.org/abs/2002.05202) |
| [19 Encoder、Decoder 与信息访问方式](../volumes/02-networks/19.md) | [Neural Machine Translation by Jointly Learning to Align and Translate](https://arxiv.org/abs/1409.0473)；[Attention Is All You Need](https://arxiv.org/abs/1706.03762)；[BERT](https://arxiv.org/abs/1810.04805)；[T5: Exploring the Limits of Transfer Learning](https://arxiv.org/abs/1910.10683) |
| [20 Transformer 之外：另一种信息保存与交互方式](../volumes/02-networks/20.md) | [Mamba](https://arxiv.org/abs/2312.00752)；[Transformers are SSMs](https://arxiv.org/abs/2405.21060)；[Gated Delta Networks](https://arxiv.org/abs/2412.06464) |

## 现代语言模型怎样形成能力

| 章节 | 方法与案例依据 |
|---|---|
| [21 预测下一个 token 为什么能训练出广泛能力](../volumes/03-language/21.md) | [BERT](https://arxiv.org/abs/1810.04805)；[T5: Exploring the Limits of Transfer Learning](https://arxiv.org/abs/1910.10683)；[Training Compute-Optimal Large Language Models](https://arxiv.org/abs/2203.15556) |
| [22 参数、数据与计算为什么一起决定规模](../volumes/03-language/22.md) | [Training Compute-Optimal Large Language Models](https://arxiv.org/abs/2203.15556) |
| [23 从续写到助手：示范、偏好与奖励](../volumes/03-language/23.md) | [Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155)；[Direct Preference Optimization](https://arxiv.org/abs/2305.18290)；[Proximal Policy Optimization Algorithms](https://arxiv.org/abs/1707.06347) |
| [24 一句话怎样逐个 token 生成出来](../volumes/03-language/24.md) | [GQA](https://arxiv.org/abs/2305.13245)；[Accelerating Large Language Model Decoding with Speculative Sampling](https://arxiv.org/abs/2302.01318)；[PagedAttention](https://arxiv.org/abs/2309.06180) |
| [25 推理模型把更多计算花在哪里](../volumes/03-language/25.md) | [DeepSeekMath](https://arxiv.org/abs/2402.03300)；[DeepSeek-R1](https://arxiv.org/abs/2501.12948)；[Qwen3 Technical Report](https://arxiv.org/abs/2505.09388) |
| [26 MoE 怎样在大量参数中选择本次使用的部分](../volumes/03-language/26.md) | [DeepSeek-V3 Technical Report](https://arxiv.org/abs/2412.19437) |
| [27 更低精度、更小更新：量化、微调和压缩](../volumes/03-language/27.md) | [LoRA](https://arxiv.org/abs/2106.09685)；[QLoRA](https://arxiv.org/abs/2305.14314) |
| [28 大模型怎样分给设备并算得更快](../volumes/03-language/28.md) | [FlashAttention](https://arxiv.org/abs/2205.14135)；[GQA](https://arxiv.org/abs/2305.13245)；[Accelerating Large Language Model Decoding with Speculative Sampling](https://arxiv.org/abs/2302.01318)；[PagedAttention](https://arxiv.org/abs/2309.06180) |
| [29 上下文为什么会变长，又为什么不等于记忆](../volumes/03-language/29.md) | [RoFormer](https://arxiv.org/abs/2104.09864)；[Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401) |
| [30 RAG 从文档走到回答，中间有哪些步骤](../volumes/03-language/30.md) | [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401) |

## AI 怎样理解与生成多种内容

| 章节 | 方法与案例依据 |
|---|---|
| [31 一张图片有哪些可计算的结构](../volumes/04-multimodal/31.md) | [An Image is Worth 16x16 Words](https://arxiv.org/abs/2010.11929) |
| [32 识别一张图和找出图里的对象](../volumes/04-multimodal/32.md) | [End-to-End Object Detection with Transformers](https://arxiv.org/abs/2005.12872)；[Segment Anything](https://arxiv.org/abs/2304.02643)；[NeRF](https://arxiv.org/abs/2003.08934)；[3D Gaussian Splatting for Real-Time Radiance Field Rendering](https://arxiv.org/abs/2308.04079) |
| [33 没有逐张标签，视觉模型还能学到什么](../volumes/04-multimodal/33.md) | [Learning Transferable Visual Models From Natural Language Supervision](https://arxiv.org/abs/2103.00020)；[Masked Autoencoders Are Scalable Vision Learners](https://arxiv.org/abs/2111.06377)；[Emerging Properties in Self-Supervised Vision Transformers](https://arxiv.org/abs/2104.14294)；[Self-Supervised Learning from Images with a Joint-Embedding Predictive Architecture](https://arxiv.org/abs/2301.08243) |
| [34 生成模型怎样描述和产生数据](../volumes/04-multimodal/34.md) | [Auto-Encoding Variational Bayes](https://arxiv.org/abs/1312.6114)；[Generative Adversarial Networks](https://arxiv.org/abs/1406.2661) |
| [35 加噪与去噪怎样变成图像生成](../volumes/04-multimodal/35.md) | [Denoising Diffusion Probabilistic Models](https://arxiv.org/abs/2006.11239)；[Denoising Diffusion Implicit Models](https://arxiv.org/abs/2010.02502)；[Score-Based Generative Modeling through Stochastic Differential Equations](https://arxiv.org/abs/2011.13456)；[High-Resolution Image Synthesis with Latent Diffusion Models](https://arxiv.org/abs/2112.10752) |
| [36 流匹配与 DiT 怎样改变生成的计算](../volumes/04-multimodal/36.md) | [Flow Matching for Generative Modeling](https://arxiv.org/abs/2210.02747)；[Flow Straight and Fast](https://arxiv.org/abs/2209.03003)；[Scalable Diffusion Models with Transformers](https://arxiv.org/abs/2212.09748)；[Consistency Models](https://arxiv.org/abs/2303.01469) |
| [37 生成图像怎样遵守条件并修改已有内容](../volumes/04-multimodal/37.md) | [Classifier-Free Diffusion Guidance](https://arxiv.org/abs/2207.12598)；[Adding Conditional Control to Text-to-Image Diffusion Models](https://arxiv.org/abs/2302.05543) |
| [38 一段声音怎样变成文字](../volumes/04-multimodal/38.md) | [Robust Speech Recognition via Large-Scale Weak Supervision](https://arxiv.org/abs/2212.04356) |
| [39 文字怎样变成语音和其他声音](../volumes/04-multimodal/39.md) | [High Fidelity Neural Audio Compression](https://arxiv.org/abs/2210.13438) |
| [40 一个模型怎样同时读取多种输入](../volumes/04-multimodal/40.md) | [Learning Transferable Visual Models From Natural Language Supervision](https://arxiv.org/abs/2103.00020)；[Visual Instruction Tuning](https://arxiv.org/abs/2304.08485)；[Qwen2.5-VL Technical Report](https://arxiv.org/abs/2502.13923) |
| [41 视频为什么比连续生成图片更难](../volumes/04-multimodal/41.md) | [Step-Video-T2V Technical Report](https://arxiv.org/abs/2502.10248)；[HunyuanVideo 1.5 Technical Report](https://arxiv.org/abs/2511.18870) |
| [42 一边听、一边看、一边回应](../volumes/04-multimodal/42.md) | [Qwen3-Omni Technical Report](https://arxiv.org/abs/2509.17765) |

## AI 怎样决策、行动和探索

| 章节 | 方法与案例依据 |
|---|---|
| [43 一次行动为什么要看后来的结果](../volumes/05-action/43.md) | [Reinforcement Learning: An Introduction, second edition](https://mitpress.mit.edu/9780262039246/reinforcement-learning/) |
| [44 从价值判断到选择动作](../volumes/05-action/44.md) | [Reinforcement Learning: An Introduction, second edition](https://mitpress.mit.edu/9780262039246/reinforcement-learning/) |
| [45 直接改进策略会发生什么](../volumes/05-action/45.md) | [Proximal Policy Optimization Algorithms](https://arxiv.org/abs/1707.06347)；[Reinforcement Learning: An Introduction, second edition](https://mitpress.mit.edu/9780262039246/reinforcement-learning/) |
| [46 规则、目标与规划：先想好怎样到达](../volumes/05-action/46.md) | [Artificial Intelligence: A Modern Approach](https://aima.cs.berkeley.edu/) |
| [47 为什么相关性不能直接告诉我们该怎么做](../volumes/05-action/47.md) | [Causality](https://bayes.cs.ucla.edu/BOOK-2K/) |
| [48 Agent 怎样调用工具并维持任务](../volumes/05-action/48.md) | [ReAct](https://arxiv.org/abs/2210.03629) |
| [49 长任务为什么需要记忆、检查和分工](../volumes/05-action/49.md) | [ReAct](https://arxiv.org/abs/2210.03629) |
| [50 世界模型怎样预测行动之后的变化](../volumes/05-action/50.md) | [Mastering Diverse Domains through World Models](https://arxiv.org/abs/2301.04104) |
| [51 从模拟走到机器人：感知、控制和行动学习](../volumes/05-action/51.md) | [Diffusion Policy](https://arxiv.org/abs/2303.04137) |
| [52 AI 怎样面对科学中的结构与探索](../volumes/05-action/52.md) | [Accurate structure prediction of biomolecular interactions with AlphaFold 3](https://www.nature.com/articles/s41586-024-07487-w)；[Causality](https://bayes.cs.ucla.edu/BOOK-2K/) |

## 怎样理解 AI 的能力与整个系统

| 章节 | 方法与案例依据 |
|---|---|
| [53 模型的知识、理解和推理该怎样判断](../volumes/06-capabilities/53.md) | [BERT](https://arxiv.org/abs/1810.04805)；[T5: Exploring the Limits of Transfer Learning](https://arxiv.org/abs/1910.10683)；[DeepSeek-R1](https://arxiv.org/abs/2501.12948)；[Deep Learning](https://www.deeplearningbook.org/) |
| [54 可解释性怎样从观察走向检验](../volumes/06-capabilities/54.md) | [A Unified Approach to Interpreting Model Predictions](https://arxiv.org/abs/1705.07874)；[Axiomatic Attribution for Deep Networks](https://arxiv.org/abs/1703.01365)；[Towards Monosemanticity: Decomposing Language Models With Dictionary Learning](https://transformer-circuits.pub/2023/monosemantic-features/index.html) |
| [55 一个分数怎样成为模型进步的证据](../volumes/06-capabilities/55.md) | [An Introduction to Statistical Learning](https://www.statlearning.com/) |
| [56 幻觉与失效怎样发生，又怎样减少](../volumes/06-capabilities/56.md) | [An Introduction to Statistical Learning](https://www.statlearning.com/) |
| [57 安全、隐私与滥用防护改变系统哪些环节](../volumes/06-capabilities/57.md) | [Deep Learning with Differential Privacy](https://arxiv.org/abs/1607.00133) |
| [58 能力背后的系统、成本与部署条件](../volumes/06-capabilities/58.md) | 成本、版本、缓存和服务流程为教学系统；与第 28 章的公开计算与缓存方法相接。 |
| [59 前沿方法究竟在改变哪一步](../volumes/06-capabilities/59.md) | [Mamba](https://arxiv.org/abs/2312.00752)；[Transformers are SSMs](https://arxiv.org/abs/2405.21060)；[Gated Delta Networks](https://arxiv.org/abs/2412.06464)；[Large Language Diffusion Models](https://arxiv.org/abs/2502.09992)；[Deep Learning](https://www.deeplearningbook.org/) |
| [60 把全书接起来：三个完整系统](../volumes/06-capabilities/60.md) | [Attention Is All You Need](https://arxiv.org/abs/1706.03762)；[Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401)；[Denoising Diffusion Probabilistic Models](https://arxiv.org/abs/2006.11239)；[Flow Matching for Generative Modeling](https://arxiv.org/abs/2210.02747)；[Diffusion Policy](https://arxiv.org/abs/2303.04137) |

## 图解依据与可重建源文件

V2 新绘的训练、注意力、Agent、多模态图是计算与数据流概览；扩散混合分布图由明确的等权高斯混合与扰动关系解析生成。可重建源在 [figures.py](../tools/figures.py)，PNG 用于正文，SVG 可用于放大和编辑。迁移的原版图解已复制到 V2 并核对相对链接；它们不改写原版图片。

来源记录支持追溯和后续更新。网页可访问、算术正确、机制解释与实验有效性是不同证据层级；每项记录只声称本次实际完成的核查。
