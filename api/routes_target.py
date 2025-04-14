from fastapi import APIRouter, HTTPException
import pandas as pd
import numpy as np
from sqlalchemy import create_engine, text
from config import TARGET_DATABASE_URL

router = APIRouter()

@router.get("/signal")
def get_signal_data():
    try:
        engine = create_engine(TARGET_DATABASE_URL)
        query = text("SELECT * FROM signal ORDER BY timestamp;")
        df = pd.read_sql(query, engine)
        
        # Substitui inf, -inf e NaN por None para garantir compatibilidade com JSON.
        df = df.replace([np.inf, -np.inf, np.nan], None)
        
        # Alternativamente, forçamos a conversão usando applymap:
        df = df.applymap(lambda x: None if (isinstance(x, float) and (np.isnan(x) or np.isinf(x))) else x)
        
        records = df.to_dict(orient="records")
        return {"data": records}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao consultar os dados: {str(e)}")
