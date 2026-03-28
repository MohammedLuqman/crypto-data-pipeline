🚀 Crypto Data PipelineAn end-to-end data engineering project that collects real-time cryptocurrency market data, stores it in a relational database, and exposes it via a REST API.🧠 Project GoalThe goal of this project is to demonstrate core concepts in Data Engineering:Data Ingestion: Fetching live data from external APIs (CoinGecko).Data Storage: Designing a schema and managing a PostgreSQL database.API Development: Building a FastAPI service for data access.Pipeline Architecture: Structuring a scalable and modular codebase.🏗️ ArchitectureCoinGecko API ➡️ Python Ingestion Script ➡️ PostgreSQL Database ➡️ FastAPI Application📂 Project Structurecrypto-data-pipeline/
├── app/
│   ├── main.py          # FastAPI entry point
│   ├── database.py      # Database connection setup
│   ├── models.py        # SQLAlchemy ORM models
│   └── crud.py          # API routes & logic
├── pipeline/
│   └── ingest_crypto.py # Data ingestion script
├── .gitignore           # Files to ignore in Git
├── README.md            # Project documentation
└── requirements.txt     # Project dependencies
⚙️ How to Run the Project1️⃣ Setup EnvironmentFirst, clone the repository and install the necessary Python packages.# Clone the repository
git clone [https://github.com/MohammedLuqman/crypto-data-pipeline.git](https://github.com/MohammedLuqman/crypto-data-pipeline.git)

# Enter the directory
cd crypto-data-pipeline

# Install dependencies
pip install -r requirements.txt
2️⃣ Ingest DataRun the pipeline script to fetch the latest prices from CoinGecko and populate your database.python pipeline/ingest_crypto.py
3️⃣ Launch the APIStart the FastAPI server to view and query your data.uvicorn app.main:app --reload
4️⃣ Explore the DocumentationOnce the server is running, you can explore the interactive API docs:👉 Interactive Docs: http://127.0.0.1:8000/docs🚀 API EndpointsMethodEndpointDescriptionGET/coinsRetrieve all stored cryptocurrency recordsGET/coins/{symbol}Filter data for a specific coin (e.g., /coins/btc)🔮 Future Improvements[ ] Add data deduplication logic.[ ] Track historical price changes over time.[ ] Containerize the application using Docker.[ ] Schedule pipelines using Apache Airflow.👤 AuthorBuilt by Mohammed LuqmanData Engineering Enthusiast
