import pandas as pd

def solution(df):
    df['name'] = df['name'].str.strip().str.title()
    #pd.to_date_time(df['date']) -> complex dtime to standartize time-object(datetime64) for mathematical equations(date differ between 2 dates - filtering)

    #dt.strftime('%Y-%m-%d') -> datetime64 to object/string wanted format of data (dt.strftime('%d-%m-%Y') - dt.strftime('%B %Y'))
    df['date'] = df['date'].str.strip()
    df['date'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m-%d')

    df = df.drop_duplicates(keep='first').reset_index(drop=True)

    df['value'] = df['value'].fillna(df['value'].mean())

    return df
    
