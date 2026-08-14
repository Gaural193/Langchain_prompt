from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate


load_dotenv()

model = ChatOpenAI()


st.header("Rearch Tool")

paper_input = st.selectbox("Select Research Paper Name", ["Attentation Is All You Need","BERT: Pre-training of deep Bidirectional Transformers","GPT-3: Language Model are Few-Shot Learners", "Diffusion Models Beat GANs on Image Systhesis"])

style_input = st.selectbox("Select Explanation Style: ", ["Beginner-friendly", "Technical", "Code-Oriented", "Mathematical"])

length_input = st.selectbox("Serlet Explanation Length", ["Short(1-2 paragraph)", "Medium(3-5 paragraph)", "Long(detailed explanation)"])

template = PromptTemplate(
    template=""" 
    Please summarize the research paper titled "{paper_input}" with the following specifications:
Explanation Style: {style_input}
Explanation Length: {length_input}
1. Mathematical Details:
    - Include relevant mathematical equations if present in the paper.
    - Explain the mathematical concepts using simple, intuitive code snippets where
      applicable.
2. Analogies:
    - Use relatable analogies to simplify complex ideas.
If certain information is not available in the paper, respond with: "Insufficient
information available" instead of guessing.
Ensure the summary is clear, accurate, and aligned with the provided style and length.
 """
)

if st.button("Summarize"):
    # result= model.invoke(user_input)
    st.write("Hello")

