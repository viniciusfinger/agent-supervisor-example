from graph import create_graph

graph = create_graph()

config = {"recursion_limit": 5}

response = graph.invoke({"user_question": "What is the capital of France?"}, config=config)

print(response)
