from sqlalchemy import Column, Integer, String, Numeric, Boolean, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID
import uuid

Base = declarative_base()

class Trade(Base):
    __tablename__ = 'trades'

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    trade_date = Column(TIMESTAMP(timezone=True))
    symbol = Column(String(10))
    market_center = Column(String(1))
    price = Column(Numeric(10, 5))
    quantity = Column(Integer)
    sales_conditions = Column(String(5))
    listing_venue = Column(String(1))
    dott = Column(String(1))
    msn = Column(Integer)
    omsn = Column(Integer)
    sub_market_center = Column(String(10))
    cancelled_indicator = Column(Boolean)