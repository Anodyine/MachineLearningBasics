import numpy as np
from sklearn.model_selection import train_test_split
from DecisionTree import DecisionTree
import pandas as pd
from PrettyPrint import PrettyPrintTree
from ModelEvaluation.DiscreteEvaluationHelpers import calculateSensitivity, calculateSpecitivity

df = pd.read_csv("decisionTreeTest.data")
X = df.values[:,0:5] # select columns
y = df.values[:,5] # select column
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
X_train = X
y_train = y
model = DecisionTree(max_depth=3)
model.fit(X_train, y_train)


def getChildren(node):
    children = []
    if node.left != None:
        children.append(node.left)
    if node.right != None:
        children.append(node.right)
    return children


def getLabel(node):
    if node.is_leaf_node():
        if node.value == 0:
            return "Did not get A"
        if node.value == 1:
            return "Got A"
    else:
        return df.columns[node.featureIndex]


print("The following decision tree was generated (true statements will cause prediction to take the left branch):")
pt = PrettyPrintTree(getChildren, getLabel)
pt(model.root)

y_train_pred = []
for i in range(X_train.shape[0]):
    y_train_pred.append(model.predict(X_train[i,:]))
    
# y_test_pred = []
# for i in range(X_test.shape[0]):
#     y_test_pred.append(model.predict(X_test[i,:]))
    
# print("Overfitting is confirmed by comparing performance on training data vs performance on testing data:")
trainedSensitivity = calculateSensitivity(y_train, y_train_pred)
print("Sensitivity with trained data: ", trainedSensitivity)
trainedSpecitivity = calculateSpecitivity(y_train, y_train_pred)
print("Specitivity with trained data: ", trainedSpecitivity)

# testSensitivity = calculateSensitivity(y_test, y_test_pred)
# print("Test sensitivity: ", testSensitivity)
# testSpecitivity = calculateSpecitivity(y_test, y_test_pred)
# print("Test specitivity: ", testSpecitivity)
