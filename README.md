🚀 Crypto Data Pipeline
📌 Overview

This project is an end-to-end data pipeline that collects cryptocurrency market data from the CoinGecko API, stores it in a PostgreSQL database, and exposes it through a FastAPI service for querying and analytics.

🧠 Project Goal

The goal of this project is to demonstrate core concepts in Data Engineering:

Data ingestion from external APIs
Data storage using relational databases
Building REST APIs for data access
Structuring scalable data pipelines
🏗 Architecture
CoinGecko API 
      ↓
Python Ingestion Script
      ↓
PostgreSQL Database
      ↓
FastAPI Application
🛠 Tech Stack
Python
FastAPI
PostgreSQL
SQLAlchemy
Uvicorn
📂 Project Structure
crypto-data-pipeline/

├── app/
│   ├── main.py          # FastAPI entry point
│   ├── database.py      # Database connection
│   ├── models.py        # ORM models
│   └── crud.py          # API routes
│
├── pipeline/
│   └── ingest_crypto.py # Data ingestion script
│
├── requirements.txt
├── .gitignore
└── README.md
⚙️ How to Run the Project
1️⃣ Clone the repository
git clone <your-repo-url>
cd crypto-data-pipeline
2️⃣ Install dependencies
pip install -r requirements.txt
3️⃣ Run the ingestion pipeline
python pipeline/ingest_crypto.py

This will fetch crypto data from CoinGecko API and store it in PostgreSQL.

4️⃣ Start the API server
uvicorn app.main:app --reload
5️⃣ Open API docs
http://127.0.0.1:8000/docs
📡 API Endpoints
Endpoint	Description
GET /coins	Get all cryptocurrencies
GET /coins/{symbol}	Get specific coin by symbol
📊 Features
Fetch real-time cryptocurrency data
Store structured data in a relational database
Query data through REST API
Modular and scalable project structure
🚧 Future Improvements
Add data deduplication
Track historical price changes
Containerize using Docker
Schedule pipelines with Apache Airflow
🎯 What I Learned
Building ETL pipelines
Working with APIs and databases
Designing backend services
Structuring production-like projects
👨‍💻 Author

Built by [Your Name] as part of learning Data Engineering.
