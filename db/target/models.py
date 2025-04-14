from sqlalchemy import create_engine, Column, Integer, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from config import TARGET_DATABASE_URL

engine = create_engine(TARGET_DATABASE_URL)
Base = declarative_base()

class Signal(Base):
    __tablename__ = 'signal'
    id = Column(Integer, primary_key=True, autoincrement=True)
    timestamp = Column(DateTime)  # Representa o início da janela agregada
    wind_speed_mean = Column(Float)
    wind_speed_min = Column(Float)
    wind_speed_max = Column(Float)
    wind_speed_std = Column(Float)
    power_mean = Column(Float)
    power_min = Column(Float)
    power_max = Column(Float)
    power_std = Column(Float)

if __name__ == "__main__":
    Base.metadata.drop_all(engine)   # Opcional: para remover o esquema antigo
    Base.metadata.create_all(engine)
