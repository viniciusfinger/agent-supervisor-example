from typing import TypedDict
from graph_status import GraphStatus

class State(TypedDict):
    user_question: str
    ai_answer: str
    graph_status: GraphStatus