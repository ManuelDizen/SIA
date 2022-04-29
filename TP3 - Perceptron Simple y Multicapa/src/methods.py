import numpy

betaParameter = 0.5

def simpleActivationFunc(value):
    return 1 if value >= 0 else -1

def linearActivationFunc(value):
    return value

def sigmoidTanhActivationFunc(value):
    return numpy.tanh(value * betaParameter)

def sigmoidLogisticActivationFunc(value):
    return 1 / (1 + numpy.exp(-2*betaParameter*value))

def simpleErrorFunc(trainingData, expectedOutput, w, activationFunc):
    i = 1
    limit = len(trainingData)
    error = 0
    for i in range(0, limit):
        actualOut = numpy.inner(trainingData[i], w)
        error += ((expectedOutput[i] - activationFunc(actualOut)) ** 2)
    return error / 2
