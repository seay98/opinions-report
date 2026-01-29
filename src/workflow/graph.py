"""LangGraph 工作流定义"""

from langgraph.graph import StateGraph, END

from src.workflow.state import WorkflowState
from src.nodes.search import search_node
from src.nodes.extraction import extraction_node
from src.nodes.summary import summary_node
from src.nodes.generation import generation_node


def should_continue(state: WorkflowState) -> str:
    """
    判断是否继续执行工作流

    Args:
        state: 当前状态

    Returns:
        下一个节点名称或 END
    """
    if state.get("error"):
        return "end"
    return "continue"


def create_workflow():
    """
    创建舆情报告生成工作流

    Returns:
        编译后的工作流图
    """
    # 创建状态图
    workflow = StateGraph(WorkflowState)

    # 添加节点
    workflow.add_node("search", search_node)
    workflow.add_node("extraction", extraction_node)
    workflow.add_node("summary", summary_node)
    workflow.add_node("generation", generation_node)

    # 设置入口点
    workflow.set_entry_point("search")

    # 添加条件边：搜索后判断
    workflow.add_conditional_edges(
        "search",
        should_continue,
        {
            "continue": "extraction",
            "end": END
        }
    )

    # 添加条件边：抽取后判断
    workflow.add_conditional_edges(
        "extraction",
        should_continue,
        {
            "continue": "summary",
            "end": END
        }
    )

    # 添加条件边：汇总后判断
    workflow.add_conditional_edges(
        "summary",
        should_continue,
        {
            "continue": "generation",
            "end": END
        }
    )

    # 生成后结束
    workflow.add_edge("generation", END)

    # 编译工作流
    return workflow.compile()
