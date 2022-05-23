import numpy as np
from src.utils import parseNumbers
from src.layer import Layer
from src.multilayer_perceptron import MultilayerPerceptron
from src.methods import sigmoidTanhActivationFunc, \
    sigmoidTanhActivationFuncDerivative
from src.utils import plotError, plotErrorDouble, plotAccuracies, accuracy

numbers = parseNumbers("TP3-ej3-mapa-de-pixeles-digitos-decimales.txt")
expectedOutput = [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1]

layer1 = Layer(10, 35)
layer2 = Layer(1, 10)

k = 5

partitionSize = numbers.shape[0] // k
indexes = np.arange(0, numbers.shape[0], dtype=int)
trainSets = []
testSet = []
expectedTrain = []
expectedTest = []

chosenK = 0
for i in range(k):
    if k != chosenK:
        auxTrain = numbers[i*partitionSize:partitionSize+(i*partitionSize)]
        trainSets.append(auxTrain)
        auxExpectedTrain = expectedOutput[i*partitionSize:partitionSize+(i*partitionSize)]
        expectedTrain.append(auxExpectedTrain)

testSet = numbers[chosenK*partitionSize:(chosenK+1)*partitionSize]
expectedTest = expectedOutput[chosenK*partitionSize:(chosenK+1)*partitionSize]

iterations = 400
errors = np.zeros(iterations)
estimationsTrain = np.zeros(0)
estimationsTest = np.zeros(0)
accuracyTrain = np.zeros(iterations)
accuracyTest = np.zeros(iterations)

expectedTrainAcc = np.zeros((k-1)*partitionSize)
expectedTestAcc = np.zeros(partitionSize)

perceptron = MultilayerPerceptron([layer1, layer2], sigmoidTanhActivationFunc,
                                  sigmoidTanhActivationFuncDerivative,
                                  0.1)

arrayTestAccuracies = [[0], [0], [0], [0], [0], [0]]
arrayTrainErrors = [[0], [0], [0], [0], [0], [0]]
errorTest = np.zeros(iterations)
for j in range(len(trainSets)):
    auxArray, auxTrainAcc, useless, auxErrorTest = perceptron.algorithm(trainSets[j], expectedTrain[j], testSet, expectedTestAcc, iterations)
    estimationsTrain = np.append(estimationsTrain, perceptron.estimations(trainSets[j]))
    auxAcc = accuracy(perceptron.estimations(testSet), expectedTest)
    arrayTestAccuracies[j] = auxTrainAcc
    arrayTrainErrors[j] = auxArray
    for i in range(len(errors)):
        errors[i] = auxArray[i] + errors[i]
        errorTest[i] = auxErrorTest[i] + errorTest[i]
        accuracyTrain[i] = auxTrainAcc[i] + accuracyTrain[i]
        accuracyTest[i] = auxAcc


for i in range(len(errors)):
    errors[i] = errors[i]/len(trainSets)
    errorTest[i] = errorTest[i] / len(trainSets)
    accuracyTrain[i] = accuracyTrain[i] / len(trainSets)


#plotErrorDouble(errors, errorTest)
plotAccuracies(arrayTestAccuracies, accuracyTest)
