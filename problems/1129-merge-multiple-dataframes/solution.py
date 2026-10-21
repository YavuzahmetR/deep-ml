import pandas as pd

def solution(df1, df2, df3):
    #pd.merge(t1, t2, on='', how='')
    name_dept_df = pd.merge(df1, df2, on='emp_id', how='inner')

    salary_name_dept_df = pd.merge(name_dept_df, df3, on='emp_id', how='left').reset_index(drop=True)

    return salary_name_dept_df
