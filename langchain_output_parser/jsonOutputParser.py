from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

from langchain_openai import ChatOpenAI

#load the env variables
load_dotenv()

#import llm model from hugging face
# llm=HuggingFaceEndpoint(
#     repo_id="bigscience/bloomz-560m",
#     task="text-generation"
# )

model=ChatOpenAI()

#creating chat model instance
#model=ChatHuggingFace(llm=llm)

parser=JsonOutputParser()

template=PromptTemplate(
    #template='Give me the name, age, city of a fictional person\n {format_instruction}',
    template='Give me 5 line summary about {topic}.\n{format_instruction}',
    input_variables=['topic'],
    #this is getting filled during compile time   
    # not run time
    partial_variables={'format_instruction':parser.get_format_instructions()} 
)

# prompt1=template.format()

# #print(prompt1)

# result=model.invoke(prompt1)

# print(result.content)

# final_result=parser.parse(result.content)

# print('Final Result:',final_result)
# print('Name:',final_result['name'])
# print('Age:',final_result['age'])
# print('City:',final_result['city'])

#using chain to perform above steps

chain=template | model | parser

# pass blank dictionary to chain as we are not using any input variables
result=chain.invoke({'topic':'black hole'})

print('Final Result:',result)