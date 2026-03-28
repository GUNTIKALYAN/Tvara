from fastapi import FastAPI, HTTPException
from openai import OpenAI
from dotenv import load_dotenv
import os
from pydantic import BaseModel


client = OpenAI(
    api_key=os.environ.get("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)


app = FastAPI()

class RequestModel(BaseModel):
    prompt: str


@app.post("/")
def dashboard():
    return {"API Check"}


@app.post("/chat")
async def chat(request: RequestModel):

    try:
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "user", "content": request.prompt}
            ],
        )

        return {
            "response": completion.choices[0].message.content
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    