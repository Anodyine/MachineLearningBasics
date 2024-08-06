import numpy as np
from sklearn.model_selection import train_test_split
from DecisionTree import DecisionTree
import pandas as pd
from PrettyPrint import PrettyPrintTree

df = pd.read_csv("decisionTreeTest.data")
X = df.values[:,0:5] # select columns
y = df.values[:,5] # select column
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4)
model = DecisionTree()
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
        return df.columns[node.featureIndex] + " == 1"


print("The following decision tree was generated (true statements will cause prediction to take the left branch):")
pt = PrettyPrintTree(getChildren, getLabel)
pt(model.root)

print("Overfitting is confirmed by comparing performance on training data vs performance on testing data:")
print("Trained Results:")
for i in range(X_train.shape[0]):
    print(model.predict(X_train[i,:]) == y_train[i])
    
print("Test Results:")
for i in range(X_test.shape[0]):
    print(model.predict(X_test[i,:]) == y_test[i])

