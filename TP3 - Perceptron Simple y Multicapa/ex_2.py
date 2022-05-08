from src.utils import *
from src.perceptron import *
from src.methods import *

trainData = parse_training_data('TP3-ej2-Conjunto-entrenamiento.txt')
outputData = parse_output_data('TP3-ej2-Salida-deseada.txt')
trainData = append_threshold(trainData)
#outputData = append_threshold(outputData)

#print(f'Train = {trainData}\noutput = {outputData}')

str = "point1"

if str == "point1":
    perceptron = perceptron(trainData, outputData, 0.1, sigmoidTanhActivationFunc, simpleErrorFunc, False, sigmoidTanhActivationFuncDerivative)
    perceptron.algorithm2(10000)
    print(f'Min w = {perceptron.w_min} and min error = {perceptron.error_min}')


