import numpy as np


class Layer:

    def __init__(self, inputCount, inputSize):
        self.weights = 2 * np.random.random((inputSize, inputCount)) - 1
        self.bias = 2 * np.random.random(inputCount) - 1
        self.derivativeError = None

    def error(self, inherited_error, derivative, activation):
        self.derivativeError = inherited_error * derivative(activation)

    def delta(self, lastActivation, learnRate):
        activationMatrix = np.matrix(lastActivation)
        errorMatrix = np.matrix(self.derivativeError)
        self.weights += learnRate * activationMatrix.T.dot(errorMatrix)
        self.bias += learnRate * self.derivativeError

    def activate(self, feed, learn_f):
        return learn_f(np.dot(feed, self.weights) + self.bias)

    def __str__(self):
        return str(self.weights)
