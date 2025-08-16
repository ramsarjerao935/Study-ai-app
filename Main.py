from fastapi import FastAPI
from pydantic import BaseModel
import openai

app = FastAPI()

openai.api_key = "Yahan_Apna_OpenAI_API_KEY_Dalo"

class Question(BaseModel):
    message: str

@app.post("/chat")
def chat(q: Question):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": q.message}]
    )
    return {"reply": response["choices"][0]["message"]["content"]}
