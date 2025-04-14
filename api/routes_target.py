from fastapi import APIRouter, HTTPException, Query
import pandas as pd
import numpy as np
from sqlalchemy import create_engine, text
from config import TARGET_DATABASE_URL

router = APIRouter()

@router.get("/signal")
def get_signal_data(
    start_date: str = None,
    end_date: str = None
):
    """
    Retorna os dados da tabela 'signal'. Se forem fornecidas as datas de início
    e fim, filtra os resultados pelo intervalo de tempo.
    """
    try:
        engine = create_engine(TARGET_DATABASE_URL)
        
        if start_date and end_date:
            sql_query = text("""
                SELECT * FROM signal
                WHERE timestamp BETWEEN :start_date AND :end_date
                ORDER BY timestamp
            """)
            params = {"start_date": start_date, "end_date": end_date}
        else:
            sql_query = text("SELECT * FROM signal ORDER BY timestamp")
            params = {}
            
        df = pd.read_sql(sql_query, engine, params=params)
        
        # Substitui todos os valores não finitos (inf, -inf, NaN) por None
        df = df.where(np.isfinite(df), None)
        
        records = df.to_dict(orient="records")
        return {"data": records}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao consultar os dados: {str(e)}")
