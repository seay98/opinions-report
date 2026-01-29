"""搜索节点"""

from src.workflow.state import WorkflowState
from src.tools.search_tool import search_opinions


def search_node(state: WorkflowState) -> dict:
    """
    搜索节点：调用搜索工具获取舆情数据

    Args:
        state: 当前工作流状态

    Returns:
        更新后的状态字典
    """
    try:
        query = state["query"]
        print(f"[搜索节点] 正在搜索: {query}")

        results = search_opinions(query)

        print(f"[搜索节点] 找到 {len(results)} 条结果")

        return {
            "search_results": results,
            "current_step": "search_completed"
        }
    except Exception as e:
        return {
            "error": f"搜索失败: {str(e)}",
            "current_step": "error"
        }
