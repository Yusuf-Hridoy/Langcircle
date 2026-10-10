from langgraph.graph import START, END, StateGraph
from typing_extensions import TypedDict
from typing import Literal 

#state 
class State(TypedDict):
    graph_str: str

#node 
def node1(state: State) -> State:
    """this wil greet """
    return {"graph_str": state["graph_str"] + "Hello, welcome to the graph!"}

def node2(state: State) -> State:
    """this will process the input """
    return {"graph_str": state["graph_str"] + "Processing..."}

def node3(state: State) -> State:
    """this will finalize the output """
    return {"graph_str": state["graph_str"] + "Finalizing..."}

#edge 
def next_step(state: State) -> Literal["node2", "node3"]:
    """this will determine the next step based on some condition"""
    state_str = state["graph_str"]
    array_state_str = state_str.split(" ")

    if array_state_str[0] == "hello":
        return "node3"
    else:
        return "node2"

#graph

builder = StateGraph(State)

builder.add_node("node1", node1)
builder.add_node("node2", node2)
builder.add_node("node3", node3)

builder.add_edge(START, "node1")
builder.add_conditional_edges("node1", next_step)
builder.add_edge("node2", END)
builder.add_edge("node3", END)

graph = builder.compile()