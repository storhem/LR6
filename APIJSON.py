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

@app.post("/items")
def create_item(item_id: int, name: str, description: Optional[str] = None):
    if item_id in items_db:
        raise HTTPException(status_code=400, detail="Item already exists")

    item = {
        "id": item_id,
        "name": name,
        "description": description
    }
    items_db[item_id] = item
    return item