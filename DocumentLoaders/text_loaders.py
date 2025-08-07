from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

loader=TextLoader(
    file_path="DocumentLoaders\cricket.txt",encoding='utf-8',
)

model=ChatOpenAI()

prompt=PromptTemplate(
    template='Generate a summary for the following poem: {poem}',
    input_variables=['poem']
)

parser=StrOutputParser()

#loading the text file
docs=loader.load()
print(docs)
print(docs[0].page_content)
print(100*"*")

chain=prompt | model | parser

response=chain.invoke({
    'poem':docs[0].page_content})

print("The summary is", response)
