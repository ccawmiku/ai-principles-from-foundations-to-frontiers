# AI 原理：从早期方法到现代智能系统 · V2

**六卷、60 章，正文 206,076 汉字。已完成全书制作、自评与优化，保存在本地。**

面向希望系统理解 AI、但不准备深入编程和数学推导的读者。我们从具体问题出发，沿着输入、表示、计算、目标与反馈慢慢展开：规则为什么有用，学习怎样改变参数，模型怎样生成内容，又怎样通过工具与环境组成真正的系统。

语言保持亲近、轻快，难点多停留一会儿；故事进入实际数据与计算，关键结论、比较和图解帮助回看。正文不设置练习，也不要求运行代码或额外读论文。

## 开始阅读

可以从第一卷顺序读起；每卷导读恢复所需前提。每章有折叠目录和前后导航。想连续搜索或整本阅读，可以打开 [全书合并版](BOOK.md)。

| 卷 | 阅读入口 | 章节 | 正文汉字 |
|---|---|---:|---:|
| AI 怎样成为一门技术 | [卷前导读](volumes/01-foundations/README.md) | 01—10 | 29,710 |
| 神经网络怎样处理信息 | [卷前导读](volumes/02-networks/README.md) | 11—20 | 35,006 |
| 现代语言模型怎样形成能力 | [卷前导读](volumes/03-language/README.md) | 21—30 | 36,818 |
| AI 怎样理解与生成多种内容 | [卷前导读](volumes/04-multimodal/README.md) | 31—42 | 38,636 |
| AI 怎样决策、行动和探索 | [卷前导读](volumes/05-action/README.md) | 43—52 | 35,957 |
| 怎样理解 AI 的能力与整个系统 | [卷前导读](volumes/06-capabilities/README.md) | 53—60 | 29,949 |

## 分章目录

### AI 怎样成为一门技术

| 章 | 正文 |
|---|---|
| 01 | [当知识被写成规则：早期 AI 到底在计算什么](volumes/01-foundations/01.md) |
| 02 | [规则告诉我们能做什么，搜索帮助我们选择怎么做](volumes/01-foundations/02.md) |
| 03 | [报警之后，故障到底有多可能](volumes/01-foundations/03.md) |
| 04 | [从历史记录到预测：一个可调整的模型](volumes/01-foundations/04.md) |
| 05 | [数值变成类别：分类、分数与概率](volumes/01-foundations/05.md) |
| 06 | [数据不只是原料：标签、任务与质量](volumes/01-foundations/06.md) |
| 07 | [一棵树怎样做判断，多棵树怎样互相帮助](volumes/01-foundations/07.md) |
| 08 | [传统学习的其他路线：距离、边界、压缩与结构](volumes/01-foundations/08.md) |
| 09 | [推荐、排序与检索：找到东西和猜对类别有什么不同](volumes/01-foundations/09.md) |
| 10 | [学会了训练数据，为什么还要检查新数据](volumes/01-foundations/10.md) |

### 神经网络怎样处理信息

| 章 | 正文 |
|---|---|
| 11 | [多层数字变换怎样形成可以学习的表示](volumes/02-networks/11.md) |
| 12 | [一次训练怎样改变参数](volumes/02-networks/12.md) |
| 13 | [让深网络稳定训练：步长、批次与信息通路](volumes/02-networks/13.md) |
| 14 | [图片的局部结构为什么催生卷积](volumes/02-networks/14.md) |
| 15 | [时间顺序为什么需要状态](volumes/02-networks/15.md) |
| 16 | [文字进入模型以前：token、嵌入与位置](volumes/02-networks/16.md) |
| 17 | [把注意力完整算一遍](volumes/02-networks/17.md) |
| 18 | [一层 Transformer 怎样把信息继续处理下去](volumes/02-networks/18.md) |
| 19 | [Encoder、Decoder 与信息访问方式](volumes/02-networks/19.md) |
| 20 | [Transformer 之外：另一种信息保存与交互方式](volumes/02-networks/20.md) |

### 现代语言模型怎样形成能力

| 章 | 正文 |
|---|---|
| 21 | [预测下一个 token 为什么能训练出广泛能力](volumes/03-language/21.md) |
| 22 | [参数、数据与计算为什么一起决定规模](volumes/03-language/22.md) |
| 23 | [从续写到助手：示范、偏好与奖励](volumes/03-language/23.md) |
| 24 | [一句话怎样逐个 token 生成出来](volumes/03-language/24.md) |
| 25 | [推理模型把更多计算花在哪里](volumes/03-language/25.md) |
| 26 | [MoE 怎样在大量参数中选择本次使用的部分](volumes/03-language/26.md) |
| 27 | [更低精度、更小更新：量化、微调和压缩](volumes/03-language/27.md) |
| 28 | [大模型怎样分给设备并算得更快](volumes/03-language/28.md) |
| 29 | [上下文为什么会变长，又为什么不等于记忆](volumes/03-language/29.md) |
| 30 | [RAG 从文档走到回答，中间有哪些步骤](volumes/03-language/30.md) |

