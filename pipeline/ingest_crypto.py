import requests
from app.database import SessionLocal  # Or wherever your session is defined
from app.models import Crypto
from datetime import datetime

URL = "https://api.coingecko.com/api/v3/coins/markets"
params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 10,
    "page": 1
}

response = requests.get(URL, params=params)
data = response.json()

db = SessionLocal()

try:
    for coin in data:
        new_coin = Crypto(
            coin_name=coin["name"],
            symbol=coin["symbol"],
            price_usd=coin["current_price"],
            market_cap=coin["market_cap"],
            timestamp=datetime.utcnow()
        )
        db.add(new_coin)
    
    db.commit()
    print("Successfully ingested crypto data!")
except Exception as e:
    print(f"Error occurred: {e}")
    db.rollback()
finally:
    db.close()