# this is for a chat prompt template where we can use the previous chat like 
# Me:i want my refund.
# AI: it will deposite after 2 days
#now after 2 days
# Me: where is my refund.
# so not Ai load the previous chat and give the answer.

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

#Chat templates
chat_template = ChatPromptTemplate([
    ('system','you are a helpful customer support  agent'),
    MessagesPlaceholder(variable_name='chat_history'),  #by this line it will fatch past all the messages
    ('human','{query}')
])

#load chat history
chat_history=[]
with open('chat_history.txt') as f:
    chat_history.extend(f.readlines())

print(chat_history)

#Create prompt

prompt = chat_template.invoke({'chat_history':chat_history, 'query':'where is my refund'})


print(prompt)