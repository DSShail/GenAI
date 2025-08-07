from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate,load_prompt
import streamlit as st

import sys
import os

load_dotenv()

model=ChatOpenAI(model='gpt-4',temperature=0)
st.header('Research Tool')

research_papers = [
    "AI in Healthcare",
    "Quantum Computing: An Overview",
    "Blockchain Technology: Future of Finance",
    "Climate Change and Its Impact on Biodiversity"
]

styles = [
    "Academic",
    "Casual",
    "Formal",
    "Creative",
    "Technical"
]

lengths = [
    "Short(1 paragraph)",
    "Medium(2 paragraph)",
    "Long(3 paragraph)"
]




# Dropdown for selecting a research paper
research_paper = st.selectbox(
    "Select a Research Paper",
    research_papers
)

# Dropdown for selecting a style
style = st.selectbox(
    "Select Writing Style",
    styles
)

# Dropdown for selecting an action (e.g., summarize, analyze, etc.)
action = st.selectbox(
    "Select length",
    lengths
)

template=load_prompt('template.json')



if st.button('Summarize'):
    
    #creating a chain for creating template and then invoking model
    #chain also calls for model.invoke- we don't need to call it separately
    chain= template | model
    
    #fill the placegholders
    # prompt=template.invoke(
    #     {
    #         'research_paper': research_papers,
    #         'style': styles,
    #         'length': lengths
    #     }
    # )
    
    result=chain.invoke(
        {
            'research_paper': research_papers,
            'style': styles,
            'length': lengths
        }
    )
    
    ##result=model.invoke(prompt)
    st.write(result.content)
    