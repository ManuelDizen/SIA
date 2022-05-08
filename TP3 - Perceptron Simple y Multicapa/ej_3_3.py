import numpy as np
from src.utils import parseNumbers
from src.layer import Layer
from src.multilayer_perceptron import MultilayerPerceptron
from src.methods import sigmoidTanhActivationFunc, \
    sigmoidTanhActivationFuncDerivative

numbers = parseNumbers("TP3-ej3-mapa-de-pixeles-digitos-decimales.txt")
expectedOutput = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]]

layer1 = Layer(16, 35)
layer2 = Layer(10, 16)
layer3 = Layer(10, 10)

perceptron = MultilayerPerceptron([layer1, layer2, layer3], sigmoidTanhActivationFunc,
                                  sigmoidTanhActivationFuncDerivative, 0.1)



perceptron.algorithm(numbers, expectedOutput, 100)
perceptron.error(numbers, expectedOutput)
