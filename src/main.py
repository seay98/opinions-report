"""舆情报告生成工作流入口"""

import sys
from pathlib import Path

# 添加项目根目录到 Python 路径
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from src.workflow.graph import create_workflow
from src.workflow.state import WorkflowState


def generate_opinion_report(query: str) -> str:
    """
    生成舆情报告

    Args:
        query: 查询主题

    Returns:
        生成的舆情报告
    """
    print(f"\n{'='*60}")
    print(f"舆情报告生成工作流")
    print(f"查询主题: {query}")
    print(f"{'='*60}\n")

    # 创建工作流
    workflow = create_workflow()

    # 初始化状态
    initial_state: WorkflowState = {
        "query": query,
        "search_results": None,
        "extracted_info": None,
        "summary": None,
        "report": None,
        "error": None,
        "current_step": "start"
    }

    # 执行工作流
    final_state = workflow.invoke(initial_state)

    # 检查结果
    if final_state.get("error"):
        print(f"\n[错误] {final_state['error']}")
        return f"报告生成失败: {final_state['error']}"

    report = final_state.get("report", "")

    print(f"\n{'='*60}")
    print("报告生成完成")
    print(f"{'='*60}\n")

    return report


def main():
    """主函数"""
    # 示例查询
    query = "人工智能技术发展"

    # 生成报告
    report = generate_opinion_report(query)

    # 输出报告
    print("\n" + "="*60)
    print("生成的舆情报告")
    print("="*60 + "\n")
    print(report)


if __name__ == "__main__":
    main()
