import pandas as pd

def transform_data(data):
    df = pd.DataFrame(data)
    print("Dados extraídos (primeiras linhas):")
    print(df.head())
    if df.empty:
        return None
    
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df.set_index('timestamp', inplace=True)
    
    agg_funcs = {
        'wind_speed': ['mean', 'min', 'max', 'std'],
        'power': ['mean', 'min', 'max', 'std']
    }
    df_resampled = df.resample('10T').agg(agg_funcs)
    # Altera nomes das colunas (join com underline)
    df_resampled.columns = ['_'.join(col).strip() for col in df_resampled.columns.values]
    df_resampled.reset_index(inplace=True)
    
    print("Colunas do DataFrame transformado:")
    print(df_resampled.columns)
    print("DataFrame transformado (primeiras linhas):")
    print(df_resampled.head())
    
    return df_resampled

