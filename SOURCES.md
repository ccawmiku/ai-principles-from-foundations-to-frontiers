# 方法与事实核查说明

核查日期：2026-10-03。以下用于追溯正文的方法定义和公开案例，不是推荐阅读清单。

基础数学与教学数值例子由本书独立展开。代表论文用于核对方法的结构、目标与公开边界；不把报告中的局部榜单结论扩写成普遍优势。未公开的商业实现不作推断。

同一名称的后续实现可能采用不同细节。公式明确标为典型、简化或教学配置时，应按相应范围理解。

<a id="chapter-05"></a>

## 05　序列问题：从固定窗口、RNN 到注意力

- [Neural Machine Translation by Jointly Learning to Align and Translate](https://arxiv.org/abs/1409.0473)：编码器—解码器注意力。

<a id="chapter-06"></a>

## 06　文字怎样进入模型：token、嵌入与位置

- [RoFormer](https://arxiv.org/abs/2104.09864)：旋转位置编码。

<a id="chapter-07"></a>

## 07　把注意力完整算一遍：Q、K、V 到底在做什么

- [Attention Is All You Need](https://arxiv.org/abs/1706.03762)：缩放点积、多头、原始Transformer。

<a id="chapter-08"></a>

## 08　完整的 Transformer 层：信息汇集以后，还要做什么

- [Attention Is All You Need](https://arxiv.org/abs/1706.03762)：缩放点积、多头、原始Transformer。
- [Layer Normalization](https://arxiv.org/abs/1607.06450)：归一化定义。
- [Root Mean Square Layer Normalization](https://arxiv.org/abs/1910.07467)：RMSNorm。
- [GLU Variants Improve Transformer](https://arxiv.org/abs/2002.05202)：门控前馈网络。

<a id="chapter-09"></a>

## 09　Encoder、Decoder 与信息访问方式

- [Attention Is All You Need](https://arxiv.org/abs/1706.03762)：缩放点积、多头、原始Transformer。
- [BERT](https://arxiv.org/abs/1810.04805)：双向编码与遮蔽预训练。
- [T5: Exploring the Limits of Transfer Learning](https://arxiv.org/abs/1910.10683)：文本到文本与编码器—解码器。

<a id="chapter-12"></a>

## 12　规模、数据与计算：大模型为什么变大

- [Training Compute-Optimal Large Language Models](https://arxiv.org/abs/2203.15556)：模型规模、数据与计算配置。

<a id="chapter-13"></a>

## 13　从续写模型到助手：指令微调、偏好与对齐

- [Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155)：示范与人类反馈训练。
- [Direct Preference Optimization](https://arxiv.org/abs/2305.18290)：直接偏好目标。

<a id="chapter-14"></a>

## 14　强化学习：动作会改变接下来看到的世界

- [Proximal Policy Optimization Algorithms](https://arxiv.org/abs/1707.06347)：PPO裁剪目标。

<a id="chapter-15"></a>

## 15　推理模型：训练与推理时计算怎样共同起作用

- [DeepSeekMath](https://arxiv.org/abs/2402.03300)：GRPO及其背景。
- [DeepSeek-R1](https://arxiv.org/abs/2501.12948)：可验证任务上的强化学习与推理。
- [Qwen3 Technical Report](https://arxiv.org/abs/2505.09388)：推理模式与预算的代表实践。

<a id="chapter-16"></a>

## 16　MoE：参数很多，为什么每次只用一部分

- [DeepSeek-V3 Technical Report](https://arxiv.org/abs/2412.19437)：MoE、MLA和训练系统。

<a id="chapter-17"></a>

## 17　把大模型算得动：注意力、精度、微调和并行

- [DeepSeek-V3 Technical Report](https://arxiv.org/abs/2412.19437)：MoE、MLA和训练系统。
- [FlashAttention](https://arxiv.org/abs/2205.14135)：IO感知的精确注意力计算。
- [GQA](https://arxiv.org/abs/2305.13245)：分组查询注意力。
- [LoRA](https://arxiv.org/abs/2106.09685)：低秩适配。
- [QLoRA](https://arxiv.org/abs/2305.14314)：量化基础权重与低秩微调。
- [Accelerating Large Language Model Decoding with Speculative Sampling](https://arxiv.org/abs/2302.01318)：推测采样。
- [PagedAttention](https://arxiv.org/abs/2309.06180)：KV缓存内存管理。

<a id="chapter-18"></a>

## 18　长上下文、RAG 与记忆：信息怎样在需要时进入计算

- [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401)：检索增强生成。

<a id="chapter-19"></a>

## 19　Agent：从产生答案到与环境形成闭环

- [ReAct](https://arxiv.org/abs/2210.03629)：行动与观察循环。

<a id="chapter-20"></a>

## 20　Transformer 之外：状态空间、线性注意力与混合结构

- [Mamba](https://arxiv.org/abs/2312.00752)：选择性状态空间模型。
- [Transformers are SSMs](https://arxiv.org/abs/2405.21060)：状态空间对偶与Mamba-2。
- [Gated Delta Networks](https://arxiv.org/abs/2412.06464)：门控、Delta规则与混合架构。

<a id="chapter-21"></a>

## 21　视觉模型：从像素、卷积到 ViT

- [Deep Residual Learning for Image Recognition](https://arxiv.org/abs/1512.03385)：残差视觉网络。
- [An Image is Worth 16x16 Words](https://arxiv.org/abs/2010.11929)：ViT与图像块。
- [End-to-End Object Detection with Transformers](https://arxiv.org/abs/2005.12872)：DETR与集合式检测。
- [Segment Anything](https://arxiv.org/abs/2304.02643)：提示式分割。

<a id="chapter-22"></a>

## 22　表示学习：相似性、对比学习与自监督视觉

- [Learning Transferable Visual Models From Natural Language Supervision](https://arxiv.org/abs/2103.00020)：CLIP图文对比学习。
- [Masked Autoencoders Are Scalable Vision Learners](https://arxiv.org/abs/2111.06377)：MAE。
- [Emerging Properties in Self-Supervised Vision Transformers](https://arxiv.org/abs/2104.14294)：DINO教师学生自监督。
- [Self-Supervised Learning from Images with a Joint-Embedding Predictive Architecture](https://arxiv.org/abs/2301.08243)：I-JEPA表示预测。

<a id="chapter-23"></a>

## 23　多模态理解：语言模型怎样读取图像、声音和视频

- [Visual Instruction Tuning](https://arxiv.org/abs/2304.08485)：视觉指令学习。
- [Qwen2.5-VL Technical Report](https://arxiv.org/abs/2502.13923)：动态视觉输入与视觉语言系统。

<a id="chapter-24"></a>

## 24　生成模型的几条路线：自回归、VAE、GAN 与流

- [Auto-Encoding Variational Bayes](https://arxiv.org/abs/1312.6114)：VAE及重参数化。
- [Generative Adversarial Networks](https://arxiv.org/abs/1406.2661)：GAN。

<a id="chapter-25"></a>

## 25　扩散模型：为什么学习去噪能够生成图像

- [Denoising Diffusion Probabilistic Models](https://arxiv.org/abs/2006.11239)：DDPM训练与采样。
- [Denoising Diffusion Implicit Models](https://arxiv.org/abs/2010.02502)：DDIM。
- [Score-Based Generative Modeling through Stochastic Differential Equations](https://arxiv.org/abs/2011.13456)：Score与连续生成视角。
- [High-Resolution Image Synthesis with Latent Diffusion Models](https://arxiv.org/abs/2112.10752)：潜在扩散。

<a id="chapter-26"></a>

## 26　Flow Matching 与 DiT：学习从噪声走向数据的速度

- [Flow Matching for Generative Modeling](https://arxiv.org/abs/2210.02747)：流匹配。
- [Flow Straight and Fast](https://arxiv.org/abs/2209.03003)：Rectified Flow。
- [Scalable Diffusion Models with Transformers](https://arxiv.org/abs/2212.09748)：DiT。
- [Consistency Models](https://arxiv.org/abs/2303.01469)：一致性生成。

<a id="chapter-27"></a>

## 27　条件生成与编辑：让图像满足具体要求

- [Classifier-Free Diffusion Guidance](https://arxiv.org/abs/2207.12598)：无分类器引导。
- [Adding Conditional Control to Text-to-Image Diffusion Models](https://arxiv.org/abs/2302.05543)：ControlNet。

<a id="chapter-28"></a>

## 28　视频生成：空间、时间与一致性怎样一起建模

- [Step-Video-T2V Technical Report](https://arxiv.org/abs/2502.10248)：视频VAE、DiT与流匹配。
- [HunyuanVideo 1.5 Technical Report](https://arxiv.org/abs/2511.18870)：视频架构、注意力与分阶段训练。

<a id="chapter-29"></a>

## 29　语音技术：波形、识别、合成与音频 token

- [Robust Speech Recognition via Large-Scale Weak Supervision](https://arxiv.org/abs/2212.04356)：Whisper代表路线。
- [High Fidelity Neural Audio Compression](https://arxiv.org/abs/2210.13438)：神经音频压缩与离散码。

<a id="chapter-30"></a>

## 30　实时多模态：怎样一边听、一边看、一边回应

- [Qwen3-Omni Technical Report](https://arxiv.org/abs/2509.17765)：实时全模态与Thinker–Talker实例。

<a id="chapter-31"></a>

## 31　世界模型与机器人：预测未来还不等于会行动

- [Diffusion Policy](https://arxiv.org/abs/2303.04137)：生成式动作策略。
- [Mastering Diverse Domains through World Models](https://arxiv.org/abs/2301.04104)：Dreamer世界模型与想象训练。
- [Qwen-RobotWorld Technical Report](https://arxiv.org/abs/2606.17030)：2026年动作条件视频世界建模实例。
- [NeRF](https://arxiv.org/abs/2003.08934)：神经辐射场。
- [3D Gaussian Splatting for Real-Time Radiance Field Rendering](https://arxiv.org/abs/2308.04079)：三维高斯场景表示。

<a id="chapter-32"></a>

## 32　图学习、科学 AI 与因果问题

- [Accurate structure prediction of biomolecular interactions with AlphaFold 3](https://www.nature.com/articles/s41586-024-07487-w)：分子结构预测与验证边界。

<a id="chapter-35"></a>

## 35　较新的方向：改变生成顺序、计算分配与学习闭环

- [Qwen3 Technical Report](https://arxiv.org/abs/2505.09388)：推理模式与预算的代表实践。
- [Gated Delta Networks](https://arxiv.org/abs/2412.06464)：门控、Delta规则与混合架构。
- [Qwen-RobotWorld Technical Report](https://arxiv.org/abs/2606.17030)：2026年动作条件视频世界建模实例。
- [Large Language Diffusion Models](https://arxiv.org/abs/2502.09992)：LLaDA离散扩散语言建模。

## 版本与时效

正文重点解释可稳定复用的原理，并纳入公开资料足以核查的现代方法与部分2026年研究实例。资料核查到上述日期，不代表穷尽当日所有模型发布，也不构成性能榜单。

教学中所用分词、参数规模、向量和概率均按正文标注理解；未声称它们来自某个实际商业模型。
