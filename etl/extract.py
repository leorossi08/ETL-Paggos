import httpx
from datetime import datetime, timedelta
from config import API_URL

def extract_data(date_str):
    try:
        start_dt = datetime.fromisoformat(date_str)
    except ValueError:
        print("Formato de data inválido. Utilize YYYY-MM-DD")
        return None
    
    end_dt = start_dt + timedelta(days=1)
    
    params = {
        "start_date": start_dt.isoformat(),
        "end_date": end_dt.isoformat(),
        "fields": "timestamp,wind_speed,power,ambient_temperature"
    }
    
    try:
        response = httpx.get(f"{API_URL}/data", params=params)
        response.raise_for_status()
        result = response.json()
        return result.get("data")
    except Exception as e:
        print(f"Erro ao extrair dados: {e}")
        return None
