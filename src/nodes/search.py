"""搜索节点 - 基于 ReACT Agent 的智能搜索"""

import json
from typing import List

from langgraph.prebuilt import create_react_agent
from langchain_core.messages import ToolMessage

from src.workflow.state import WorkflowState
from src.models.llm import get_llm
from src.tools.search_tool import search_tavily
from config.settings import MAX_SEARCH_COUNT


SEARCH_AGENT_PROMPT = f"""你是一名专业的舆情搜索分析师。你的任务是围绕给定的主题，进行全面的舆情信息搜索。

## 工作流程

1. **分析主题**：理解用户给出的主题，拆解为多个搜索角度（如：正面报道、负面报道、政策动态、行业影响、公众反应等）
2. **生成搜索词**：为每个角度生成精准的中文搜索关键词
3. **执行搜索**：调用搜索工具进行搜索
4. **评估结果**：评估搜索结果的覆盖度和充分性
5. **迭代搜索**：如果信息覆盖不全面，换角度生成新的搜索关键词再次搜索

## 约束条件

- 你最多可以调用搜索工具 {MAX_SEARCH_COUNT} 次，请合理规划搜索策略
- 每次搜索使用不同的关键词和角度，避免重复搜索
- 搜索关键词应使用中文
- 完成所有搜索后，不需要总结，直接结束即可
"""


def _extract_search_results(messages) -> List[dict]:
    """
    从 agent 消息历史中提取所有 Tavily 搜索结果

    Args:
        messages: agent 返回的消息列表

    Returns:
        去重后的搜索结果列表
    """
    results = []
    seen_urls = set()

    for msg in messages:
        if not isinstance(msg, ToolMessage):
            continue

        try:
            content = msg.content
            if isinstance(content, str):
                content = json.loads(content)

            if isinstance(content, list):
                items = content
            elif isinstance(content, dict) and "results" in content:
                items = content["results"]
            else:
                continue

            for item in items:
                if not isinstance(item, dict):
                    continue
                url = item.get("url", "")
                if url in seen_urls:
                    continue
                seen_urls.add(url)
                results.append({
                    "title": item.get("title", ""),
                    "url": url,
                    "content": item.get("content", ""),
                    "score": item.get("score", 0),
                })
        except (json.JSONDecodeError, TypeError, KeyError):
            continue

    return results


def search_node(state: WorkflowState) -> dict:
    """
    搜索节点：使用 ReACT Agent 进行智能舆情搜索

    Agent 会自动分析主题、生成多角度搜索词、评估结果充分性并迭代搜索。

    Args:
        state: 当前工作流状态

    Returns:
        更新后的状态字典
    """
    try:
        query = state["query"]
        print(f"[搜索节点] 正在启动搜索 Agent，主题: {query}")

        llm = get_llm()
        search_tool = search_tavily()

        agent = create_react_agent(
            model=llm,
            tools=[search_tool],
            prompt=SEARCH_AGENT_PROMPT,
        )

        result = agent.invoke(
            {"messages": [{"role": "user", "content": f"请搜索以下主题的舆情信息：{query}"}]},
            config={"recursion_limit": MAX_SEARCH_COUNT * 2 + 2},
        )

        results = _extract_search_results(result["messages"])

        print(f"[搜索节点] 搜索完成，共获取 {len(results)} 条结果")

        return {
            "search_results": results,
            "current_step": "search_completed"
        }
    except Exception as e:
        return {
            "error": f"搜索失败: {str(e)}",
            "current_step": "error"
        }
