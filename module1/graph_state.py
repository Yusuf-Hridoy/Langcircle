from typing import TypedDict

from langgraph.graph import StateGraph, START, END

# state
class State(TypedDict):
    text: str

# node
def greeting(state: State) -> dict:
    """greet people"""
    return {"text": state["text"] + " welcome to langgraph"}

# langgraph
builder = StateGraph(State)

# add node
builder.add_node("greeting", greeting)

# add edge
builder.add_edge(START, "greeting")
builder.add_edge("greeting", END)

graph = builder.compile()

#if __name__ == "__main__":
    #print(graph.invoke({"text": "hello"}))  # returns {"text": "hello welcome to langgraph"}
