from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
#from huggingface_hub import HfApi
#import os

load_dotenv()


# hf_token=os.getenv('HUGGINGFACEHUB_ACCESS_TOKEN')
# if not hf_token:
#     raise ValueError('HuggingFace API token not found in environment variables')
# else:
#     print(hf_token)
#     print('Token is present')
    

# Initialize HuggingFace API with the token
#api = HfApi(token=hf_token)    

#creating llm endpoint using HuggingFaceEndpoint
llm=HuggingFaceEndpoint(
    model="HuggingFaceH4/zephyr-7b-beta",
    task='text-generation'
    #client=InferenceClient(model='TinyLlama/TinyLlama-1.1B-Chat-v1.0', timeout=120, token=hf_token),
    #async_client=InferenceClient(model='TinyLlama/TinyLlama-1.1B-Chat-v1.0', timeout=120, token=hf_token)
)

model=ChatHuggingFace(llm=llm)

print(f'model detail: {model}')
try:
    response = model.invoke([
        {"role": "user", "content": "What is the capital of India?"}
    ])
    
    print(response.content)
except Exception as e:
    print(f'Exception while invoking the model: {llm.model} {e}')
    import traceback
    traceback.print_exc()

