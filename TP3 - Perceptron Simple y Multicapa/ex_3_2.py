import numpy as np
from src.utils import parseNumbers
from src.layer import Layer
from src.multilayer_perceptron import MultilayerPerceptron
from src.methods import sigmoidTanhActivationFunc, \
    sigmoidTanhActivationFuncDerivative
from src.utils import plotError

numbers = parseNumbers("TP3-ej3-mapa-de-pixeles-digitos-decimales.txt")
expectedOutput = [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1]

layer1 = Layer(16, 35)
layer2 = Layer(10, 16)
layer3 = Layer(1, 10)

k = 5

partitionSize = numbers.shape[0] // k
indexes = np.arange(0, numbers.shape[0], dtype=int)
trainSets = []
testSets = []

for i in range(k):
    test = indexes[i * partitionSize: (i + 1) * partitionSize]
    before = indexes[0: i * partitionSize]
    after = indexes[(i + 1) * partitionSize:]
    train = np.concatenate((before, after))
    trainSets.append(train)
    testSets.append(test)

trainData = np.take(numbers, trainSets, axis=0)
expectedTrain = np.take(expectedOutput, trainSets, axis=0)

testData = np.take(numbers, testSets, axis=0)
expectedTest = np.take(expectedOutput, testSets, axis=0)


errors = np.zeros(100)
for j in range(len(trainData)):
    perceptron = MultilayerPerceptron([layer1, layer2, layer3], sigmoidTanhActivationFunc,
                                      sigmoidTanhActivationFuncDerivative,
                                      0.1)
    auxArray = perceptron.algorithm(trainData[j], expectedTrain[j], 100)
    for i in range(len(errors)):
        aux = errors[i]
        errors[i] = (auxArray[i] + errors[i])/2

plotError(errors)


