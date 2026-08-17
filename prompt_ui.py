from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate , load_prompt
#load_prompt is for importing template from the prompt_generator.py


load_dotenv()

model = ChatOpenAI()


st.header("Rearch Tool")

paper_input = st.selectbox("Select Research Paper Name", ["Attentation Is All You Need","BERT: Pre-training of deep Bidirectional Transformers","GPT-3: Language Model are Few-Shot Learners", "Diffusion Models Beat GANs on Image Systhesis"])

style_input = st.selectbox("Select Explanation Style: ", ["Beginner-friendly", "Technical", "Code-Oriented", "Mathematical"])

length_input = st.selectbox("Serlet Explanation Length", ["Short(1-2 paragraph)", "Medium(3-5 paragraph)", "Long(detailed explanation)"])


# -----------------------------------------------------------------
# Now the below template is comming from the prompt_generator.py file 
# template = PromptTemplate(
#     template=""" 
#     Please summarize the research paper titled "{paper_input}" with the following specifications:
# Explanation Style: {style_input}
# Explanation Length: {length_input}
# 1. Mathematical Details:
#     - Include relevant mathematical equations if present in the paper.
#     - Explain the mathematical concepts using simple, intuitive code snippets where
#       applicable.
# 2. Analogies:
#     - Use relatable analogies to simplify complex ideas.
# If certain information is not available in the paper, respond with: "Insufficient
# information available" instead of guessing.
# Ensure the summary is clear, accurate, and aligned with the provided style and length.
#  """,
# input_variables = ['paper_input','style_input','length_input'],
# validate_template=True #this will give us a error message wjen we there is extra or less parameter in above input_variable
# )

template = load_prompt('template.json')
# prompt = template.invoke({
#     'paper_input':paper_input,
#     'style_input': style_input,
#     'length_input':length_input
# })

# if st.button("Summarize"):
#     result = model.invoke(prompt)
#     st.write(result.content)

# Now if we want to make a Chian.  


if st.button("Summarize"):

    chain = template | model 
    result = chain.invoke({
    'paper_input':paper_input,
    'style_input': style_input,
    'length_input':length_input
    })

    st.write(result.content)    