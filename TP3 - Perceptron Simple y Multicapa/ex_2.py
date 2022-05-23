import numpy

from src.utils import *
from src.perceptron import *
from src.methods import *
import matplotlib.pyplot as plt


trainData = parse_training_data('TP3-ej2-Conjunto-entrenamiento.txt')

output = parseOutputData('TP3-ej2-Salida-deseada.txt')
outputData = normalize(output)
trainData = appendThreshold(trainData)

#outputData = appendThreshold(outputData)

#print(f'Train = {trainData}\noutput = {outputData}')





str = "point1"

if str == "point1":
    linear_perceptron = perceptron(trainData, output, 0.01, linearActivationFunc, simpleErrorFunc, True)
    tanh_perceptron = perceptron(trainData, outputData, 0.01, sigmoidTanhActivationFunc, simpleErrorFunc, False, sigmoidTanhActivationFuncDerivative)
    #  logistic_perceptron = perceptron(trainData, outputData, 0.01, sigmoidLogisticActivationFunc, simpleErrorFunc, False, sigmoidLogisticActivationFuncDerivative)
    linear_perceptron.algorithm2(1000)
    tanh_perceptron.algorithm2(1000)
    #  logistic_perceptron.algorithm2(1000)
    print(f'Linear: min w = {linear_perceptron.w_min} and min error = {linear_perceptron.error_min}')
    print(f'Tanh: min w = {tanh_perceptron.w_min} and min error = {tanh_perceptron.error_min}')
    #  print(f'Logistic: min w = {logistic_perceptron.w_min} and min error = {logistic_perceptron.error_min}')
    perceptrons = [linear_perceptron, tanh_perceptron]
    for p in perceptrons:
        x_axis_values = range(1000)
        y_axis_values = p.errors
        plt.plot(x_axis_values, y_axis_values, label=p)
    plt.title(f'Error para cada iteración')
    plt.xlabel("Iteraciones")
    plt.ylabel("Error")
    plt.legend()
    plt.show()
    for p in perceptrons:
        learnrates = [0.1, 0.05, 0.01, 0.001]
        for i in learnrates:
            p.error_min = numpy.inf
            p.w_min = numpy.zeros(len(trainData[0]))
            p.learnRate = i
            p.algorithm2(1000)
            x_axis_values = range(1000)
            y_axis_values = p.min_errors
            plt.plot(x_axis_values, y_axis_values, label=f'n = {i}')
        plt.title(f'Error mínimo \nen {p}')
        plt.xlabel("Iteraciones")
        plt.ylabel("Error mínimo")
        plt.legend()
        plt.show()

        for i in learnrates:
            p.error_min = numpy.inf
            p.w_min = numpy.zeros(len(trainData[0]))
            p.learnRate = i
            p.algorithm2(1000)
            x_axis_values = range(1000)
            y_axis_values = p.errors
            plt.plot(x_axis_values, y_axis_values, label=f'n = {i}')
        plt.title(f'Error \nen {p}')
        plt.xlabel("Iteraciones")
        plt.ylabel("Error")
        plt.legend()
        plt.show()


elif str == "point2":
    perceptron = perceptron(trainData, outputData, 0.001, sigmoidTanhActivationFunc, simpleErrorFunc, False,
                            sigmoidTanhActivationFuncDerivative)
    k = 100
    trainSet = trainData[0:int(k)]
    outputSet = outputData[0:int(k)]
    testSet = trainData[int(k):len(trainData)]
    expectedOutput = outputData[int(k):len(trainData)]
    perceptron.trainingData = trainSet
    perceptron.expectedOutput = outputSet
    perceptron.w_min = numpy.zeros(len(trainSet[0]))
    perceptron.error_min = numpy.inf
    perceptron.algorithm2(100)
    err = simpleErrorFunc(testSet, expectedOutput, perceptron.w_min, sigmoidTanhActivationFunc) / len(testSet)
    print(f'k = {k}, error = {err}')
    accuracy = numpy.zeros(100)
    accuracyTraining = numpy.zeros(100)
    for i in range(100):
        perceptron.algorithm2(100)
        current = simpleErrorFunc(testSet, expectedOutput, perceptron.w_min, sigmoidTanhActivationFunc) / len(testSet)
        accuracy[i] = 1 / current
        current = simpleErrorFunc(trainSet, outputSet, perceptron.w_min, sigmoidTanhActivationFunc) / len(trainSet)
        accuracyTraining[i] = 1 / current
    x_axis_values = range(100)
    y_axis_values = accuracyTraining
    plt.plot(x_axis_values, y_axis_values, label="Entrenamiento")
    y_axis_values = accuracy
    plt.plot(x_axis_values, y_axis_values, label="Test")
    plt.title(f'Precisión vs época para k = {k}')
    plt.xlabel("Época")
    plt.ylabel("Precisión")
    plt.legend()
    plt.show()
    plt.plot(x_axis_values, y_axis_values)
    plt.title(f'Precisión vs época para k = {k}')
    plt.xlabel("Época")
    plt.ylabel("Precisión")
    plt.show()

    limInf = 0
    limSup = len(trainData) / 10
    accuracy = numpy.zeros(10)
    i = 0
    while limSup <= len(trainData):
        testSet = trainData[int(limInf):int(limSup)]
        expectedOutput = outputData[int(limInf):int(limSup)]
        trainSet = trainData[0:int(limInf)] + trainData[int(limSup):int(len(trainData))]
        outputSet = outputData[0:int(limInf)] + outputData[int(limSup):int(len(trainData))]
        perceptron.trainingData = trainSet
        perceptron.expectedOutput = outputSet
        perceptron.w_min = numpy.zeros(len(trainSet[0]))
        perceptron.error_min = numpy.inf
        perceptron.algorithm2(1000)
        current = simpleErrorFunc(testSet, expectedOutput, perceptron.w_min, sigmoidTanhActivationFunc) / len(testSet)
        accuracy[i] = 1 / current
        i += 1
        limSup += len(trainData) / 10
        limInf += len(trainData) / 10
    print(accuracy)

