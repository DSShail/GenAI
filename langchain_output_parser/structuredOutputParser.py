from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

# load the env variables
load_dotenv()

model=ChatOpenAI()

print("Model created : the model details are \n ------------------ ",model)

schema=[
    ResponseSchema(name='fact 1',description='First fact about the topic'),
    ResponseSchema(name='fact 2',description='Second fact about the topic'),   
    ResponseSchema(name='fact 3',description='Third fact about the topic')]

parser=StructuredOutputParser.from_response_schemas(schema)

template=PromptTemplate(
    template='Give me 3 facts about {topic}.\n{format_instruction}',
    input_variables=['topic'],
    # this is getting filled during compile time   
    # not run time
    partial_variables={'format_instruction':parser.get_format_instructions()} 
)

print("the tempalate is ",template)
chain=template | model | parser
result=chain.invoke({'topic':'black hole'})
print(result)

