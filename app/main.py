from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.services.aggregator import aggregate
from app.services.synthesizer import synthesize

from app.services.router import route_question
from app.services.router_executor import execute_route

from app.services.intelligent_router import intelligent_route
from app.services.intelligent_executor import intelligent_execute

from app.tools.web_search import search_web

from app.memory.database import init_db
from app.memory.store import save_conversation
from app.memory.retrieve import get_history

from app.middleware.logging_middleware import (
    LoggingMiddleware,
)
from app.middleware.exception_handler import (
    global_exception_handler,
)


app = FastAPI(
    title="Multi LLM Agent",
    version="1.0.0",
    description="Multi-LLM Agent Platform powered by Groq, Gemini, DeepSeek and OpenAI",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(
    LoggingMiddleware
)

app.add_exception_handler(
    Exception,
    global_exception_handler
)

init_db()


# ------------------------------------------------------
# ROOT
# ------------------------------------------------------
@app.get("/")
async def home():
    return {
        "message": "Multi LLM Agent Running",
        "version": "1.0.0",
    }


# ------------------------------------------------------
# HEALTH
# ------------------------------------------------------
@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "version": "1.0.0",
        "providers": [
            "groq",
            "gemini",
            "deepseek",
            "openai",
        ],
        "features": [
            "memory",
            "routing",
            "aggregation",
            "tools",
        ],
    }


# ------------------------------------------------------
# ASK (ALL MODELS)
# ------------------------------------------------------
@app.get("/ask")
async def ask(question: str):

    responses = await aggregate(
        question
    )

    final_answer = await synthesize(
        question,
        responses,
    )

    return {
        "question": question,
        "responses": responses,
        "final": final_answer,
    }


# ------------------------------------------------------
# SMART ROUTER
# ------------------------------------------------------
@app.get("/smart")
async def smart(question: str):

    selected_model = await route_question(
        question
    )

    answer = await execute_route(
        selected_model,
        question,
    )

    return {
        "question": question,
        "selected_model": selected_model,
        "answer": answer,
    }


# ------------------------------------------------------
# AGENT WITH MEMORY
# ------------------------------------------------------
@app.get("/agent")
async def agent(
    question: str,
    session_id: str = "default",
):

    history = get_history(
        session_id
    )

    context = ""

    for item in reversed(history):

        context += f"""
User:
{item['question']}

Assistant:
{item['answer']}
"""

    route = await intelligent_route(
        question
    )

    answer = await intelligent_execute(
        route,
        question,
        context,
    )

    save_conversation(
        session_id,
        question,
        answer,
    )

    return {
        "version": "1.0.0",
        "session_id": session_id,
        "question": question,
        "route": route,
        "history_count": len(history),
        "answer": answer,
    }


# ------------------------------------------------------
# MEMORY
# ------------------------------------------------------
@app.get("/memory")
async def memory(
    session_id: str,
):
    history = get_history(
        session_id
    )

    return {
        "session_id": session_id,
        "count": len(history),
        "history": history,
    }


# ------------------------------------------------------
# WEB SEARCH
# ------------------------------------------------------
@app.get("/search")
async def search(
    question: str,
):

    results = await search_web(
        question
    )

    return {
        "question": question,
        "results": results,
    }