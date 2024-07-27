import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets
import matplotlib.pyplot as plt
from LinearRegression import LinearRegression

def meanSquaredError(y_test, predictions):
    return np.mean((predictions - y_test)**2)

X, y = datasets.make_regression(n_samples=200, n_features=5, n_informative=1, noise=10, bias=200)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
fig = plt.figure(figsize=(8,6))

colors = ['maroon', 'sienna', 'steelblue', 'darkolivegreen','purple']
for i in range(X.shape[1]):
    plt.scatter(X[:,i], y, color = colors[i], marker = "o", s = 30)

model = LinearRegression(learningRate = 0.005, numIterations = 10000)

model.fit(X_train, y_train)
preditions = model.predictFeatures(X_test)
colors = ['red', 'orange',  'lightskyblue', 'limegreen','violet']
for i in range(X.shape[1]):
    print("Error of " + colors[i] + ": " + str(meanSquaredError(y_test, preditions[:,i])))
    plt.plot(X_test[:,i], preditions[:,i], color=colors[i], linewidth = 2)

plt.show()