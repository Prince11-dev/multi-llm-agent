from app.memory.database import init_db
from app.memory.store import save_conversation
from app.memory.retrieve import get_history

init_db()

save_conversation(
    "test",
    "What is FastAPI?",
    "FastAPI is a Python web framework."
)

history = get_history("test")

print(history)