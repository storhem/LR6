from fastapi import FastAPI, HTTPException
from typing import List

app = FastAPI()

notes = []
next_id = 1

@app.get("/")
def root():
    return {"message": "API для заметок. Документация: /docs"}

@app.get("/notes", response_model=List[dict])
def get_notes():
    return notes