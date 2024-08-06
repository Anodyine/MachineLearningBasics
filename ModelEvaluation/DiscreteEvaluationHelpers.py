import numpy as np


def calculateSensitivity (y_actual, y_predicted):
    numPositives = np.count_nonzero(np.equal(y_predicted, 1))
    
    if (numPositives == 0):
        return None
    
    numTruePositives = np.count_nonzero(np.logical_and(
        np.equal(y_actual, 1), 
        np.equal(y_predicted, 1)))
    
    return numTruePositives/numPositives

def calculateSpecitivity (y_actual, y_predicted):
    numNegatives = np.count_nonzero(np.equal(y_predicted, 0))
    
    if (numNegatives == 0):
        return None
    
    numTrueNegatives = np.count_nonzero(np.logical_and(
        np.equal(y_actual, 0), 
        np.equal(y_predicted, 0)))
    
    return numTrueNegatives/numNegatives