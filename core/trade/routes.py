from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
from core.trade.models import Trade
from dependencies import get_db
from core.trade.models import Trade

trade_router = APIRouter()

@trade_router.get('/trades')
async def read_item(symbol: str, db: Session = Depends(get_db)):
    # This won't work, since we don't have an id column in our table
    # q = db.query(Trade).filter_by(symbol=symbol.upper()).limit(100).all()
    # return q

    with db as session:
        trades = session.execute("SELECT symbol, price, cancelled_indicator FROM trades WHERE symbol = :symbol LIMIT 1000", {"symbol": symbol.upper()}).scalars()
    return StreamingResponse(trades, media_type="application/json")