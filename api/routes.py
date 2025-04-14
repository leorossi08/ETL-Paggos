from fastapi import APIRouter, HTTPException, Query
from datetime import datetime
from api.database import engine, data_table
from sqlalchemy import select

router = APIRouter()

@router.get("/data")
def get_data(
    start_date: datetime,
    end_date: datetime,
    fields: str = Query(None, description="Campos separados por vírgula: timestamp,wind_speed,power,ambient_temprature")
):
    valid_columns = {"timestamp", "wind_speed", "power", "ambient_temprature"}
    if fields:
        columns_requested = set([f.strip() for f in fields.split(",")])
        if not columns_requested.issubset(valid_columns):
            raise HTTPException(status_code=400, detail="Campos inválidos")
        selected_columns = [data_table.c[col] for col in columns_requested]
    else:
        selected_columns = list(data_table.c)
    
    # Desempacotando a lista de colunas
    query = select(*selected_columns).where(
        data_table.c.timestamp.between(start_date, end_date)
    )
    
    with engine.connect() as conn:
        result = conn.execute(query)
        # Usar row._mapping para converter cada linha em dicionário
        registros = [dict(row._mapping) for row in result]
    
    return {"data": registros}
