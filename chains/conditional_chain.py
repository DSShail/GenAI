from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain.schema.runnable import RunnableParallel, RunnableBranch, RunnableLambda
from pydantic import BaseModel, Field
from typing  import Literal

load_dotenv()

openai_model=ChatOpenAI()

parser=StrOutputParser()


class Feedback(BaseModel):
    sentiment: Literal['positive','negative'] =Field(description='Give the sentiment of the feedback')



parser2=PydanticOutputParser(pydantic_object=Feedback)
prompt1=PromptTemplate(
    template='classify the sentiments of the following feedback into positive or negative \n {feedback} \n {format_instruction}',
    input_variables=['feedback'],
    partial_variables={'format_instruction':parser2.get_format_instructions}
    )


classifier_chain=prompt1 | openai_model | parser2

# result=classifier_chain.invoke({'feedback':'Iphone is terrible smartphone'}).sentiment

# print(result)



prompt2=PromptTemplate(
    template='write an appropriate response to this postitive feedback \n {feedback}',
    input_variables=['feedback']
)


prompt3=PromptTemplate(
    template='write an appropriate response to this negative feedback \n {feedback}',
    input_variables=['feedback']
)
#using runnable branch  you can use condtional branch

branch_chain=RunnableBranch(
    (lambda x:x.sentiment=='positive', prompt2| openai_model | parser),
    (lambda x:x.sentiment=='negative', prompt3| openai_model | parser),
    
    #default chain - here also we need to implement chain - we will concept of runnable here
    #convert lanbda function into RunnableLambda
    RunnableLambda((lambda x: "couldn't find appropriate sentiment"))
)

chain=classifier_chain | branch_chain

print(chain.invoke({'feedback':'Iphone is terrible smartphone'}))

#print the chain
print(chain.get_graph().print_ascii())

