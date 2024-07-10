import pandas as pd
import urllib.request
from pathlib import Path

csv = Path("sbux.csv")
if not csv.is_file():
    urllib.request.urlretrieve("https://raw.githubusercontent.com/lazyprogrammer/machine_learning_examples/master/tf2.0/sbux.csv", filename="sbux.csv")
    
df = pd.read_csv("sbux.csv")

print(type(df))

print(df.head())
print(df.head(10))
print(df.tail(10))
print(df.info())

