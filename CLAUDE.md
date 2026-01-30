# CLAUDE.md

## Project Overview

This is a **public opinion/sentiment report generation workflow framework** (舆情报告生成工作流框架). It automates the process of searching for public opinion data, extracting key information, summarizing findings, and generating professional sentiment analysis reports using a local LLM.

**Primary language:** Chinese (comments, prompts, output, and documentation are in Chinese)

**Current stage:** Prototype/framework. All tool implementations return mock data and are designed to be replaced with real integrations.

## Tech Stack

| Component | Technology |
|-----------|-----------|
| Language | Python 3.x |
| Workflow orchestration | LangGraph (>=0.2.0) |
| LLM framework | LangChain (>=0.3.0) |
| LLM integration | langchain-ollama (>=0.2.0) |
| LLM model | Qwen3:32b via Ollama (localhost:11434) |
| Data validation | Pydantic (>=2.0.0) |

## Project Structure

```
opinions-report/
├── CLAUDE.md                        # This file
├── requirements.txt                 # Python dependencies (4 packages)
├── step1.md                         # Project spec and requirements (Chinese)
├── .gitignore                       # Ignores .vscode
├── config/
│   └── settings.py                  # Ollama URL, model name, LLM parameters
└── src/
    ├── __init__.py
    ├── main.py                      # Entry point: generate_opinion_report(query)
    ├── models/
    │   ├── __init__.py
    │   └── llm.py                   # ChatOllama factory (get_llm())
    ├── nodes/                       # LangGraph workflow nodes
    │   ├── __init__.py
    │   ├── search.py                # search_node — calls search tool
    │   ├── extraction.py            # extraction_node — calls extraction tool
    │   ├── summary.py               # summary_node — calls summary tool
    │   └── generation.py            # generation_node — calls LLM with prompt
    ├── tools/                       # Tool implementations (currently mock)
    │   ├── __init__.py
    │   ├── search_tool.py           # search_opinions() — returns 4 mock articles
    │   ├── extraction_tool.py       # extract_info() — returns mock key points
    │   └── summary_tool.py          # summarize_info() — returns mock summary
    └── workflow/
        ├── __init__.py
        ├── state.py                 # WorkflowState TypedDict definition
        └── graph.py                 # LangGraph StateGraph with conditional edges
```

## Architecture

### Workflow Pipeline

```
START → Search → Extraction → Summary → Generation → END
           ↘         ↘           ↘
            └─────────┴───────────┴──→ END (early termination on error)
```

Each node is connected via **conditional edges** — if any node sets `error` in the state, the workflow terminates early via the `should_continue()` routing function in `src/workflow/graph.py`.

### State Management

The workflow state (`WorkflowState` in `src/workflow/state.py`) is a `TypedDict` with these fields:

- `query` (str) — input search topic
- `search_results` (Optional[List[dict]]) — raw search results
- `extracted_info` (Optional[List[dict]]) — extracted key points, entities, sentiment
- `summary` (Optional[dict]) — aggregated summary with sentiment distribution, themes, risk level
- `report` (Optional[str]) — final generated markdown report
- `error` (Optional[str]) — error message (triggers early termination)
- `current_step` (str) — tracks which step completed last

### Layer Separation

- **nodes/** — Orchestration layer. Each node reads from state, calls its corresponding tool, writes results back to state. Handles errors with try-except.
- **tools/** — Implementation layer. Pure functions that do the actual work. Currently return mock data. Replace these with real implementations.
- **models/** — LLM configuration. Single factory function `get_llm()` returns a configured `ChatOllama` instance.
- **workflow/** — Graph definition and state schema. Defines the DAG structure and routing logic.

## Development Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Ensure Ollama is running with qwen3:32b model
ollama serve
ollama pull qwen3:32b

# Run the application
python -m src.main
```

## Configuration

All LLM settings are in `config/settings.py`:

- `OLLAMA_BASE_URL` — Ollama server URL (default: `http://localhost:11434`)
- `OLLAMA_MODEL` — Model name (default: `qwen3:32b`)
- `LLM_TEMPERATURE` — Sampling temperature (default: `0.7`)
- `LLM_TOP_P` — Top-p sampling (default: `0.9`)

## Code Conventions

### Node Pattern

Every node in `src/nodes/` follows this structure:

```python
def node_name(state: WorkflowState) -> dict:
    try:
        # 1. Read inputs from state
        # 2. Call corresponding tool function
        # 3. Print progress with [节点名] prefix
        # 4. Return dict with updated fields and current_step
        return {"field": value, "current_step": "step_completed"}
    except Exception as e:
        return {"error": f"失败描述: {str(e)}", "current_step": "error"}
```

### Tool Pattern

Tools in `src/tools/` are pure functions:

```python
def tool_function(input_data) -> return_type:
    """Docstring in Chinese context, English format"""
    # Currently returns mock data
    return mock_result
```

### General Conventions

- **Docstrings:** Module-level docstrings in Chinese. Function docstrings use Google-style with Chinese descriptions.
- **Error messages:** In Chinese (e.g., `"搜索失败: ..."`)
- **Console output:** Uses Chinese with bracketed node labels (e.g., `[搜索节点]`, `[抽取节点]`)
- **Type hints:** Used throughout with `typing` module (TypedDict, Optional, List)
- **Imports:** Absolute imports from `src.` and `config.` packages
- **Path setup:** `src/main.py` adds project root to `sys.path` for import resolution

## Testing

No testing infrastructure exists yet. No test framework is configured in requirements.txt. There are no test files.

## Key Files for Common Tasks

| Task | File(s) |
|------|---------|
| Change LLM model or parameters | `config/settings.py` |
| Modify the report generation prompt | `src/nodes/generation.py` (REPORT_PROMPT) |
| Replace mock search with real API | `src/tools/search_tool.py` |
| Replace mock extraction with real logic | `src/tools/extraction_tool.py` |
| Replace mock summary with real logic | `src/tools/summary_tool.py` |
| Add a new workflow step | `src/workflow/graph.py` + new node in `src/nodes/` |
| Change workflow state schema | `src/workflow/state.py` |
| Run the application | `src/main.py` |
