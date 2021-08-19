import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('hindalcocsv.csv',index_col ='datetime')

df.tail()

df['30_MA_Close'] = df['close'].rolling(window=30).mean()
#calculating 20 days rolling standard devtaion
df['20_std_Close'] = df['close'].rolling(window=20).std()

df.head(31)

# Upper Bollinger Bands = Mean+2*SD
# Lower Bollinger Bands = Mean-2*SD
df['Upper'] = df['30_MA_Close'] + 2*df['20_std_Close']
df['Lower'] = df['30_MA_Close'] - 2*df['20_std_Close']

df.head(31)

df[['close','30_MA_Close','Upper','Lower']].plot(figsize=(15,5))
