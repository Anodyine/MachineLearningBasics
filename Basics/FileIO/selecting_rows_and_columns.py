import numpy as np
import pandas as pd
import urllib.request
from pathlib import Path

csv = Path("sbux.csv")
if not csv.is_file():
    urllib.request.urlretrieve("https://raw.githubusercontent.com/lazyprogrammer/machine_learning_examples/master/tf2.0/sbux.csv", filename="sbux.csv")
    
df = pd.read_csv("sbux.csv")


print(df.columns)

df.columns = ['date', 'open', 'high', 'low', 'close', 'volume', 'name']
print(df.columns)
print(type(df['open']))
print(df['open'])
print(type(df[['open', 'close']]))
print(df[['open','close']])
print(df.loc[0])
print(df.iloc[0])

df2 = pd.read_csv('sbux.csv', index_col='date')

print(df2.loc['2013-02-08'])

print(df[df['open'] > 64])
print(type(df['name'] != 'SBUX'))
print(df['name'] != 'SBUX')

A = np.arange(10)

print (type(A))
print(A)

#where
print (type(A[A % 2 == 0]))
print (A[A % 2 == 0])

#map
print(type(A * 2))
print(A * 2)

print(df.values)

A = df[['open', 'close']].values
print(type(A))
print(A)