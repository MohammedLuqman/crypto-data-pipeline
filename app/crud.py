from fastapi import FastAPI, HTTPException,APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Crypto

router = APIRouter(prefix= "/coins", tags=["coins"])

@router.get("/")
def get_all(db : Session = Depends(get_db)):
    coins = db.query(Crypto).all()
    return coins

@router.get("/top")
def get_top(db: Session = Depends(get_db)):
    top = db.query(Crypto).order_by(Crypto.market_cap.desc()).limit(10).all()
    return top

@router.get("/prices/{symbol}")
def get_price(symbol: str, db: Session = Depends(get_db)):
    from sqlalchemy import func
    price_entry = db.query(Crypto).filter(
        (Crypto.symbol == symbol.lower()) | (Crypto.symbol == symbol.upper())
    ).first()
    
    if not price_entry:
        print(f"Searched for {symbol}, but found nothing in the DB.")
        raise HTTPException