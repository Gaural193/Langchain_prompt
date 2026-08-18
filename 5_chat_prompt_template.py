# here we are doing dynamic prompt using langchain_core.messages
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv


load_dotenv()

chat_template = ChatPromptTemplate([
    # here the below steps are little different from previous files.
    ('system','You are a Helpful {domain} expert'),  
    ('human','Explain in simple terms what is {topic}')
])

prompt = chat_template.invoke({'domain':'pickle ball','topic':'rules'})

print(prompt)




