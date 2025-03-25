from langgraph.graph import StateGraph
from state import State
from node.simple_answer_agent_node import simple_answer_agent_node
from node.supervisor_agent_node import supervisor_agent_node
from langgraph.graph import START, END

def create_graph() -> StateGraph:
    
    graph = StateGraph(State)
   
    graph.add_node("simple_answer_agent_node", simple_answer_agent_node)
    graph.add_node("supervisor_agent_node", supervisor_agent_node)
    
    graph.add_edge(START, "simple_answer_agent_node")
    graph.add_edge("simple_answer_agent_node", "supervisor_agent_node")
    
    graph.add_conditional_edges(
        "supervisor_agent_node",
        lambda graph: graph["graph_status"],
        {
            "FINISH": END,
            "CONTINUE": "simple_answer_agent_node"
        }
    )
    
    return graph.compile()