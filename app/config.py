from dotenv import load_dotenv
import os

load_dotenv()


class Settings:

    APP_NAME = os.getenv(
        "APP_NAME",
        "Multi LLM Agent"
    )

    APP_VERSION = os.getenv(
        "APP_VERSION",
        "1.0.0"
    )

    DEBUG = os.getenv(
        "DEBUG",
        "True"
    ).lower() == "true"

    GEMINI_API_KEY = os.getenv(
        "GEMINI_API_KEY"
    )

    GROQ_API_KEY = os.getenv(
        "GROQ_API_KEY"
    )

    DEEPSEEK_API_KEY = os.getenv(
        "DEEPSEEK_API_KEY"
    )

    OPENAI_API_KEY = os.getenv(
        "OPENAI_API_KEY"
    )

    DATABASE_URL = os.getenv(
        "DATABASE_URL",
        "sqlite:///memory.db"
    )


settings = Settings()