from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
import os
from config import TARGET_DATABASE_URL

engine = create_engine(TARGET_DATABASE_URL)
Base = declarative_base()

class Signal(Base):
    __tablename__ = 'signal'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    data = Column(DateTime)
    timestamp = Column(DateTime)
    signal_id = Column(Integer)
    value = Column(Float)

if __name__ == "__main__":
    Base.metadata.create_all(engine)
