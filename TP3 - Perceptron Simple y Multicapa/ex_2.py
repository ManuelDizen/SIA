import numpy

from src.utils import *
from src.perceptron import *
from src.methods import *
import matplotlib.pyplot as plt

trainData = parseTrainingData('TP3-ej2-Conjunto-entrenamiento.txt')

output = parseOutputData('TP3-ej2-Salida-deseada.txt')

outputNormalized = normalize(output)

trainData = appendThreshold(trainData)

# print(trainData)
# print(output)
# print(outputNormalized)
# print(outputNormalized2


linear_perceptron = perceptron(trainData, output, 0.01, linearActivationFunc, simpleErrorFunc, True)
tanh_perceptron = perceptron(trainData, outputNormalized, 0.01, sigmoidTanhActivationFunc, simpleErrorFunc, False,
                             sigmoidTanhActivationFuncDerivative, denormalizeErrorFunc)
print("LINEAR PERCEPTRON:")
linear_perceptron.algorithm(10000)
print(f'w min: {linear_perceptron.w_min}, error min: {linear_perceptron.error_min}')
print("NON LINEAR PERCEPTRON:")
tanh_perceptron.algorithm(10000)
print(
    f'w min: {tanh_perceptron.w_min}, error min: {tanh_perceptron.error_min}, denormalized error min: {tanh_perceptron.min_errors_denormalize[-1]}')

x_axis_values = range(10000)
y_axis_values = linear_perceptron.errors
plt.plot(x_axis_values, y_axis_values, label=f'{linear_perceptron}')
x_axis_values = range(10000)
y_axis_values = tanh_perceptron.min_errors_denormalize
plt.ylim(0, 50000)
plt.plot(x_axis_values, y_axis_values, label=f'{tanh_perceptron} denormalized')
plt.title(f'Error para cada iteración')
plt.xlabel("Iteraciones")
plt.ylabel("Error")
plt.legend()
plt.show()

learnrates = [1, 0.5, 0.1, 0.01, 0.001, 0.0001]
for i in learnrates:
    tanh_perceptron.error_min = numpy.inf
    tanh_perceptron.w_min = numpy.zeros(len(trainData[0]))
    tanh_perceptron.learnRate = i
    tanh_perceptron.algorithm(10000)
    x_axis_values = range(10000)
    y_axis_values = tanh_perceptron.min_errors_denormalize
    plt.plot(x_axis_values, y_axis_values, label=f'n = {i}')
plt.title(f'Error en {tanh_perceptron}')
plt.xlabel("Iteraciones")
plt.ylabel("Error mínimo")
plt.legend()
plt.show()

ks = [20, 40, 60, 80, 100, 120, 140, 160, 180]
perceptron = perceptron(trainData, outputNormalized, 0.01, sigmoidTanhActivationFunc, simpleErrorFunc,
                        False, sigmoidTanhActivationFuncDerivative, denormalizeErrorFunc)
trainAcc = numpy.zeros(10)
testAcc = numpy.zeros(10)
for k in ks:
    trainSet = trainData[:int(k)]
    testSet = trainData[int(k):]
    trainOutput = output[:int(k)]
    trainOutputNormalized = normalize(trainOutput)
    testOutput = output[int(k):]
    testOutputNormalized = normalize(testOutput)

    perceptron.trainingData = trainSet
    perceptron.expectedOutput = trainOutputNormalized
    perceptron.error_min = numpy.inf
    perceptron.w_min = numpy.zeros(len(trainData[0]))
    perceptron.algorithm(10000)
    index = k / 20
    trainAcc[int(index)] = denormalizeErrorFunc(trainSet, trainOutputNormalized, perceptron.w_min,
                                                sigmoidTanhActivationFunc) / len(trainSet)

    testAcc[int(index)] = denormalizeErrorFunc(testSet, testOutputNormalized, perceptron.w_min,
                                               sigmoidTanhActivationFunc) / len(testSet)
    print(f'{trainAcc[int(index)]}, {testAcc[int(index)]}')

x = numpy.zeros(9)
for i in range(9):
    x[i] = (i + 1) * 10

x_axis_values = x
y_axis_values = trainAcc[1:]
plt.plot(x_axis_values, y_axis_values, label=f'Entrenamiento')
y_axis_values = testAcc[1:]
plt.plot(x_axis_values, y_axis_values, label=f'Test')
plt.title(f'Accuracy para diferentes tamaños del conjunto de entrenamiento')
plt.xlabel("Porcentaje del total")
plt.ylabel("Accuracy")
plt.legend()
plt.show()

ks = [20, 100, 180]
perceptron.learnRate = 0.001
for k in ks:
    trainSet = trainData[:int(k)]
    testSet = trainData[int(k):]
    trainOutput = output[:int(k)]
    trainOutputNormalized = normalize(trainOutput)
    testOutput = output[int(k):]
    perceptron.trainingData = trainSet
    perceptron.expectedOutput = trainOutputNormalized
    perceptron.error_min = numpy.inf
    perceptron.w_min = numpy.zeros(len(trainData[0]))
    accuracy = numpy.zeros(500)
    accuracyTraining = numpy.zeros(500)
    for i in range(500):
        perceptron.algorithm(100)
        print(
            f'w min: {perceptron.w_min}, error min: {perceptron.error_min}, denormalized error min: {perceptron.min_errors_denormalize[-1]}')
        accuracyTraining[i] = calcAccuracy(trainSet, trainOutput, perceptron.w_min, sigmoidTanhActivationFunc)
        accuracy[i] = calcAccuracy(testSet, testOutput, perceptron.w_min, sigmoidTanhActivationFunc)
    x_axis_values = range(500)
    y_axis_values = accuracyTraining
    plt.plot(x_axis_values, y_axis_values, label="Entrenamiento")
    y_axis_values = accuracy
    plt.plot(x_axis_values, y_axis_values, label="Test")
    porc = int(k / 2)
    plt.title(f'Accuracy vs época para {porc}%')
    plt.xlabel("Época")
    plt.ylabel("Accuracy")
    plt.legend()
    plt.show()

limInf = 0
limSup = int(len(trainData) / 5)
accuracy = numpy.zeros(10)
i = 0
while limSup <= len(trainData):
    print(f'limInf = {limInf}, limSup = {limSup}')
    testSet = trainData[limInf:limSup]
    trainSet = trainData[:limInf] + trainData[limSup:]
    testOutput = output[limInf:limSup]
    trainOutput = output[:limInf] + output[limSup:]
    trainOutputNormalized = normalize(trainOutput)
    perceptron.trainingData = trainSet
    perceptron.expectedOutput = trainOutputNormalized
    perceptron.error_min = numpy.inf
    perceptron.w_min = numpy.zeros(len(trainData[0]))
    perceptron.algorithm(5000)
    accuracy = calcAccuracy(testSet, testOutput, perceptron.w_min, sigmoidTanhActivationFunc)
    print(accuracy)
    limSup += int(len(trainData) / 5)
    limInf += int(len(trainData) / 5)
