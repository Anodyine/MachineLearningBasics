import numpy as np

class LinearRegression:
    def __init__(self, learningRate = 0.001, numIterations=1000):
        self.learningRate = learningRate
        self.numIterations = numIterations
        self.weights = None
        self.bias = None
        
    def fit(self, X, y):
        numSamples, numFeatures = X.shape
        self.weights = np.zeros(numFeatures)
        self.bias = np.zeros(numFeatures)
        
        for i in range(numFeatures):
            for _ in range(self.numIterations):
                yPredicted = np.dot(X[:,i], self.weights[i]) + self.bias[i]
                
                dw = 1/numSamples*np.dot(X[:,i].T, (yPredicted - y))
                db = 1/numSamples*np.sum(yPredicted - y)
                
                self.weights[i] = self.weights[i] - self.learningRate * dw
                self.bias[i] = self.bias[i] - self.learningRate * db
        
    def predictFeatures(self, X):
        numSamples, numFeatures = X.shape
        y = np.zeros(X.shape)
        for i in range(numFeatures):
            y[:,i] = np.dot(X[:,i], self.weights[i]) + self.bias[i]
            
        return y
    