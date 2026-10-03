# 附录 B　概念关系索引

<!-- generated:nav:start -->
[← 附录 A　符号与形状速查](appendix-a-symbols.md)　｜　[总目录](../README.md)　｜　全书结束
<!-- generated:nav:end -->

<!-- generated:toc:start -->
<details>
<summary>本章目录</summary>

- [几组容易放错层次的概念](#s01)

</details>
<!-- generated:toc:end -->

这个索引用于找到概念在主线中的位置，不要求独立背诵。链接指向相应完整章节。

| 概念 | 应怎样定位 | 主要章节 |
|---|---|---|
| 人工智能 | 广泛任务与方法领域，不等于某一种神经网络 | [全书地图](00-map.md) |
| 符号主义、专家系统 | 显式知识与推理规则 | [早期路线](01-history.md) |
| 搜索、规划 | 组织候选行动或解答的探索 | [历史](01-history.md)、[强化学习](14-reinforcement-learning.md) |
| 参数 | 跨输入长期共享、通常通过训练调整的数字 | [神经网络](03-neural-networks.md) |
| 激活 | 当前输入经过网络产生的中间结果 | [神经网络](03-neural-networks.md) |
| 损失 | 训练优化的代理目标 | [学习目标](02-learning.md) |
| 反向传播 | 高效计算参数梯度 | [训练](04-training.md) |
| 优化器 | 根据梯度及状态修改参数 | [训练](04-training.md) |
| Token | 分词或其他编码方案定义的处理单位 | [文字表示](06-tokens.md) |
| Embedding | 输入符号或对象的连续表示 | [文字表示](06-tokens.md) |
| 自注意力 | 同一序列内部的信息汇集 | [注意力](07-attention.md) |
| 交叉注意力 | 一个序列读取另一个序列表示 | [架构](09-architectures.md) |
| Q/K/V | 匹配接收方、匹配提供方和传递内容 | [完整计算](07-attention.md) |
| 残差 | 将模块更新量加回已有表示 | [完整层](08-transformer-block.md) |
| FFN | 每个位置内部的非线性变换 | [完整层](08-transformer-block.md) |
| LayerNorm/RMSNorm | 特定轴上的数值尺度处理 | [完整层](08-transformer-block.md) |
| RoPE | 用位置相关旋转影响查询键匹配 | [位置](06-tokens.md) |
| 因果掩码 | 限制信息读取方向 | [注意力](07-attention.md) |
| 预训练 | 形成广泛基础表示与预测能力 | [预训练](10-pretraining.md) |
| 自回归 | 用已有前缀逐步确定后续变量 | [架构](09-architectures.md) |
| 温度、top-p | 从预测分布选择输出的规则 | [推理](11-inference.md) |
| KV Cache | 缓存可复用的历史键值计算 | [推理](11-inference.md) |
| SFT | 利用示范调整条件响应行为 | [后训练](13-posttraining.md) |
| RLHF | 使用人类反馈构造奖励并优化策略的一类流程 | [后训练](13-posttraining.md) |
| DPO | 相对参考策略直接学习偏好对 | [后训练](13-posttraining.md) |
| PPO/GRPO | 不同策略优化组织方式 | [强化学习](14-reinforcement-learning.md)、[推理模型](15-reasoning.md) |
| 推理时计算 | 在运行阶段增加步骤、候选、搜索或验证 | [推理模型](15-reasoning.md) |
| MoE | 按输入选择部分专家模块执行 | [混合专家](16-moe.md) |
| FlashAttention | 改善注意力的访存与计算组织 | [效率](17-efficiency.md) |
| GQA/MQA | 多查询头共享较少键值头 | [效率](17-efficiency.md) |
| 量化 | 用低位表示近似权重或其他数值 | [效率](17-efficiency.md) |
| LoRA | 用低秩参数表达微调增量 | [效率](17-efficiency.md) |
| 蒸馏 | 让学生学习教师行为或表示 | [效率](17-efficiency.md) |
| RAG | 检索证据后进行条件生成 | [检索与记忆](18-context-rag.md) |
| Agent | 模型、工具与环境形成行动反馈循环 | [智能体](19-agents.md) |
| SSM/Mamba | 以结构化或选择性状态更新处理序列 | [其他架构](20-state-space.md) |
| CNN | 局部连接与共享核的视觉或序列结构 | [视觉](21-vision.md) |
| ViT | 把图像块作为token处理的Transformer | [视觉](21-vision.md) |
| CLIP | 通过图文对比形成可比较表示 | [表示学习](22-representation-learning.md) |
| 多模态理解 | 连接不同模态表示以完成理解任务 | [多模态](23-multimodal.md) |
| VAE | 带潜在分布约束的概率编码解码模型 | [生成路线](24-generative-models.md) |
| GAN | 通过生成器与判别器的对抗反馈学习 | [生成路线](24-generative-models.md) |
| Diffusion | 学习扰动过程对应的逆向生成 | [扩散](25-diffusion.md) |
| Score | 对数密度对样本坐标的梯度 | [扩散](25-diffusion.md) |
| Flow Matching | 学习概率路径对应的速度场 | [流匹配](26-flow-matching.md) |
| DiT | 扩散或相关生成任务使用的Transformer主干 | [流匹配与DiT](26-flow-matching.md) |
| CFG | 组合条件与无条件预测来调整引导 | [生成控制](27-generation-control.md) |
| 视频生成 | 联合处理外观、时间与运动约束 | [视频](28-video.md) |
| CTC | 对多种合法帧级对齐路径求和训练 | [语音](29-speech.md) |
| 音频codec token | 压缩声学表示的离散码本索引 | [语音](29-speech.md) |
| 全双工 | 输入监听与输出生成可并行进行的交互方式 | [实时多模态](30-realtime-multimodal.md) |
| VLA | 将视觉语言条件映射到动作的模型 | [机器人](31-world-models-robotics.md) |
| 世界模型 | 对环境状态或未来观察进行预测的模型 | [世界模型](31-world-models-robotics.md) |
| GNN | 根据图连接进行消息传递的网络 | [图与科学](32-graphs-science.md) |
| 机理解释 | 研究中间表示和模块怎样因果影响行为 | [可解释性](33-knowledge-interpretability.md) |
| 校准 | 检查置信估计与实际正确率的关系 | [评估](34-evaluation.md) |
| 文本扩散 | 对离散文本定义扰动与迭代恢复生成 | [较新方向](35-frontiers.md) |

<a id="s01"></a>
## 几组容易放错层次的概念

Transformer与扩散可以同时描述一个模型，前者是结构，后者是生成建模路线。MoE与RLHF也可以同时成立，前者分配内部计算，后者描述反馈训练。RAG与微调可组合，前者改变本次条件，后者改变长期参数。

“生成”可能指下一token采样，也可能指潜在数组的迭代演化；“记忆”可能在权重、上下文、缓存或外部数据库；“推理”可能指一次前向计算，也可能指多步逻辑求解。理解具体语境比认定某个词永远只有一个意思更重要。

需要把这些关系重新接起来时，可以直接回到[三条完整计算链](36-whole-system.md)。

<!-- generated:footer:start -->
---

[← 附录 A　符号与形状速查](appendix-a-symbols.md)　｜　[总目录](../README.md)　｜　全书结束
<!-- generated:footer:end -->
