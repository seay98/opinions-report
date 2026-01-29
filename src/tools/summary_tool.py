"""汇总工具（模拟实现）"""

from typing import List


def summarize_info(extracted_info: List[dict]) -> dict:
    """
    汇总抽取的信息（模拟实现，返回固定数据）

    Args:
        extracted_info: 抽取的信息列表

    Returns:
        汇总结果
    """
    # 模拟汇总结果
    return {
        "overview": "该事件在近期引发广泛关注，社交媒体讨论热度持续升高，舆论场呈现多元化态势。",
        "sentiment_distribution": {
            "positive": 0.4,
            "neutral": 0.35,
            "negative": 0.25
        },
        "key_themes": [
            {
                "theme": "社会影响",
                "description": "事件对行业和社会产生深远影响，引发专家学者广泛讨论"
            },
            {
                "theme": "舆论分化",
                "description": "公众意见存在分歧，支持与反对声音并存"
            },
            {
                "theme": "政策预期",
                "description": "业内预测可能有相关政策出台，需持续关注"
            }
        ],
        "hot_entities": ["专家", "官方", "政策", "微博", "大V"],
        "trend": "上升",
        "risk_level": "中等",
        "recommendation": "建议持续关注舆情走向，做好应对预案，适时发布官方信息引导舆论"
    }
