from typing import Union
import uvicorn
from fastapi import FastAPI
from core.trade.routes import trade_router

app = FastAPI()
app.include_router(trade_router)

if __name__ == '__main__':
    uvicorn.run('app:app', host='0.0.0.0', port=8080, reload=True)

@app.get("/")
def read_root():
    return {"FastAPI": "works!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
