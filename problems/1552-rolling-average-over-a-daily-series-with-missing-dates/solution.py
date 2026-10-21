import pandas as pd
import numpy as np


def solution(df, window):
    # TODO: complete the daily calendar, keep NaN for missing days, trailing calendar-window mean
    df['date'] = pd.to_datetime(df['date'])
    #missing day filling day-based and other missing columns sets NaN
    df = df.set_index('date').sort_index().asfreq('D')
    #2"D" for time-based window
    df['rolling_mean'] = df['value'].rolling(f"{window}D").mean()
    #date index goes to column side
    return df.reset_index()

