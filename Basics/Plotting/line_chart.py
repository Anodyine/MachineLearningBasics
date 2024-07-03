import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 20, 1000)

y = np.sin(x) + 0.2 * x

plt.plot(x, y)
plt.xlabel('Input')
plt.ylabel('Output')
plt.title('My Plot')
plt.show()