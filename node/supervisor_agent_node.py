from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from graph_status import GraphStatus
from state import State
import logging


def supervisor_agent_node(state: State):
    """An agent that validates if the task is finished or not, evaluating the answer of the ai and the user question."""
    
    llm = ChatOpenAI(model= "gpt-4o-mini", temperature= 0).with_structured_output(GraphStatus)
    
    prompt_template = ChatPromptTemplate.from_template(
        """
        The user asked: {user_question}. 
        The AI answer generated was: {ai_answer}. 
        
        Dispensing validations of time, the answer is a good answer for the user question?
        
        Please validate if the answer was correct and if the task is finished. 
        
        If yes, answer with "FINISH", if not, answer with "CONTINUE".
        """
    )
    
    prompt = prompt_template.format(user_question=state["user_question"], ai_answer=state["ai_answer"])
    
    response = llm.invoke(prompt)
    
    print(f"Supervisor agent node response: {response.status}")
    
    return {"graph_status": response.status}