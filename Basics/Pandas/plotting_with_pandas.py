import numpy as np
import pandas as pd
import urllib.request
import matplotlib.pyplot as plt
from pathlib import Path

csv = Path("sbux.csv")
if not csv.is_file():
    urllib.request.urlretrieve("https://raw.githubusercontent.com/lazyprogrammer/machine_learning_examples/master/tf2.0/sbux.csv", filename="sbux.csv")
    
df = pd.read_csv("sbux.csv")

# df['open'].hist()
# df['open'].plot()
df[['open', 'high', 'low', 'close']].plot.box()
plt.show()