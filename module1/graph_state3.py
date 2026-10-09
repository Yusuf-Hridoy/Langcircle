from langgraph.graph import START, END, StateGraph
from typing_extensions import TypeDict
from typing import Literal 

#state 
class State(TypeDict):
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