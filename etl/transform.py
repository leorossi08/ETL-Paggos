import pandas as pd

def transform_data(data):
    df = pd.DataFrame(data)
    print("Dados extraídos (primeiras linhas):")
    print(df.head())
    if df.empty:
        print("DataFrame está vazio após a extração.")
        return None
    
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df.set_index('timestamp', inplace=True)
    
    agg_funcs = {
        'wind_speed': ['mean', 'min', 'max', 'std'],
        'power': ['mean', 'min', 'max', 'std']
    }
    df_resampled = df.resample('10min').agg(agg_funcs)
    print("Após resample:")
    print(df_resampled.head())
    
    # Ajusta os nomes das colunas
    df_resampled.columns = ['_'.join(col).strip() for col in df_resampled.columns.values]
    df_resampled.reset_index(inplace=True)
    
    print("DataFrame transformado final:")
    print(df_resampled.head())
    return df_resampled
