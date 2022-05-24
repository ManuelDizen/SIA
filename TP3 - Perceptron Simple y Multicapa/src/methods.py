import numpy

betaParameter = 1
maxVal = 99.3834
minVal = 0.1558

def simpleActivationFunc(value):
    return 1 if value >= 0 else -1

def linearActivationFunc(value):
    return value

def sigmoidTanhActivationFunc(value):
    return numpy.tanh(value * betaParameter)

def sigmoidTanhActivationFuncDerivative(value):
    return betaParameter * (1 - value * value)

def sigmoidLogisticActivationFunc(value):
    return 1 / (1 + numpy.exp(-2*betaParameter*value))

def simpleErrorFunc(trainingData, expectedOutput, w, activationFunc):
    limit = len(trainingData)
    error = 0
    for i in range(limit):
        actualOut = numpy.dot(trainingData[i], w)
        error += ((expectedOutput[i] - activationFunc(actualOut)) ** 2)
    return error / 2

def denormalizeErrorFunc(trainingData, expectedOutput, w, activationFunc):
    limit = len(trainingData)


    error = 0
    for i in range(limit):
        aux = activationFunc(numpy.dot(trainingData[i], w))
        actualOut = ((aux + 1)*(maxVal-minVal)/2)+minVal
        expected = ((expectedOutput[i]+1)*(maxVal-minVal)/2)+minVal
        error += ((expected - actualOut) ** 2)
    return error / 2

def normalize(output):
    outData = numpy.zeros(len(output))

    for i in range(len(output)):
        current = (2*(output[i] - minVal)/(maxVal - minVal))-1
        outData[i] = current

    return outData

def calcAccuracy(data, output, w, activationFunc):
    count = 0
    delta = 0.25
    for i in range(len(data)):
        aux = activationFunc(numpy.dot(data[i], w))
        current = ((aux + 1)*(maxVal-minVal)/2)+minVal
        #  print(f'current = {current}, output = {output[i]}')
        if abs(output[i] - current) < delta:
            count += 1


    return count/len(data)
