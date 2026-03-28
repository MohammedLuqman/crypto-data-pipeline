from sqlalchemy import Column, String, Integer, Float,TIMESTAMP
from app.database import Base,get_db
from sqlalchemy.sql import func

class Crypto(Base):
    __tablename__ = "crypto_prices"
    id = Column(Integer , primary_key=True)
    coin_name = Column(String, nullable= False)
    symbol = Column(String, nullable= False)
    price_usd = Column(Float, nullable= False)
    market_cap = Column(Float, nullable=False)
    timestamp = Column(TIMESTAMP, server_default=func.now())