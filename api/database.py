from sqlalchemy import create_engine, MetaData, Table, Column, DateTime, Float
from config import DATABASE_URL

engine = create_engine(DATABASE_URL)
metadata = MetaData()

data_table = Table(
    'data', metadata,
    Column('timestamp', DateTime, primary_key=True),
    Column('wind_speed', Float),
    Column('power', Float),
    Column('ambient_temprature', Float)  # Use "ambient_temperature" se corrigir em todos os pontos
)

# Se preferir criar a tabela via código (opcional)
# metadata.create_all(engine)
