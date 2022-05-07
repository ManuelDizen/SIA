import numpy as np

from src.layer import Layer
from src.multilayer_perceptron import MultilayerPerceptron
from src.methods import sigmoidTanhActivationFunc, \
    sigmoidTanhActivationFuncDerivative


trainDataAnd = np.array([[-1, 1], [1, -1], [-1, -1], [1, 1]])
expectedOutputAnd = np.array([1, 1, -1, -1])

layer1 = Layer(4, 2)
layer2 = Layer(2, 4)

perceptron = MultilayerPerceptron([layer1, layer2], sigmoidTanhActivationFunc, sigmoidTanhActivationFuncDerivative, 0.1)
print("\nFunción lógica \"AND\"")
perceptron.algorithm(trainDataAnd, expectedOutputAnd, 50)
perceptron.error(trainDataAnd, expectedOutputAnd)
