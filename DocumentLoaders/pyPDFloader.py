from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

loader=PyPDFLoader(
    file_path="DocumentLoaders\dl-curriculum.pdf"
)

docs=loader.load()

print("no of documents object loaded from given pdf is ",len(docs))

print(docs[0].page_content)
print(docs[0].metadata)
