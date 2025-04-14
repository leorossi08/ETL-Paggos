from sqlalchemy import create_engine, MetaData, Table, Column, DateTime, Float
import os
from config import DATABASE_URL

engine = create_engine(DATABASE_URL)
metadata = MetaData()

data_table = Table(
    'data', metadata,
    Column('timestamp', DateTime, primary_key=True),
    Column('wind_speed', Float),
    Column('power', Float),
    Column('ambient_temprature', Float)
)

# Se desejar criar a tabela via código (opcional, visto que o container pode executar o SQL de inicialização)
# metadata.create_all(engine)
