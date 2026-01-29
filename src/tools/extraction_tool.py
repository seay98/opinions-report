"""抽取工具（模拟实现）"""

from typing import List


def extract_info(search_results: List[dict]) -> List[dict]:
    """
    从搜索结果中抽取关键信息（模拟实现，返回固定数据）

    Args:
        search_results: 搜索结果列表

    Returns:
        抽取的关键信息列表
    """
    # 模拟抽取的关键信息
    return [
        {
            "source_id": "1",
            "key_points": [
                "事件引发社会广泛关注",
                "专家认为将对行业产生深远影响",
                "社交媒体讨论量超过100万次"
            ],
            "entities": ["专家", "行业", "社交媒体"],
            "sentiment_score": 0.5,
            "importance": "高"
        },
        {
            "source_id": "2",
            "key_points": [
                "网友意见分化",
                "支持方与反对方观点对立",
                "官方暂未回应"
            ],
            "entities": ["网友", "官方"],
            "sentiment_score": 0.3,
            "importance": "高"
        },
        {
            "source_id": "3",
            "key_points": [
                "与当前经济形势密切相关",
                "业内预测将有更多政策出台",
                "需关注后续发展"
            ],
            "entities": ["经济形势", "政策", "业内人士"],
            "sentiment_score": 0.7,
            "importance": "中"
        },
        {
            "source_id": "4",
            "key_points": [
                "登上微博热搜榜首",
                "阅读量突破5亿",
                "大V参与讨论"
            ],
            "entities": ["微博", "热搜", "大V"],
            "sentiment_score": 0.6,
            "importance": "中"
        }
    ]
