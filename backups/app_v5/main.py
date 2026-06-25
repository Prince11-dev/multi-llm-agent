from fastapi import FastAPI

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


app = FastAPI(
    title="Multi LLM Agent",
    version="5.0"
)

init_db()


@app.get("/")
async def home():

    return {
        "message": "AI Agent Running",
        "version": "5.0"
    }


@app.get("/health")
async def health():

    return {
        "status": "healthy",
        "version": "5.0",
        "providers": [
            "gemini",
            "groq",
            "deepseek"
        ],
        "features": [
            "memory",
            "routing",
            "aggregation",
            "web_search"
        ]
    }


@app.get("/ask")
async def ask(question: str):

    responses = await aggregate(question)

    final_answer = await synthesize(
        question,
        responses
    )

    return {
        "question": question,
        "timing": {
            "gemini": responses["gemini"]["time"],
            "groq": responses["groq"]["time"],
            "deepseek": responses["deepseek"]["time"]
        },
        "responses": responses,
        "final": final_answer
    }


@app.get("/smart")
async def smart(question: str):

    selected_model = await route_question(
        question
    )

    answer = await execute_route(
        selected_model,
        question
    )

    return {
        "question": question,
        "selected_model": selected_model,
        "answer": answer
    }


@app.get("/search")
async def search(question: str):

    results = await search_web(
        question
    )

    return {
        "question": question,
        "results": results
    }


@app.get("/agent")
async def agent(
    question: str,
    session_id: str = "default"
):

    history = get_history(
        session_id
    )

    context = ""

    for q in reversed(history):

        context += f"""
User: {q}
"""

    route = await intelligent_route(
        question
    )

    answer = await intelligent_execute(
        route,
        question,
        context
    )

    save_conversation(
        session_id,
        question,
        answer
    )

    return {
        "version": "5.0",
        "session_id": session_id,
        "question": question,
        "route": route,
        "history_count": len(history),
        "answer": answer
    }


@app.get("/memory")
async def memory(
    session_id: str
):

    history = get_history(
        session_id
    )

    formatted_history = []

    for question in history:

        formatted_history.append(
            {
                "question": question
            }
        )

    return {
        "version": "5.0",
        "session_id": session_id,
        "count": len(formatted_history),
        "history": formatted_history
    }