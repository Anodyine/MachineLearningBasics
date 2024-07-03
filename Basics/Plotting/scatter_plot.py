import numpy as np
import matplotlib.pyplot as plt

X = np.random.randn(100,2)
print(X)
plt.scatter(X[:,0], X[:,1])
plt.show()

print(X[0,:])

X = np.random.randn(10,2)
print(X[:5])
print(X[:])
print(X[:,0].size)
print(X.shape)
print(X.shape[0])
X[:,1] += 3
print(X)
Y = np.zeros(200)
print(Y)

Y[:50] = 1
print(Y)
X = np.random.randn(200,2)
print(X[:,0].size)
print(X.shape)
print(X.shape[0])
X[:50] += 3
Y = np.zeros((200,3))
Y[:50] = [.5, 0, 0]
plt.scatter(X[:,0], X[:,1], c=Y)

plt.show()

X = np.random.randn(200,2)
X[:100] += 3
print(X)

fig, (axs1, axs2) = plt.subplots(2, 1, figsize = (6, 4))
X = np.random.randn(200,2)
X[:100] += 3
Y = np.zeros((200,3))
Y[:100] = [.5, 0, 0]
axs1.scatter(X[:,0],X[:,1], c=Y)
Y = np.full(200, '#0000FF')
Y[:100] = '#00FF00'
# Y = np.zeros(200)
# Y[:100] = 0.5
axs2.scatter(X[:,0],X[:,1], c=Y)
plt.show()