### AI 怎样理解与生成多种内容

| 章 | 正文 |
|---|---|
| 31 | [一张图片有哪些可计算的结构](volumes/04-multimodal/31.md) |
| 32 | [识别一张图和找出图里的对象](volumes/04-multimodal/32.md) |
| 33 | [没有逐张标签，视觉模型还能学到什么](volumes/04-multimodal/33.md) |
| 34 | [生成模型怎样描述和产生数据](volumes/04-multimodal/34.md) |
| 35 | [加噪与去噪怎样变成图像生成](volumes/04-multimodal/35.md) |
| 36 | [流匹配与 DiT 怎样改变生成的计算](volumes/04-multimodal/36.md) |
| 37 | [生成图像怎样遵守条件并修改已有内容](volumes/04-multimodal/37.md) |
| 38 | [一段声音怎样变成文字](volumes/04-multimodal/38.md) |
| 39 | [文字怎样变成语音和其他声音](volumes/04-multimodal/39.md) |
| 40 | [一个模型怎样同时读取多种输入](volumes/04-multimodal/40.md) |
| 41 | [视频为什么比连续生成图片更难](volumes/04-multimodal/41.md) |
| 42 | [一边听、一边看、一边回应](volumes/04-multimodal/42.md) |

### AI 怎样决策、行动和探索

| 章 | 正文 |
|---|---|
| 43 | [一次行动为什么要看后来的结果](volumes/05-action/43.md) |
| 44 | [从价值判断到选择动作](volumes/05-action/44.md) |
| 45 | [直接改进策略会发生什么](volumes/05-action/45.md) |
| 46 | [规则、目标与规划：先想好怎样到达](volumes/05-action/46.md) |
| 47 | [为什么相关性不能直接告诉我们该怎么做](volumes/05-action/47.md) |
| 48 | [Agent 怎样调用工具并维持任务](volumes/05-action/48.md) |
| 49 | [长任务为什么需要记忆、检查和分工](volumes/05-action/49.md) |
| 50 | [世界模型怎样预测行动之后的变化](volumes/05-action/50.md) |
| 51 | [从模拟走到机器人：感知、控制和行动学习](volumes/05-action/51.md) |
| 52 | [AI 怎样面对科学中的结构与探索](volumes/05-action/52.md) |

### 怎样理解 AI 的能力与整个系统

| 章 | 正文 |
|---|---|
| 53 | [模型的知识、理解和推理该怎样判断](volumes/06-capabilities/53.md) |
| 54 | [可解释性怎样从观察走向检验](volumes/06-capabilities/54.md) |
| 55 | [一个分数怎样成为模型进步的证据](volumes/06-capabilities/55.md) |
| 56 | [幻觉与失效怎样发生，又怎样减少](volumes/06-capabilities/56.md) |
| 57 | [安全、隐私与滥用防护改变系统哪些环节](volumes/06-capabilities/57.md) |
| 58 | [能力背后的系统、成本与部署条件](volumes/06-capabilities/58.md) |
| 59 | [前沿方法究竟在改变哪一步](volumes/06-capabilities/59.md) |
| 60 | [把全书接起来：三个完整系统](volumes/06-capabilities/60.md) |

## 回看与项目记录

- [符号与形状速查](appendices/SYMBOLS.md) · [概念关系索引](appendices/CONCEPTS.md)
- [方法、案例与实际核查范围](sources/README.md)
- [自评、优化与验收记录](REVIEW.md) · [实施计划与完成状态](PLAN.md)
- [需求与验收标准](REQUIREMENTS.md) · [覆盖设计](OUTLINE.md) · [写作规范](STYLE.md) · [原版基线](BASELINE.md)

## 版本与保存

原版目录、正文、图片和生成文件保持原状，V2 的内容与工具全部独立位于此目录。用户提供的历史原文没有保存。GitHub 读取成功，但当前集成的内容写入返回 403；按用户授权，本次交付保存到本地 Git，未上传远端。

字数只计六十章与卷前导读的正文汉字；标题、导航、自动目录、项目文档、附录、来源和合并版不计入下限，也不把原版另算一份。约 29 万字曾是立项预算，实际交付按解释需要完成，满足二十万字下限。

维护时可运行 `python V2/tools/build.py`、`python V2/tools/numerics.py` 和 `python V2/tools/check.py --final`。新图的源文件在 `tools/figures.py`；这些工具只读或写 V2，普通阅读不需要运行它们。
