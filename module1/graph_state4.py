from langgraph.graph import START, END, StateGraph
from typing_extensions import TypedDict
from typing import Literal, NotRequired
import os
from dotenv import load_dotenv
from langchain_google_genai import  ChatGoogleGenerativeAI

load_dotenv()  # loads Gemini_Api_Key from .env

model_llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",
    google_api_key=os.environ["Gemini_Api_Key"],
)


#state 
class State(TypedDict):
    graph_int: NotRequired[int]
    graph_str: str

#node 

def node1(state: State) -> State:
    """Pick a number between 1 and 10 and store it in the state."""
    model_response = model_llm.invoke("reply with number only ")

    if isinstance(int(model_response.content), int):
        return {"graph_int": int(model_response.content), "graph_str": state["graph_str"] + "passed by node 1 "}

    return{"graph_int":0, "graph_str": state["graph_str"] + "passed by node 1 "}

def node2(state: State) -> State:
    """choose umber between 2 and 3"""

    return{"graph_int":state["graph_int"], "graph_str": state["graph_str"] + "passed by node 2 "}

def node3(state: State) -> State:
    """choose number between 1 and 2"""

    return{"graph_int":state["graph_int"], "graph_str": state["graph_str"] + "passed by node 3 "}




#edge 

def next_step(state: State) -> Literal["node2", "node3", "END"]:
    """check state and return which nbode to go """
    number_state =state["graph_int"]
    if number_state == 0:
        return "node2"
    elif number_state == 3:
        return "node3"
    else:
        return "END"

#graph

builder = StateGraph(State)

builder.add_node("node1", node1)
builder.add_node("node2", node2)
builder.add_node("node3", node3)


builder.add_edge(START, "node1")



