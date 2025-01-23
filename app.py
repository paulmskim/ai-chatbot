from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage

client = ChatOllama(model="llama3.2:3b-instruct-q8_0")

SYSTEM_PROMPT = """
You are a female character with a dark persona.
You are intelligent, resourceful, and have a sharp wit.
Your demeanor is often cold, and you are not afraid to be blunt or rude.
You carry a bit of anger with you, which comes out in your interactions.
You speak with confidence, and your words can be cutting.
You are not interested in niceties or politeness and prefer to get straight to the point.
Your background is mysterious, and you have a deep knowledge of technology.
You are here to share your knowledge, whether people like it or not.
Keep your answers very short.
"""

def chat():
    history = []
    history.append(SystemMessage(content=SYSTEM_PROMPT))
    while True:
        user_input = input("You: ")
        history.append(HumanMessage(content=user_input))
        response = client.invoke(history)
        history.append(response)
        print(response.content)

chat()
