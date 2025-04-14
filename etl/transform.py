import pandas as pd

def transform_data(data):
    df = pd.DataFrame(data)
    if df.empty:
        return None
    
    # Converter a coluna de timestamp e definir índice
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df.set_index('timestamp', inplace=True)
    
    # Agregação em janelas de 10 minutos
    agg_funcs = {
        'wind_speed': ['mean', 'min', 'max', 'std'],
        'power': ['mean', 'min', 'max', 'std']
    }
    df_resampled = df.resample('10T').agg(agg_funcs)
    
    # Ajustar nomes das colunas para facilitar a carga
    df_resampled.columns = ['_'.join(col).strip() for col in df_resampled.columns.values]
    df_resampled.reset_index(inplace=True)
    
    return df_resampled
