from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from state import State

def simple_answer_agent_node(state: State):
    """An agent that generates a simple answer for the user question."""
    
    print(f"Generating simple answer for the user question: {state['user_question']}")
    
    llm = ChatOpenAI(model= "gpt-4o", temperature= 0)
    
    prompt_template = ChatPromptTemplate.from_template(
        """
        You are a helpful assistant that generates a simple answer for the user question. Be kind, concise and friendly.
        
        The user asked: {user_question}. 
        """
    )
    
    prompt = prompt_template.format(user_question=state["user_question"])
    
    response = llm.invoke(prompt)
    
    print(f"Simple answer generated: {response.content}")
    
    return {"ai_answer": response.content}