# Multi-LLM Agent 🚀

A production-ready AI agent platform powered by multiple Large Language Models (LLMs) and a modern React frontend.

## Features

* Multi-LLM support

  * Groq
  * Gemini
  * OpenAI
  * DeepSeek

* Intelligent model routing

* Response aggregation and synthesis

* Conversation memory using SQLite

* Tool integrations

  * Web Search
  * Calculator
  * Weather

* FastAPI backend

* React "Jarvis" frontend

* REST APIs with Swagger documentation

## Tech Stack

### Backend

* Python
* FastAPI
* SQLAlchemy
* SQLite

### Frontend

* React
* Vite
* Axios

### AI Providers

* Groq
* Gemini
* OpenAI
* DeepSeek

## Architecture

User → React UI → FastAPI → Agent Router → LLM Providers → Response Synthesis → Memory & Tools

## API Endpoints

* `/`
* `/health`
* `/ask`
* `/smart`
* `/agent`
* `/memory`
* `/search`

## Installation

```bash
git clone https://github.com/Prince11-dev/multi-llm-agent.git
cd multi-llm-agent
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

Frontend:

```bash
cd frontend
npm install
npm run dev
```

## Future Roadmap

* PDF Chat (RAG)
* Streaming Responses
* Authentication
* Voice Assistant
* Docker Deployment
* Cloud Deployment
