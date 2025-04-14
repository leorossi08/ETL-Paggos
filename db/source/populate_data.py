import random
from datetime import datetime, timedelta
import psycopg2
import os

def populate_data():
    conn = psycopg2.connect(
        dbname=os.getenv("POSTGRES_DB", "source_db"),
        user=os.getenv("POSTGRES_USER", "user"),
        password=os.getenv("POSTGRES_PASSWORD", "password"),
        host="localhost"  # Ajuste conforme necessário (pode ser o hostname do container)
    )
    cur = conn.cursor()
    
    start = datetime(2025, 4, 1, 0, 0, 0)
    end = start + timedelta(days=20)
    current = start
    
    while current <= end:
        wind_speed = round(random.uniform(0, 20), 2)
        power = round(random.uniform(0, 100), 2)
        ambient_temprature = round(random.uniform(10, 35), 2)
        
        cur.execute(
            """
            INSERT INTO data (timestamp, wind_speed, power, ambient_temprature)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (timestamp) DO NOTHING;
            """,
            (current, wind_speed, power, ambient_temprature)
        )
        current += timedelta(minutes=1)
    
    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    populate_data()
