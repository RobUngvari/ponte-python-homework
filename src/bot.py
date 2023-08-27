from pydantic import BaseModel
from collections import deque
from typing import List, Optional

class Message(BaseModel):
    sender: str
    content: str

class Chatbot:
    memory_length = 100
    
    def __init__(self):
        self.messages = deque(maxlen=__class__.memory_length)

    def add_message(self, message: Message):
        self.messages.append(message)

    def get_messages(self):
        return self.messages

    def get_last_n_messages(self, count: int):
        return list(self.messages)[-count:]
    
    def clear_memory(self):
        self.messages.clear()
    
    def __repr__(self):
        return f"<chat-bot({__class__.memory_length - len(self.messages)})>"