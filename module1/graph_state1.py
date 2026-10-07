from typing import TypedDict

from langgraph.graph import StateGraph, START, END


# state
class State(TypedDict):
    graph_state: str


# node
def greeting(state: State) -> dict:
    """hello everyone"""
    return {"graph_state": state["graph_state"] + " welcome to langgraph"}


# graph
builder = StateGraph(State)
builder.add_node("greeting", greeting)
builder.add_edge(START, "greeting")
builder.add_edge("greeting", END)

graph = builder.compile()

#if __name__ == "__main__":
  #  print(graph.invoke({"graph_state": "hello"}))
