from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
   
# Load the env variables    
load_dotenv()

#define a openai chat model
model=ChatOpenAI()

class Person(BaseModel):
    name: str=Field(description="Name of the person")
    age: int=Field(gt=18,description="Age of the person")
    city:str=Field(description="Name of the city person belongs to")
    
parser=PydanticOutputParser(pydantic_object=Person) 

template=PromptTemplate(
    template='Generate the name,age,city of a fictional {place} person.\n {format_instruction}',
    input_variables=['place'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)   

chain=template |model |parser

#print("Template after chain implementation: ",template)
result=chain.invoke({'place':'russian'})

print('Final Result:',result)