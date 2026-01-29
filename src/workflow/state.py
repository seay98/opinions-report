"""工作流状态定义"""

from typing import TypedDict, Optional, List


class WorkflowState(TypedDict):
    """舆情报告工作流状态"""

    # 输入
    query: str  # 用户查询主题

    # 搜索阶段
    search_results: Optional[List[dict]]  # 搜索到的舆情数据

    # 抽取阶段
    extracted_info: Optional[List[dict]]  # 抽取的关键信息

    # 汇总阶段
    summary: Optional[dict]  # 汇总结果

    # 生成阶段
    report: Optional[str]  # 最终生成的报告

    # 状态控制
    error: Optional[str]  # 错误信息
    current_step: str  # 当前步骤
