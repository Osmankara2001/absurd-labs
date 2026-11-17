
import os
from pathlib import Path
from fastapi.responses import FileResponse

from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from openai import OpenAIError

from app.graph import invention_graph


app = FastAPI(title="Absurd Labs")


class InventionRequest(BaseModel):
    words: list[str] = Field(min_length=3, max_length=3)


@app.get("/")
def home():
    html_path = Path(__file__).parent / "static" / "index.html"
    return FileResponse(html_path)


@app.post("/invent")
def invent(request: InventionRequest):
    words = [word.strip() for word in request.words]

    if any(not word for word in words):
        raise HTTPException(
            status_code=400,
            detail="Kelimeler bos olamaz."
        )

    try:
        result = invention_graph.invoke({
            "words": words
        })

        return {
            "words": words,
            "inventor": result["inventor"],
            "engineer": result["engineer"],
            "investor": result["investor"]
        }

    except OpenAIError as error:
        print(f"OpenAI API hatasi: {error}")
        raise HTTPException(
            status_code=502,
            detail="OpenAI API istegi basarisiz oldu."
        )
