import numpy as np
import matplotlib.pyplot as plt

X = 2*np.random.random((1000,2)) - 1
print(X)

def getColor (x):
    return 50 if (x[0] > 0 and x[1] < 0) or (x[0] < 0 and x[1] > 0) else 0
getColors = np.vectorize(getColor, signature='(n)->()')

Y = getColors(X)

plt.scatter(X[:,0], X[:,1], c=Y)
plt.show()

