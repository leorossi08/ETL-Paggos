from pydantic import BaseModel
from datetime import datetime

class DataRecord(BaseModel):
    timestamp: datetime
    wind_speed: float
    power: float
    ambient_temperature: float
