# 舆情报告工作流框架 - Step 1

## 功能

生成舆情报告

## 基本流程

搜索 -> 抽取 -> 汇总 -> 生成

## 要求

- 生成流程框架
- 调用的工具先不实现具体细节，先用固定返回值代替
- 使用python + langchain + ollama实现

## 项目结构

```
opinions-report/
├── requirements.txt              # langchain, langgraph, langchain-ollama, pydantic
├── config/
│   └── settings.py              # Ollama 配置 (qwen3:32b)
├── src/
│   ├── __init__.py
│   ├── main.py                  # 入口文件，提供 generate_opinion_report(query)
│   ├── workflow/
│   │   ├── __init__.py
│   │   ├── graph.py             # LangGraph 工作流定义（含条件边）
│   │   └── state.py             # WorkflowState TypedDict
│   ├── nodes/
│   │   ├── __init__.py
│   │   ├── search.py            # 搜索节点
│   │   ├── extraction.py        # 抽取节点
│   │   ├── summary.py           # 汇总节点
│   │   └── generation.py        # LLM 生成节点
│   ├── tools/
│   │   ├── __init__.py
│   │   ├── search_tool.py       # 模拟搜索（返回4条舆情数据）
│   │   ├── extraction_tool.py   # 模拟抽取（返回关键信息）
│   │   └── summary_tool.py      # 模拟汇总（返回汇总结果）
│   └── models/
│       ├── __init__.py
│       └── llm.py               # ChatOllama 配置
└── step1.md                     # 本文档
```

## 使用方法

```bash
# 1. 安装依赖
pip install -r requirements.txt

# 2. 确保 Ollama 服务运行
ollama serve

# 3. 运行
python -m src.main
```

## 工作流

```
START → Search → Extraction → Summary → Generation → END
              ↘      ↘           ↘
               └──────┴───────────┴──→ END (错误时提前终止)
```

## 技术选型

| 组件 | 选择 | 说明 |
|------|------|------|
| 工作流框架 | LangGraph | 支持状态管理、条件分支 |
| LLM 集成 | langchain-ollama | 官方推荐方式 |
| LLM 模型 | qwen3:32b | 中文能力强 |
| 状态类型 | TypedDict | 类型安全 |
