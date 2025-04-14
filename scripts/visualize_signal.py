import pandas as pd
from sqlalchemy import create_engine

# Conexão com o banco alvo. Aqui usamos a porta 5433 conforme definido no docker-compose.
engine = create_engine("postgresql://user:password@localhost:5433/target_db")

query = "SELECT * FROM signal;"
df = pd.read_sql(query, engine)

print(df)
