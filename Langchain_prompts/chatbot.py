from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage

load_dotenv()

model=ChatOpenAI()
chat_history=[
    SystemMessage(content='you are helpful assistant')
]
while True:
    user_input=input('you: ')
    chat_history.append(HumanMessage(content=user_input))
    #chat_history.append(user_input)
    if user_input=='exit':
        break
    result=model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    #chat_history.append(result.content)
    print("AI: ",result.content)
    
print(chat_history)
    

