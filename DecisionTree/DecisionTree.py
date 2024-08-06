import numpy as np
import math


class DecisionTreeNode:
    def __init__(self, featureIndex=None, left=None, right=None, *, value=None):
        self.featureIndex = featureIndex
        self.left = left
        self.right = right
        self.value = value
        
    def is_leaf_node(self):
        return self.value is not None


class DecisionTree:
    def fit(self, X, y):
        numFeatures = X.shape[1]
        featuresUsed = np.zeros(numFeatures, bool)
        self.root = DecisionTreeNode()
        self._findOptimalChildBranches(self.root, X, y, featuresUsed)
        
    def predict(self, X):
        current_node = self.root
        while current_node.is_leaf_node() == False:
            if (X[current_node.featureIndex] == 1):
                current_node = current_node.left
            else:
                current_node = current_node.right
        
        return current_node.value
            
        
    def _findOptimalChildBranches(self, node: DecisionTreeNode, X, y, featuresUsed):
        numSamples, numFeatures = X.shape
        
        if featuresUsed[featuresUsed == False].size < 2:
            node.featureIndex = int(tuple(np.argwhere(featuresUsed == False)[0])[0])
            self._createEndingBranch(node, X, y)
            return
        
        lowestEntropyIndex = int(tuple(np.argwhere(featuresUsed == False)[0])[0])
        lowestEntropy = 1
        lowestLeftBranchEntropy = 1
        lowestRightBranchEntropy = 1
        for i in range(numFeatures):
            if (featuresUsed[i] == False):
                leftBranchYValues = y[X[:,i] == 1]
                rightBranchYValues = y[X[:,i] == 0]
                leftBranchEntropy = self._calculateEntropy(leftBranchYValues)
                rightBranchEntropy = self._calculateEntropy(rightBranchYValues)
                totalBranchEntropy = leftBranchEntropy*leftBranchYValues.size/numSamples + rightBranchEntropy*rightBranchYValues.size/numSamples
                if (totalBranchEntropy < lowestEntropy):
                    lowestEntropy = totalBranchEntropy
                    lowestEntropyIndex = i
                    lowestLeftBranchEntropy = leftBranchEntropy
                    lowestRightBranchEntropy = rightBranchEntropy
        
        node.featureIndex = lowestEntropyIndex
        featuresUsed[lowestEntropyIndex] = True
        
        if (lowestEntropy != 0):
            node.left = DecisionTreeNode()
            node.right = DecisionTreeNode()
            if (lowestLeftBranchEntropy > 0):
                self._findOptimalChildBranches(
                    node.left, 
                    X[X[:,lowestEntropyIndex] == 1, :],
                    y[X[:,lowestEntropyIndex] == 1],
                    np.copy(featuresUsed))
            else:
                node.left.value = y[X[:,lowestEntropyIndex] == 1][0]
            if (lowestRightBranchEntropy > 0):
                self._findOptimalChildBranches(
                    node.right, 
                    X[X[:,lowestEntropyIndex] == 0, :],
                    y[X[:,lowestEntropyIndex] == 0],
                    np.copy(featuresUsed))
            else:
                node.right.value = y[X[:,lowestEntropyIndex] == 0][0]
        else:
            self._createEndingBranch(node, X, y)
        
        return 
    
    def _createEndingBranch (self, node, X, y):
        leftYValues = y[X[:,node.featureIndex] == 1]
        rightYValues = y[X[:,node.featureIndex] == 0]
        node.left = DecisionTreeNode()
        node.right = DecisionTreeNode()
        if (leftYValues.size > 0):
            node.left.value = round(np.mean(leftYValues))
        if (rightYValues.size > 0):
            node.right.value = round(np.mean(rightYValues)) 
        return
        
    
    def _calculateEntropy(self, y):
        if y.size <= 0:
            return 0
        
        numOnes = np.count_nonzero(y)
        numZeros = y.size - numOnes 
        p1 = numOnes/(y.size)
        p2 = numZeros/(y.size)

        if (p1 == 0 or p2 == 0):
            return 0
        
        return -(p1*math.log(p1, 2) + p2*math.log(p2, 2))
    
    