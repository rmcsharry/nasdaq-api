from typing import Union
import uvicorn
from fastapi import FastAPI
from database import Base, engine

app = FastAPI()
Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    uvicorn.run('app:app', host='0.0.0.0', port=8080, reload=True)

@app.get("/")
def read_root():
    return {"FastAPI": "works fine!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
