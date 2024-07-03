import numpy as np
import matplotlib.pyplot as plt

X = np.random.randn(10000)
plt.hist(X)
plt.show()

plt.hist(X, bins=50)
plt.show()

X = np.random.random(10000)
plt.hist(X, bins=50)
plt.show()

