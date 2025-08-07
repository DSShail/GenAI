from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model=ChatOpenAI()

prompt=PromptTemplate(
    template='Answer the following questions \n {questions} from given text \n {text}',
    input_variables=['text', 'questions']
)

parser=StrOutputParser()

loaders=WebBaseLoader('https://www.flipkart.com/hp-victus-intel-core-i5-14th-gen-14450hx-16-gb-512-gb-ssd-windows-11-home-6-graphics-nvidia-geforce-rtx-3050-144-hz-16-r1705tx-gaming-laptop/p/itmc62ebc24c2cfd?pid=COMHBZT389VW3CYA&lid=LSTCOMHBZT389VW3CYASHNDVJ&marketplace=FLIPKART&q=hp+laptop&store=6bo%2Fb5g&srno=s_1_5&otracker=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&fm=organic&iid=32878987-c9a5-4df2-864a-3c1da0ea2dbc.COMHBZT389VW3CYA.SEARCH&ppt=hp&ppn=homepage&ssid=t8fxzu36800000001753548459819&qH=9d1edd3d0f6d1b3c'   
)

docs=loaders.load()

# print(len(docs))
# print(docs[0].page_content)

chain=prompt | model | parser

question = 'What is the screen size of the laptop?'
response = chain.invoke({'questions': question, 'text': docs[0].page_content})

print(f"The answer to question '{question}' is: {response}")