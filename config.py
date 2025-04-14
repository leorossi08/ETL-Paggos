import os

# String de conexão com o banco de dados Fonte (utilizado na API)
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@db_source/source_db")

# String de conexão com o banco de dados Alvo (utilizado no ETL)
TARGET_DATABASE_URL = os.getenv("TARGET_DATABASE_URL", "postgresql://user:password@db_target/target_db")

# URL da API para o processo de ETL
API_URL = os.getenv("API_URL", "http://localhost:8000")
