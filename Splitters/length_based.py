from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders  import PyPDFLoader
import os

file_path=r'D:\Codebase\GenAI\Splitters\dl-curriculum.pdf'
if os.path.isfile(file_path):
    print('File available')
    loader=PyPDFLoader(file_path)
else:
    print(f'File not found at {file_path}')

splitter=CharacterTextSplitter(
    chunk_size=200, #size of each chunk will be of 200 characters
    chunk_overlap=0,
    #seperator='' 
)

text='''
    Agentic AI refers to artificial intelligence systems that possess the capacity to act autonomously, make decisions, and pursue goals independently. Unlike traditional AI, which typically follows predefined instructions, agentic AI can initiate actions, adapt to changing environments, and optimize outcomes based on its objectives. These systems often incorporate elements like reinforcement learning, planning algorithms, and reasoning capabilities to simulate agency. Agentic AI holds promise for complex tasks such as robotics, supply chain optimization, and personalized education. However, its development raises ethical concerns around accountability, control, and alignment with human values, making responsible design and oversight critically important.
'''

result=splitter.split_text(text)

print(result)

