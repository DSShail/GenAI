from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from  langchain.prompts import PromptTemplate

load_dotenv()

llm=ChatOpenAI()

template1=PromptTemplate(
    template="write a detailed report about a {topic}",
    input_variables=['topic']
)

template2=PromptTemplate(
    template="Write a 5 line summary on following text. /n {text}",
    input_variables=['text']
)

prompt1=template1.invoke({'topic':'black_hole'})
result1=llm.invoke(prompt1)

prompt2=template2.invoke({'text':result1.content})
result2=llm.invoke(prompt2)

print("The 5 line summary is \n",result2)

