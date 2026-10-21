import pandas as pd

def solution(df):
    df_clean = df.copy()

    thresh_col = len(df) * 0.5
    df_clean = df_clean.dropna(axis= 1, thresh=thresh_col) #thresh >= 2

    thresh_row = df_clean.shape[1] * 0.5
    df_clean = df_clean.dropna(axis= 0, thresh=thresh_row)

    for col in df_clean.columns:
        if df_clean[col].dtype != 'object':
            df_clean[col] = df_clean[col].fillna(df_clean[col].mean())
        else:
            df_clean[col] = df_clean[col].fillna(df_clean[col].mode()[0]) # most reccured value [0] - 0 x / 1 y => x
    
    return df_clean.reset_index(drop=True)