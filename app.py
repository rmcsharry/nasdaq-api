from typing import Union
import uvicorn
from fastapi import FastAPI
from core.trade.routes import trade_router

app = FastAPI()
app.include_router(trade_router)

if __name__ == '__main__':
    uvicorn.run('app:app', host='127.0.0.1', port=8000, reload=True)

@app.get("/")
def read_root():
    return {"FastAPI": "works!"}
