from fastapi import FastAPI, HTTPException
from typing import Optional

app = FastAPI()

items_db = {}

@app.get("/")
def read_root():
    return {"message": "HELLO FastAPI!", "status": "работает"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return items_db[item_id]