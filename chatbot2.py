from typing import Union , List, TypedDict
from dotenv import load_dotenv
from langchain_core.messages import AIMessage,HumanMessage
from langgraph.graph import StateGraph,START,END
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7
)

class AgenState(TypedDict):
    message: list[Union[HumanMessage,AIMessage]]

def process(state:AgenState)->AgenState:
    """this is the conversation fucntion for the llm""" 
    response = llm.invoke(state["message"])
    state["message"].append(AIMessage(content=response.content))
    print(f"ai :{response.content}")
    return state

conversationHistory=[]

graph=StateGraph(AgenState)
graph.add_node("ai",process)
graph.add_edge(START,"ai")
graph.add_edge("ai",END)
agent = graph.compile()


userInput=input("ai :hey there i am the best ai you can ever come accros tell me how can i help you \n")

while userInput!="exit":
    conversationHistory.append(HumanMessage(content=userInput))
    result = agent.invoke({"message":conversationHistory})
    conversationHistory = result["message"]
    userInput=input("human : ")

      

   