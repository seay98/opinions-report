"""抽取节点"""

from src.workflow.state import WorkflowState
from src.tools.extraction_tool import extract_info


def extraction_node(state: WorkflowState) -> dict:
    """
    抽取节点：从搜索结果中抽取关键信息

    Args:
        state: 当前工作流状态

    Returns:
        更新后的状态字典
    """
    try:
        search_results = state.get("search_results", [])

        if not search_results:
            return {
                "error": "没有搜索结果可供抽取",
                "current_step": "error"
            }

        print(f"[抽取节点] 正在抽取 {len(search_results)} 条结果的信息")

        extracted = extract_info(search_results)

        print(f"[抽取节点] 抽取完成，得到 {len(extracted)} 条信息")

        return {
            "extracted_info": extracted,
            "current_step": "extraction_completed"
        }
    except Exception as e:
        return {
            "error": f"抽取失败: {str(e)}",
            "current_step": "error"
        }
