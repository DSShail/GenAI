from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv

model=GoogleGenerativeAI(model='gemini-1.5-pro',api_key="AIzaSyB3_IaaarjEgTyQ8UQc9gZ2nv5IbMx-rig")

result=model.invoke("what is the capital of india")

print(result.content)