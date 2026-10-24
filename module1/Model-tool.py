from langgraph.graph import START, END, MessagesState, StateGraph
from langgraph.prebuilt import ToolNode, tools_condition
from typing_extensions import TypedDict
from typing import Literal, NotRequired
import os
from dotenv import load_dotenv
from langchain_google_genai import  ChatGoogleGenerativeAI
from langchain_core.tools import tool


load_dotenv()  # loads Gemini_Api_Key from .env


model_llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",
    google_api_key=os.environ["Gemini_Api_Key"],
)

@tool
def multiply(nb1: int, nb2: int) -> int:
    """Multiply two numbers."""
    return nb1 * nb2

model_llm_with_tool = model_llm.bind_tools([multiply])

# node 

def chat_with_tool(state: MessagesState) -> MessagesState:
    return {"messages":model_llm_with_tool.invoke(state["messages"])}

# graphs 

builder = StateGraph(MessagesState)

builder.add_node("chat_with_tool", chat_with_tool)
builder.add_node("tools", ToolNode([multiply]))

builder.add_edge(START, "chat_with_tool")

# routes to "tools" if the model called a tool, otherwise to END
builder.add_conditional_edges("chat_with_tool", tools_condition)

builder.add_edge("tools", "chat_with_tool")

graph = builder.compile()
    
