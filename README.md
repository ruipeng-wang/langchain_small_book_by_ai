# LangChain 实战教程：从入门到企业级应用

> 🤖 一套面向初中级开发者的 LangChain/LangGraph/Deep Agents 系统化教程

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10+-green.svg)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/LangChain-latest-00A1F0.svg)](https://python.langchain.com/)
[![LangGraph](https://img.shields.io/badge/LangGraph-latest-FF6B6B.svg)](https://langchain-ai.github.io/langgraph/)

---

## 📖 项目简介

随着大语言模型（LLM）技术的爆发式发展，如何高效地将AI能力集成到实际应用中成为了开发者面临的重大挑战。LangChain 作为当前最流行的 AI 应用开发框架，提供了一套标准化的抽象接口，帮助开发者屏蔽底层模型差异，专注于业务逻辑的实现。

**本教程旨在：**

- 🎯 **系统化讲解** LangChain 生态系统的核心组件与设计哲学
- 🔧 **从零到一** 构建企业级 AI 应用，涵盖 RAG、智能客服、多代理协作等实战场景
- 💡 **深入原理** 不仅教你"怎么用"，更教你"为什么这样设计"
- 🚀 **面向生产** 关注部署、监控、成本优化等企业级议题

> 本教程基于 LangChain 最新版构建，所有代码示例均经过验证，可直接运行。

---

## 🗺️ 教程结构

本教程共分为 **6 大部分、17 章**，按照"基础 → 进阶 → 实战 → 职业"的学习路径组织：

### 第 1 部分 | LangChain 基础与入门

> 建立对 AI 应用开发的基本认知

| 章节 | 标题 | 核心内容 |
|------|------|----------|
| [第 1 章](./第1部分%20LangChain基础与入门/第1章：人工智能应用开发新范式/) | 人工智能应用开发新范式 | 编程范式转变、LangChain 生态全景、环境搭建 |
| [第 2 章](./第1部分%20LangChain基础与入门/第2章：LangChain核心设计哲学/) | LangChain 核心设计哲学 | 模块化设计、链式思维、代理思维 |
| [第 3 章](./第1部分%20LangChain基础与入门/第3章：核心抽象与执行模型/) | 核心抽象与执行模型 | Runnable 抽象、LCEL 表达式语言、消息系统 |

### 第 2 部分 | 数据处理与知识管理

> 掌握向量数据库与 RAG 的数据处理流程

| 章节 | 标题 | 核心内容 |
|------|------|----------|
| [第 4 章](./第2部分%20数据处理与知识管理/第4章：文档加载与预处理系统/) | 文档加载与预处理系统 | 统一文档抽象、加载器、文档管道、分块策略 |
| [第 5 章](./第2部分%20数据处理与知识管理/第5章：向量存储与检索系统/) | 向量存储与检索系统 | 向量检索基础、Embedding 模型、相似度计算、性能优化 |

### 第 3 部分 | 核心工作流引擎

> 理解 LangChain 的核心执行机制

| 章节 | 标题 | 核心内容 |
|------|------|----------|
| [第 6 章](./第3部分%20核心工作流引擎/第6章：模型系统与集成策略/) | 模型系统与集成策略 | 模型抽象适配器、主流模型集成、流式输出 |
| [第 7 章](./第3部分%20核心工作流引擎/第7章：提示工程与模板系统/) | 提示工程与模板系统 | 动态模板引擎、高级提示技术、输出解析器 |
| [第 8 章](./第3部分%20核心工作流引擎/第8章：链式执行引擎/) | 链式执行引擎 | 链式执行基础、内置链类型、链的组合与扩展 |
| [第 9 章](./第3部分%20核心工作流引擎/第9章：代理系统与智能决策/) | 代理系统与智能决策 | 代理架构设计、代理类型与场景、工具系统设计 |
| [第 10 章](./第3部分%20核心工作流引擎/第10章：Deep%20Agents深度代理系统/) | Deep Agents 深度代理系统 | 中间件与状态管理、深度代理实战模式 |

### 第 4 部分 | LangGraph 高级工作流

> 掌握复杂业务工作流的编排能力

| 章节 | 标题 | 核心内容 |
|------|------|----------|
| [第 11 章](./第4部分%20LangGraph高级工作流/第11章：LangGraph图计算引擎/) | LangGraph 图计算引擎 | StateGraph 核心概念、节点与边条件、设计模式 |
| [第 12 章](./第4部分%20LangGraph高级工作流/第12章：复杂业务工作流编排/) | 复杂业务工作流编排 | 多步骤工作流、人工介入、状态持久化与恢复 |
| [第 13 章](./第4部分%20LangGraph高级工作流/第13章：多代理协作系统/) | 多代理协作系统 | Supervisor 架构、并行执行与任务分配、协调与冲突解决 |

### 第 5 部分 | 企业级实战应用

> 将理论知识应用于真实项目场景

| 章节 | 标题 | 核心内容 |
|------|------|----------|
| [第 13 章](./第5部分%20企业级实战应用/第13章：高级RAG系统架构/) | 高级 RAG 系统架构 | RAG 核心原理、高级检索策略、生产环境优化 |
| [第 14 章](./第5部分%20企业级实战应用/第14章：智能客服系统实战/) | 智能客服系统实战 | 客服系统架构、对话管理与状态追踪、实战案例 |
| [第 15 章](./第5部分%20企业级实战应用/第15章：生产环境部署运维/) | 生产环境部署运维 | 部署架构与服务编排、监控与可观测性、安全与成本控制 |

### 第 6 部分 | 职业发展与进阶

> 为 AI 工程师的职业发展提供指导

| 章节 | 标题 | 核心内容 |
|------|------|----------|
| [第 16 章](./第6部分%20职业发展与进阶/第16章：面试与求职指导/) | 面试与求职指导 | 企业级 AI 能力要求、面试技巧、职业发展路径 |
| [第 17 章](./第6部分%20职业发展与进阶/第17章：开源贡献与社区参与/) | 开源贡献与社区参与 | 开源贡献指南、技术社区资源、个人品牌建设 |

---

## 🚀 快速开始

### 环境要求

- **Python**: 3.10+
- **包管理**: pip / uv / poetry

### 安装依赖

```bash
# 安装核心依赖
pip install langchain langchain-core langchain-community langgraph

# 安装常用扩展包
pip install langchain-openai langchain-anthropic langchain-google-genai
pip install chromadb faiss-cpu  # 向量数据库
pip install tiktoken            # Token 计算
```

### 第一个 LangChain 应用

```python
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# 1. 初始化模型
llm = ChatOpenAI(model="gpt-4o", temperature=0.7)

# 2. 定义提示模板
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个专业的{role}，擅长{skill}。"),
    ("human", "请用通俗易懂的方式解释：{topic}")
])

# 3. 构建 LCEL 链
chain = prompt | llm | StrOutputParser()

# 4. 执行
result = chain.invoke({
    "role": "AI教育者",
    "skill": "用简单例子解释复杂概念",
    "topic": "什么是机器学习？"
})
print(result)
```

---

## 💡 教程特色

### 📐 文章结构

每篇文章遵循统一结构，确保学习效率：

```
概念讲解（文字 + 图示）
    ↓
核心要点（重点标记）
    ↓
简单示例（代码演示）
    ↓
进阶应用（可选内容）
    ↓
常见问题（FAQ）
    ↓
本节总结
```

### 🎯 学习原则

1. **代码占比不超过 30%**：聚焦原理理解，而非大量堆砌代码
2. **概念先行**：先理解"为什么"，再学习"怎么做"
3. **图示辅助**：用直观的架构图帮助理解复杂概念
4. **实战驱动**：每个核心概念都配有可运行的示例

---

## 📚 推荐阅读路径

### 新手入门路线

```
第 1 部分（基础概念）
    ↓
第 2 部分（数据处理）
    ↓
第 3 部分第 6-8 章（模型、提示、链）
```

### RAG 应用开发路线

```
第 1-2 部分（基础 + 数据）
    ↓
第 3 部分第 6-8 章（核心组件）
    ↓
第 5 部分第 13 章（高级 RAG 实战）
```

### 企业级项目路线

```
完整学习第 1-4 部分
    ↓
第 5 部分（实战 + 部署 + 运维）
    ↓
第 6 部分（职业发展）
```

---

## 🛠️ 技术栈

本教程涉及的核心技术：

| 类别 | 技术 | 用途 |
|------|------|------|
| **框架** | LangChain | AI 应用开发基础框架 |
| **框架** | LangGraph | 复杂工作流编排 |
| **框架** | Deep Agents | 深度代理系统 |
| **模型** | OpenAI GPT | 主力 LLM |
| **模型** | Anthropic Claude | 备选 LLM |
| **存储** | Chroma / FAISS | 向量数据库 |
| **存储** | PostgreSQL pgvector | 生产级向量存储 |

---

## 🤝 参与贡献

本教程是开源项目，欢迎任何人参与贡献：

1. Fork 本仓库
2. 创建你的特性分支 (`git checkout -b feature/amazing-content`)
3. 提交你的更改 (`git commit -m 'feat: add amazing content'`)
4. 推送到分支 (`git push origin feature/amazing-content`)
5. 提交 Pull Request

### 贡献指南

- 保持内容简洁清晰，代码占比不超过 30%
- 遵循既定的文章结构
- 使用 Python 3.10+ 语法
- 所有代码示例需经过验证

---

## 📄 许可证

本项目采用 MIT 许可证。

---

## ⭐ 支持项目

如果你觉得这个教程对你有帮助，请给个 ⭐ Star，这是对我最大的鼓励！

---

## 📬 联系方式

- **Issues**: [提交问题](https://github.com/ruipeng-wang/langchain_small_book_by_ai/issues)
- **Discussions**: [参与讨论](https://github.com/ruipeng-wang/langchain_small_book_by_ai/discussions)

---

> 💬 *"AI 不会取代开发者，但会用 AI 的开发者会取代不会用的。"*

**Happy Learning! 🎉**