# etl/etl_runner.py
import sys
import argparse
from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data

def main(date_str):
    print(f"Iniciando o ETL para a data: {date_str}")
    
    # Extração
    data = extract_data(date_str)
    if not data:
        print("Nenhum dado extraído.")
        sys.exit(1)
    
    # Transformação
    transformed_data = transform_data(data)
    
    # Carga
    load_data(transformed_data)
    
    print("Processo ETL concluído com sucesso!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Script ETL para transferir dados da API para o banco de destino"
    )
    parser.add_argument("date", help="Data no formato YYYY-MM-DD para processamento")
    args = parser.parse_args()
    
    main(args.date)
