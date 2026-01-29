"""Ollama LLM 配置"""

from langchain_ollama import ChatOllama
from config.settings import OLLAMA_BASE_URL, OLLAMA_MODEL, LLM_TEMPERATURE


def get_llm() -> ChatOllama:
    """获取配置好的 Ollama LLM 实例"""
    return ChatOllama(
        base_url=OLLAMA_BASE_URL,
        model=OLLAMA_MODEL,
        temperature=LLM_TEMPERATURE,
    )
