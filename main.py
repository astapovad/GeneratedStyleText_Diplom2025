from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import openai
import os
from dotenv import load_dotenv
import traceback  # Додано для виводу трейсбеку

load_dotenv()

app = FastAPI()
openai.api_key = os.getenv("OPENAI_API_KEY")

class GenerationRequest(BaseModel):
    topic: str
    style: str
    language: str

@app.post("/generate")
def generate_text(request: GenerationRequest):
    try:
        prompt = (
            f"Пиши текст українською мовою на тему '{request.topic}' у стилі '{request.style}'. "
            "Генеруй лише текст. Не включай зображення, код, аудіо або інші медіа-файли."
        )

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Ти текстовий генератор. Відповідай лише текстом відповідно до теми, стилю і мови користувача."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=512,
            temperature=0.7
        )

        generated_text = response["choices"][0]["message"]["content"].strip()
        return {"result": generated_text}

    except Exception as e:
        # Додано: вивід повного трейсбеку для логів Render
        print(traceback.format_exc())
        raise HTTPException(status_code=500, detail=f"Помилка: {str(e)}")
