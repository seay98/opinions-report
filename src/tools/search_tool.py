"""搜索工具（模拟实现）"""

from typing import List


def search_opinions(query: str) -> List[dict]:
    """
    搜索舆情数据（模拟实现，返回固定数据）

    Args:
        query: 搜索查询词

    Returns:
        舆情数据列表
    """
    # 模拟返回的舆情数据
    return [
        {
            "id": "1",
            "title": f"关于{query}的最新报道",
            "source": "新浪新闻",
            "date": "2025-01-28",
            "content": f"近日，{query}引发社会广泛关注。多位专家表示，这一事件将对行业发展产生深远影响。据统计，相关话题在社交媒体上的讨论量已超过100万次。",
            "sentiment": "中性",
            "url": "https://news.example.com/1"
        },
        {
            "id": "2",
            "title": f"{query}事件持续发酵",
            "source": "澎湃新闻",
            "date": "2025-01-27",
            "content": f"针对{query}，网友们发表了不同看法。支持方认为这是积极的信号，反对方则表达了担忧。官方尚未对此作出正式回应。",
            "sentiment": "争议",
            "url": "https://news.example.com/2"
        },
        {
            "id": "3",
            "title": f"深度分析：{query}背后的原因",
            "source": "财经网",
            "date": "2025-01-26",
            "content": f"本文深入分析了{query}产生的背景和原因。从宏观角度来看，这与当前的经济形势密切相关。业内人士预测，后续可能会有更多政策出台。",
            "sentiment": "正面",
            "url": "https://news.example.com/3"
        },
        {
            "id": "4",
            "title": f"网友热议{query}",
            "source": "微博热搜",
            "date": "2025-01-25",
            "content": f"#{query}#话题登上微博热搜榜首，阅读量突破5亿。众多大V纷纷发表评论，形成了多元化的讨论氛围。部分网友表示期待看到更多进展。",
            "sentiment": "正面",
            "url": "https://weibo.example.com/topic"
        }
    ]
