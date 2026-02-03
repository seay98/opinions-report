"""Ollama 配置"""

import os

# Ollama 服务配置
OLLAMA_BASE_URL = "http://localhost:11434"
OLLAMA_MODEL = "qwen3:32b"

# LLM 参数
LLM_TEMPERATURE = 0.4
LLM_TOP_P = 0.9

# Tavily 搜索配置
TAVILY_API_KEY = os.environ.get("TAVILY_API_KEY", "")
MAX_SEARCH_COUNT = 3
