import pandas as pd

def solution(df):
    filtered_df = df[df['status'] == 'completed']

    region_filter = filtered_df.groupby('region')['amount'].sum().sort_values(ascending=False).reset_index().head(10)

    return region_filter


     









    