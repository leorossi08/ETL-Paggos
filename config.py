from dotenv import load_dotenv
load_dotenv()

import os

# Conexão com o banco Fonte (usado na API)
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@db_source/source_db")

# Conexão com o banco Alvo (usado no ETL)
TARGET_DATABASE_URL = os.getenv("TARGET_DATABASE_URL", "postgresql://user:password@db_target/target_db")

# URL da API para o processo de ETL
API_URL = os.getenv("API_URL", "http://localhost:8000")
