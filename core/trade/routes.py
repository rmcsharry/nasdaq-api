from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
from core.trade.models import Trade
from dependencies import get_db

trade_router = APIRouter()

@trade_router.get('/trades')
async def read_item(symbol: str, db: Session = Depends(get_db)):
    with db as session:
        trades = session.execute("SELECT symbol, price, cancelled_indicator FROM trades WHERE symbol = :symbol LIMIT 100", {"symbol": symbol.upper()}) 
    return StreamingResponse(trades)