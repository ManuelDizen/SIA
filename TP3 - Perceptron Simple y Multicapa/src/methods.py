import numpy


def simpleActivationFunc(value):
    return 1 if value >= 0 else -1


def simpleErrorFunc(trainingData, expectedOutput, w, activationFunc):
    i = 1
    limit = len(trainingData)
    error = 0
    for i in range(limit):
        O = numpy.inner(trainingData[i], w)
        error += ((expectedOutput[i] - activationFunc(O)) ** 2)
    return error / 2
