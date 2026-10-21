import pandas as pd


def solution(df):
    # TODO: bucket scores, count per (grade, bucket), cumulative percentage within grade
    df['bucket'] = (df['score'] // 10) * 10

    summary_df = df.groupby(['grade','bucket']).size().reset_index(name='count')
    
    summary_df['cum_pct'] = (summary_df.groupby('grade')['count'].transform('cumsum') / summary_df.groupby('grade')['count'].transform('sum') * 100).round(2)

    return summary_df

