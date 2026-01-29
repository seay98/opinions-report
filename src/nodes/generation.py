"""生成节点"""

import json
from src.workflow.state import WorkflowState
from src.models.llm import get_llm


REPORT_PROMPT = """你是一位专业的舆情分析师。请根据以下汇总信息，生成一份结构清晰、内容专业的舆情分析报告。

## 查询主题
{query}

## 汇总信息
{summary}

## 报告要求
1. 报告应包含以下部分：概述、舆情态势、主要观点、风险评估、建议措施
2. 语言要专业、客观、简洁
3. 适当使用数据支撑观点
4. 报告长度适中，重点突出

请直接输出报告内容，使用 Markdown 格式："""


def generation_node(state: WorkflowState) -> dict:
    """
    生成节点：使用 LLM 生成舆情报告

    Args:
        state: 当前工作流状态

    Returns:
        更新后的状态字典
    """
    try:
        summary = state.get("summary")
        query = state.get("query", "")

        if not summary:
            return {
                "error": "没有汇总信息可供生成报告",
                "current_step": "error"
            }

        print("[生成节点] 正在使用 LLM 生成报告...")

        llm = get_llm()

        prompt = REPORT_PROMPT.format(
            query=query,
            summary=json.dumps(summary, ensure_ascii=False, indent=2)
        )

        response = llm.invoke(prompt)
        report = response.content

        print("[生成节点] 报告生成完成")

        return {
            "report": report,
            "current_step": "generation_completed"
        }
    except Exception as e:
        return {
            "error": f"报告生成失败: {str(e)}",
            "current_step": "error"
        }
