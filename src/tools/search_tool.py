"""搜索工具 - 基于 Tavily 的舆情搜索"""

from langchain_tavily import TavilySearch
from config.settings import TAVILY_API_KEY


def get_search_tool() -> TavilySearch:
    """
    获取配置好的 Tavily 搜索工具实例

    Returns:
        TavilySearch 工具实例，可直接传给 create_react_agent
    """
    return TavilySearch(
        max_results=5,
        api_key=TAVILY_API_KEY,
    )
