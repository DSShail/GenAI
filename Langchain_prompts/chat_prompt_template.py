from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage,HumanMessage

chat_template=ChatPromptTemplate([
   
    ('system','you are helpful {domain} expert')
    ('human','Explain in simple words about {topic}')
])

#behaviour is bit different compare to PromptTemplate
prompt=chat_template.invoke({'domain':'cricket','topic':'dusra'})

print(prompt)