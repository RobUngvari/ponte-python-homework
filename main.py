from fastapi import FastAPI
from src.bot import Chatbot, Message

app = FastAPI()
chatbot = Chatbot()


## testing purposes

chatbot.add_message(Message(sender='Agent_01', 
                            content='This is a basic test message.'))
chatbot.add_message(Message(sender='Agent_02', 
                            content='This is an initial test message.'))

@app.get("/")
async def get_messages():
    return {"messages": "Hello Ponte"}

@app.get("/messages/")
async def get_messages():
    messages = [{'sender': m.sender, 'content' : m.content} for m in chatbot.get_messages()]
    return {"messages": messages}

@app.get("/get-last-messages/")
async def get_last_messages(count: int = 10):
    messages = [{'sender': m.sender, 'content' : m.content} for m in chatbot.get_last_n_messages(count)]
    return {"messages": messages}
