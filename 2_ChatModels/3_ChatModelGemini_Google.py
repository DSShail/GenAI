from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv

loadenv=load_dotenv()
api_key=loadenv.get("GOOGLE_API_KEY")
model=GoogleGenerativeAI(model='gemini-1.5-pro',api_key=api_key)

result=model.invoke("what is the capital of india")

print(result.content)