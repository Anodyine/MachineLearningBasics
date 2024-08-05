import numpy as np
from typing import Optional
import math


class DecisionTreeNode:
    def __init__(self, featureIndex=None, left=None, right=None, *, value=None):
        self.featureIndex = featureIndex
        self.left = left
        self.right = right
        self.value = value
        
    def is_leaf_node(self):
        return self.value is not None
    # featureIndex: int = -1
    # yLabel: int = -1
    # left: Optional['DecisionTreeNode'] = None
    # right: Optional['DecisionTreeNode'] = None


class DecisionTree:
    def fit(self, X, y):
        numSamples, numFeatures = X.shape
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
            leftYValues = y[X[:,node.featureIndex] == 1]
            rightYValues = y[X[:,node.featureIndex] == 0]
            node.left = DecisionTreeNode()
            node.right = DecisionTreeNode()
            if (leftYValues.size > 0):
                node.left.value = round(np.mean(leftYValues))
            if (rightYValues.size > 0):
                node.right.value = round(np.mean(rightYValues))
            return
        
        lowestEntropyIndex = int(tuple(np.argwhere(featuresUsed == False)[0])[0])
        lowestEntropy = 1
        leftBranchEntropy = 1
        rightBranchEntropy = 1
        for i in range(numFeatures):
            if (featuresUsed[i] == False):
                branch1YValues = y[X[:,i] == 1]
                branch2YValues = y[X[:,i] == 0]
                branch1Entropy = self._calculateEntropy(branch1YValues)
                branch2Entropy = self._calculateEntropy(branch2YValues)
                totalBranchEntropy = branch1Entropy*branch1YValues.size/numSamples + branch2Entropy*branch2YValues.size/numSamples
                if (totalBranchEntropy < lowestEntropy):
                    lowestEntropy = totalBranchEntropy
                    lowestEntropyIndex = i
                    leftBranchEntropy = branch1Entropy
                    rightBranchEntropy = branch2Entropy
        
        node.featureIndex = lowestEntropyIndex
        featuresUsed[lowestEntropyIndex] = True
        
        if (lowestEntropy != 0):
            node.left = DecisionTreeNode()
            node.right = DecisionTreeNode()
            newX1 = X[X[:,lowestEntropyIndex] == 1, :]
            newX2 = X[X[:,lowestEntropyIndex] == 0, :]
            if (leftBranchEntropy > 0):
                self._findOptimalChildBranches(
                    node.left, 
                    newX1,
                    y[X[:,lowestEntropyIndex] == 1],
                    np.copy(featuresUsed))
            else:
                print(y[X[:,lowestEntropyIndex] == 1])
                node.left.value = 1
            if (rightBranchEntropy > 0):
                self._findOptimalChildBranches(
                    node.right, 
                    newX2,
                    y[X[:,lowestEntropyIndex] == 0],
                    np.copy(featuresUsed))
            else:
                print(y[X[:,lowestEntropyIndex] == 0])
                node.right.value = 0
        else:
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
    
    