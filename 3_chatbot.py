from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage

load_dotenv()

model = ChatOpenAI()


#the below code does not have the context window means it forgot the previous prompts.
# while True:
#     user_input = input("You: ")
#     if user_input == "exit":
#         break
#     result = model.invoke(user_input)
#     print("AI: ",result.content)

# ------------------------------< This is for the history, but this is not a relaable >-----------------------------

# chat_history = []
# while True:
#     user_input = input("You: ")
#     chat_history.append(user_input)
#     if user_input == "exit":
#         break
#     result = model.invoke(chat_history)
#     chat_history.append(result.content)
#     print("AI: ",result.content)

# print(chat_history)


# -----------------< This is for the history using the langchain_core.messages more detail in messagers.py >---------------

chat_history = [
    SystemMessage(content="You are a Helpful Ai assistant")
    
]
while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input == "exit":
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI: ",result.content)

print(chat_history)

