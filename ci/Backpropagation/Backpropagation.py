import math

import numpy as np
import matplotlib.pyplot as plt


def Funktiontolearn(x):
    return -math.cos(-x/2) + math.sin(4/(np.abs(x)+0.3))+ 0.2*x

def Fermi(x):
  return 1/(1+np.exp(-x))

def Fermi_derivative(x):
    return Fermi(x) * (1 - Fermi(x))

def feedForward(W1, b1, W2, b2, trainValues):
    X1 = np.dot(W1, trainValues.reshape(1, -1)) + b1
    X1 = Fermi(X1)

    X2 = np.dot(W2, X1) + b2
    return X1, X2

def mean_squared_error(y_true, y_pred):
    return np.mean((np.square(y_true - y_pred)**2))

def initialize_weights_and_biases(input_dim, hidden_dim, output_dim):
    W1 = np.random.uniform(-1, 1, (hidden_dim, input_dim)) # Gewichte für die verdeckte Schicht
    b1 = np.ones((hidden_dim, 1)) # Bias für die verdeckte Schicht

    W2 = np.random.uniform(-1, 1, (output_dim, hidden_dim)) # Gewichte für die Ausgabeschicht
    b2 = np.ones((output_dim, 1)) # Bias für die Ausgabeschicht

    return W1, b1, W2, b2

if __name__ == '__main__':
    trainValues = np.linspace(-10, 10, num=1001)
    trainPairs = np.array(list(zip(trainValues, [Funktiontolearn(x) for x in trainValues])))

    input_dim = 1
    hidden_dim = 20
    output_dim = 1
    learning_rate = 0.01
    error = 0
    W1, b1, W2, b2 = initialize_weights_and_biases(input_dim, hidden_dim, output_dim)
    for i in range(10):
        X1, X2 = feedForward(W1, b1, W2, b2, trainValues)

        #error = mean_squared_error(X2, trainPairs[:,1])
        #error = X2 - trainPairs[:,1]
        dW2 = np.dot(error, X1.T)
        db2 = np.sum(error, axis=1, keepdims=True)

        error = X2 - trainPairs[:,1]

        dX1 = np.dot(W2.T, mse) * Fermi_derivative(X1)
        dW1 = np.dot(dX1, trainValues.reshape(1, -1).T)
        db1 = np.sum(dX1, axis=1, keepdims=True)

        W1 -= learning_rate * dW1
        b1 -= learning_rate * db1
        W2 -= learning_rate * dW2
        b2 -= learning_rate * db2
        print("ERROR: ", mse)
    X1, X2 = feedForward(W1, b1, W2, b2, trainValues)

    print("true: ", X2)
    print("ERROR: ", trainPairs[:,1])







