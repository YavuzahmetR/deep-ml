import pandas as pd

def solution(df):
    df = df.pivot_table(index='date', columns='product', values='sales', aggfunc='sum', fill_value=0).reset_index()

    df = pd.melt(frame=df, id_vars='date', var_name='product', value_name='sales')

    df = df.sort_values(by=['date','product']).reset_index(drop=True)

    return  df