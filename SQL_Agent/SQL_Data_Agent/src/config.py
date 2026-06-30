import os
from dotenv import load_dotenv

load_dotenv()

MYSQL_CONFIG = {
    "host": os.getenv("MYSQL_HOST", "localhost"),
    "port": int(os.getenv("MYSQL_PORT", 3306)),
    "database": os.getenv("MYSQL_DATABASE", "retail_agent_assignment"),
    "user": os.getenv("MYSQL_USER", "root"),
    "password": os.getenv("MYSQL_PASSWORD", "")
}

LLM_CONFIG = {
    "url": os.getenv("TIGER_AI_GATEWAY_URL"),
    "api_key": os.getenv("TIGER_AI_GATEWAY_API_KEY"),
    "model": os.getenv("TIGER_AI_GATEWAY_MODEL")
}
