from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from  langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model=ChatOpenAI()

template1=PromptTemplate(
    template="write a detailed report about a {topic}",
    input_variables=['topic']
)

template2=PromptTemplate(
    template="Write a 5 line summary on following text. /n {text}",
    input_variables=['text']
)

parser=StrOutputParser(
    
)

#flow
chain= template1 | model | parser | template2 | model | parser

result=chain.invoke({'topic':'black hole'})

print(result)