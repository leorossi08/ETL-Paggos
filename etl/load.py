from sqlalchemy import create_engine, text
import pandas as pd
from config import TARGET_DATABASE_URL

def load_data(df):
    if df is None or df.empty:
        print("Nenhum dado para carregar.")
        return
    
    engine = create_engine(TARGET_DATABASE_URL)
    print("Dados a serem carregados no banco destino:")
    print(df.head())
    try:
        df.to_sql('signal', engine, if_exists='append', index=False)
        print("Dados carregados com sucesso no banco de destino!")
        
        # Após a inserção, verifique a contagem de linhas
        with engine.connect() as conn:
            result = conn.execute(text("SELECT COUNT(*) FROM signal"))
            count = result.scalar()
            print(f"Número total de registros em 'signal': {count}")
            
    except Exception as e:
        print(f"Erro ao carregar dados: {e}")
