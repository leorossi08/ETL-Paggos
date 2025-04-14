import sys
import argparse
import time
import httpx

from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data
from config import API_URL

def wait_for_api(max_retries=10, delay=5):
    for attempt in range(max_retries):
        try:
            response = httpx.get(f"{API_URL}/docs", timeout=5)
            if response.status_code == 200:
                print("API disponível!")
                return True
        except Exception as e:
            print(f"Tentativa {attempt+1}: API indisponível ({e}). Aguardando {delay} segundos...")
        time.sleep(delay)
    return False

def main(date_str):
    if not wait_for_api():
        print("A API não ficou disponível em tempo hábil. Encerrando o ETL.")
        sys.exit(1)
    
    print(f"Iniciando o ETL para a data: {date_str}")
    data = extract_data(date_str)
    if not data:
        print("Nenhum dado extraído.")
        sys.exit(1)
    
    transformed_data = transform_data(data)
    load_data(transformed_data)
    print("Processo ETL concluído com sucesso!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Script ETL para transferir dados da API para o banco de destino"
    )
    parser.add_argument("date", help="Data no formato YYYY-MM-DD para processamento")
    args = parser.parse_args()
    
    main(args.date)
