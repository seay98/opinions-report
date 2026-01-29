"""汇总节点"""

from src.workflow.state import WorkflowState
from src.tools.summary_tool import summarize_info


def summary_node(state: WorkflowState) -> dict:
    """
    汇总节点：汇总抽取的信息

    Args:
        state: 当前工作流状态

    Returns:
        更新后的状态字典
    """
    try:
        extracted_info = state.get("extracted_info", [])

        if not extracted_info:
            return {
                "error": "没有抽取信息可供汇总",
                "current_step": "error"
            }

        print(f"[汇总节点] 正在汇总 {len(extracted_info)} 条抽取信息")

        summary = summarize_info(extracted_info)

        print("[汇总节点] 汇总完成")

        return {
            "summary": summary,
            "current_step": "summary_completed"
        }
    except Exception as e:
        return {
            "error": f"汇总失败: {str(e)}",
            "current_step": "error"
        }
