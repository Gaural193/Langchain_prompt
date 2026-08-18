# there are theree type of messages in langchain system msg, Ai msg, and human message.

from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

messages = [
    SystemMessage(content="You are a Helpful Assistant"),
    HumanMessage(content="tell me how to use LLM")
]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)