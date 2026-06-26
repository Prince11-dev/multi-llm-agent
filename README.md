# 🚀 Multi-LLM Agent

> **Production-ready AI Agent Platform powered by FastAPI, React, OpenAI, Gemini, Groq & DeepSeek**

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Framework-009688?logo=fastapi)
![React](https://img.shields.io/badge/React-Frontend-61DAFB?logo=react)
![Vite](https://img.shields.io/badge/Vite-Build-646CFF?logo=vite)
![GitHub Actions](https://img.shields.io/github/actions/workflow/status/Prince11-dev/multi-llm-agent/ci.yml?branch=main&label=Build)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📖 Overview

Multi-LLM Agent is a production-ready AI platform that intelligently routes requests across multiple Large Language Models while providing conversation memory, intelligent routing, web search capabilities, and a modern React interface.

The project demonstrates scalable backend architecture using **FastAPI**, asynchronous Python programming, modular AI providers, persistent conversation memory, and a responsive frontend built with **React + Vite**.

---

# ✨ Features

- 🤖 Multi-LLM Integration
  - OpenAI
  - Gemini
  - Groq
  - DeepSeek

- 🧠 Intelligent Model Routing

- 🔀 Multi-model Aggregation

- 💬 Persistent Conversation Memory

- 🌐 Web Search Integration

- ⚡ FastAPI REST API

- 🎨 Modern React Frontend

- 🔄 Asynchronous Request Processing

- 📦 Modular Provider Architecture

- 🧪 Automated GitHub Actions CI

- 🐳 Docker Ready

- 🔒 Environment Variable Configuration

---

# 🏗 Architecture

```text
                    ┌────────────────────┐
                    │    React Frontend  │
                    └─────────┬──────────┘
                              │
                        REST API Calls
                              │
                    ┌─────────▼──────────┐
                    │      FastAPI       │
                    └─────────┬──────────┘
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
        ▼                     ▼                     ▼
 Intelligent Router     Aggregator Service     Memory Layer
        │                     │                     │
        │                     │              SQLite Database
        │                     │
        └──────────────┬──────┘
                       │
      ┌────────────────┼────────────────┐
      ▼                ▼                ▼
    Groq            Gemini          OpenAI
                       │
                       ▼
                  DeepSeek
```

---

# 🛠 Tech Stack

## Backend

- Python 3.12
- FastAPI
- SQLAlchemy
- SQLite
- AsyncIO
- Uvicorn

## AI Providers

- OpenAI
- Google Gemini
- Groq
- DeepSeek

## Frontend

- React
- Vite
- JavaScript
- CSS

## DevOps

- Git
- GitHub
- GitHub Actions
- Docker (Coming Soon)

---

# 📂 Project Structure

```text
multi-llm-agent/

├── app/
│   ├── memory/
│   ├── middleware/
│   ├── providers/
│   ├── schemas/
│   ├── services/
│   ├── tools/
│   ├── utils/
│   └── main.py
│
├── frontend/
│
├── tests/
│
├── scripts/
│
├── .github/
│   └── workflows/
│
├── requirements.txt
├── pytest.ini
├── README.md
└── .env.example
```

---

## 🚀 Current Status

- ✅ Backend CI Passing
- ✅ Frontend CI Passing
- ✅ Multi-LLM Integration
- ✅ Memory Support
- ✅ Intelligent Routing
- ✅ Web Search
- ✅ React Frontend
- ✅ Production Repository Structure

---

## ⭐ Highlights

- Production-ready FastAPI backend
- Modern React frontend
- Intelligent AI model selection
- Modular architecture
- Automated CI/CD pipeline
- Easily extensible provider system