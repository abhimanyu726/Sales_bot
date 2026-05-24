from fastapi import FastAPI
from pydantic import BaseModel

from graph.sales_graph import (
    SalesGraph
)

app = FastAPI()

graph = SalesGraph().compile()


class ChatRequest(BaseModel):

    message: str


@app.post("/chat")
async def chat(request: ChatRequest):

    initial_state = {
        "user_input": request.message,
        "conversation_history": [],
        "intent": None,
        "lead_score": 0,
        "qualified": False,
        "adherence_score": 0,
        "crm_logged": False,
        "escalation_required": False,
        "response": None
    }

    result = await graph.ainvoke(
        initial_state
    )

    return result