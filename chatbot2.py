from typing import Union, List, TypedDict
from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage
from langgraph.graph import StateGraph, START, END
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7
)

class AgentState(TypedDict): 
    message: list[Union[HumanMessage, AIMessage]]

def process(state: AgentState) -> AgentState:
    """this is the conversation function for the llm""" 
    try:
        response = llm.invoke(state["message"])
        state["message"].append(AIMessage(content=response.content))
        print(f"ai: {response.content}")
        return state
    except Exception as e:
        print(f"Error processing message: {e}")
        state["message"].append(AIMessage(content="Sorry, I encountered an error. Please try again."))
        return state

conversationHistory = []

graph = StateGraph(AgentState)  
graph.add_node("ai", process)
graph.add_edge(START, "ai")
graph.add_edge("ai", END)
agent = graph.compile()

userInput = input("ai: hey there i am the best ai you can ever come across tell me how can i help you \n")

while userInput != "exit":
    if userInput.strip():  
        conversationHistory.append(HumanMessage(content=userInput))
        result = agent.invoke({"message": conversationHistory})
        conversationHistory = result["message"]
        max = 10 
        if len(conversationHistory)>max:
            conversationHistory=conversationHistory[-max:]
    userInput = input("human: ")
    


try:
    with open("logging.txt", "w", encoding="utf-8") as file: 
        file.write("your conversation\n")
        
        for message in conversationHistory:
            if isinstance(message, HumanMessage):
                file.write(f"you: {message.content}\n")
            elif isinstance(message, AIMessage):
                file.write(f"ai: {message.content}\n")
                                 
        file.write("end of the conversation")
    print("Conversation saved to logging.txt")
except Exception as e:
    print(f"Error saving conversation: {e}")
