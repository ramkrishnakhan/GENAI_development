from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv

load_dotenv()

os.environ['OPENAI_API_KEY']=os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGSMITH_API_KEY")
app=FastAPI(
    title="Langchain Server",
    version="1.0",
    decsription="A simple API Server"

)


model=ChatOpenAI(model="gpt-3.5-turbo")
##ollama llama2
llm=Ollama(model="llama2")

prompt=ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words")

add_routes(
    app,
    ChatOpenAI(),
    path="/openai"
)
add_routes(
    app,
    prompt|model,
    path="/gpt"
)
add_routes(
    app,
    prompt|llm,
    path="/llm"
)


if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)
