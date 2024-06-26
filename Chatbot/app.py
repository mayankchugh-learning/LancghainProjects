from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
## Langmith tracking
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

os.environ["OPENAI_MODEL_NAME"]=os.getenv("OPENAI_MODEL_NAME")

model = os.environ["OPENAI_MODEL_NAME"]
## Prompt Template

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please response to the user queries"),
        ("user","Question:{question}")
    ]
)

## streamlit framework

st.title("💬 Chatbot")
st.caption("🚀 A Streamlit chatbot powered by OpenAI using Lancghain")

    
input_text=st.text_input("Enter text to search")

# openAI LLm 
#llm=ChatOpenAI(model="gpt-3.5-turbo")

# llm = ChatOpenAI(
#     model="llama3",
#     base_url="http://localhost:11434/v1",
#     api_key="NA"
# )
llm = ChatOpenAI(model=model)

output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))