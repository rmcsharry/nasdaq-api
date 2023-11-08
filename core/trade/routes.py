import json
from re import split
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import StreamingResponse
from sqlalchemy import text
from sqlalchemy.orm import Session
from core.trade.models import Trade
from dependencies import get_db
from core.trade.models import Trade

trade_router = APIRouter()

@trade_router.get('/trades')
def read_item(symbol: str, db: Session = Depends(get_db)):
    # This won't work, since we don't have an id column in our table
    # q = db.query(Trade).filter_by(symbol=symbol.upper()).all()
    # return q

    with db as session:
        trades = session.execute(text("SELECT * FROM trades WHERE symbol = :symbol"), {"symbol": symbol.upper()})

    def iter_trades():
        for trade in trades:
            yield json.dumps({
                "trade_date": str(trade.trade_date),
                #"market_center": trade.market_center,
                "price": str(trade.price),
                "quantity": trade.quantity,
                #"sales_conditions": trade.sales_conditions,
                #"listing_venue": trade.listing_venue,
                #"dott": trade.dott,
                #"msn": trade.msn,
                #"omsn": trade.omsn,
                #"sub_market_center": trade.sub_market_center,
                #"cancelled_indicator": trade.cancelled_indicator
            }) + "\n"
            # send as csv
            # yield f"{trade.symbol}, {trade.price}, {trade.cancelled_indicator}\n"

    return StreamingResponse(iter_trades(), media_type="application/json")
