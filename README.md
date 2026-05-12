# Hello-Agents 学习摘要与复习笔记

> 本仓库用于整理 Datawhale 开源教程 [Hello-Agents：《从零开始构建智能体》](https://datawhalechina.github.io/hello-agents/#/) 的学习摘要、章节复习脑图、习题答案与个人总结。

## 项目定位

Hello-Agents 是 Datawhale 社区推出的系统性智能体学习教程，目标是帮助学习者从大语言模型的使用者，逐步成长为能够设计、实现和评估智能体系统的构建者。

本地仓库不是原项目源码的镜像，而是围绕原教程建立的学习笔记仓库，主要用于：

- 汇总每章核心概念和知识脉络
- 保存 XMind 复习脑图，便于回顾章节结构
- 整理习题答案、实践心得和易错点
- 为后续补充代码实验、案例复盘和面试总结预留空间

## 原教程核心内容

Hello-Agents 的内容从基础理论到应用实践逐步展开，覆盖智能体系统构建的主要知识链路：

| 模块 | 学习重点 | 关键词 |
| --- | --- | --- |
| 第一部分：智能体与语言模型基础 | 建立智能体和大语言模型的基础认知 | Agent 定义、发展史、LLM、Transformer、Prompt |
| 第二部分：构建大语言模型智能体 | 动手实现典型智能体范式与应用框架 | ReAct、Plan-and-Solve、Reflection、Coze、Dify、LangGraph |
| 第三部分：高级知识扩展 | 理解智能体长期运行、协作和评估能力 | Memory、RAG、上下文工程、MCP、A2A、Agentic RL、评估体系 |
| 第四部分：综合案例进阶 | 将理论组合成真实应用案例 | 智能旅行助手、Deep Research、赛博小镇、多智能体协作 |
| 第五部分：毕业设计及未来展望 | 完成完整多智能体应用构建 | 系统设计、工程实现、能力评估、项目总结 |

## 当前笔记结构

```text
hello-agents-notes/
├─ 第一部分/
│  ├─ 第一章/
│  │  ├─ hello_agents_chapter1_mindmap.xmind
│  │  └─ 第一章-初识智能体-习题答案.md
│  ├─ 第二章/
│  │  └─ 第二章-智能体发展史-复习脑图.xmind
│  └─ 第三章/
├─ 第二部分/
│  └─ 第四章/
│     └─ 第四章-智能体经典范式构建-复习脑图.xmind
└─ README.md
```

## 已整理内容

| 章节 | 主题 | 当前材料 | 状态 |
| --- | --- | --- | --- |
| 第一章 | 初识智能体 | 复习脑图、习题答案 | 已整理 |
| 第二章 | 智能体发展史 | 复习脑图 | 已整理 |
| 第三章 | 大语言模型基础 | 待补充 | 待整理 |
| 第四章 | 智能体经典范式构建 | 复习脑图 | 已整理 |

## 推荐整理规范

为了让后续内容更容易维护，建议每一章按统一结构归档：

```text
第X章/
├─ 第X章-章节摘要.md
├─ 第X章-复习脑图.xmind
├─ 第X章-习题答案.md
└─ 第X章-实践记录.md
```

每章 Markdown 笔记可采用以下小节：

```markdown
# 第X章 标题

## 一句话总结

## 核心概念

## 知识框架

## 关键方法或范式

## 实践记录

## 易错点与思考

## 习题答案

## 延伸阅读
```

## 学习路线建议

1. 先读原教程正文，建立章节全局理解。
2. 再查看对应 XMind 脑图，快速复盘知识结构。
3. 补充 Markdown 摘要，把概念、公式、流程和案例写成自己的表达。
4. 对实践章节保留运行环境、关键代码、报错记录和解决方法。
5. 每完成一个部分后，增加一次阶段总结，沉淀可复用的方法论。

## 参考链接

- 在线阅读：[Hello-Agents 文档站](https://datawhalechina.github.io/hello-agents/#/)
- GitHub 仓库：[datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents)
- PDF 发布页：[Hello-Agents Releases](https://github.com/datawhalechina/hello-agents/releases/latest/)

## 备注

本仓库内容仅作为个人学习、复习和总结使用。原教程版权、许可协议和贡献说明请以 Hello-Agents 官方仓库为准。
