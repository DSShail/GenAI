from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

#load the env variables
load_dotenv()

#import llm model from hugging face
llm=HuggingFaceEndpoint(
    repo_id="google/magenta-realtime",
    task="text-generation"
)

#creating chat model instance
model=ChatHuggingFace(llm=llm)

#check hf_connection
def test_hf_connection():
    print("============Testing hf connection================")
    
    try:
        from huggingface_hub import HfApi
        api=HfApi()
        
        user_info=api.whoami()
        print(f"Connected to HF hub as {user_info.get('name','radheshail')}")
    except Exception as e:
        print(f"HF connection failed: {e}")

template1=PromptTemplate(
    template="write a detailed report about a {topic}",
    input_variables=['topic']
)

template2=PromptTemplate(
    template="Write a 5 line summary on following text. /n {text}",
    input_variables=['text']
)
def invoke_model():
    prompt1=template1.invoke({'topic':'black_hole'})
    result1=model.invoke(prompt1)

    prompt2=template2.invoke({'text':result1.content})
    result2=model.invoke(prompt2)

    print("The 5 line summary is \n",result2)
def apply_fixes():
    """Apply common fixes"""
    print("\n=== Applying Fixes ===")
    
    fixes = [
        "pip install --upgrade huggingface-hub",
        "pip install --upgrade langchain-huggingface",
        "pip install --upgrade transformers",
        "huggingface-cli login",  # Interactive login
    ]
    
    print("Run these commands to fix common issues:")
    for fix in fixes:
        print(f"  {fix}")
    
    print("\nOr run them automatically? (y/n): ", end="")
    if input().lower() == 'y':
        import subprocess
        for fix in fixes[:-1]:  # Skip the login command
            try:
                subprocess.run(fix.split(), check=True)
                print(f"✅ {fix}")
            except subprocess.CalledProcessError as e:
                print(f"❌ {fix} failed: {e}")
def main():
    print("🔍 Hugging Face Configuration Debugger")
    print("=" * 50)
   # test_hf_connection()
   # apply_fixes()
    invoke_model()
    
    
    
if __name__=="__main__":
    main()
    