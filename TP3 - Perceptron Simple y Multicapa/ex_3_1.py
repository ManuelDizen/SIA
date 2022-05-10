import numpy as np
from src.layer import Layer
from src.multilayer_perceptron import MultilayerPerceptron
from src.methods import sigmoidTanhActivationFunc, \
    sigmoidTanhActivationFuncDerivative
from src.utils import plotError


trainDataXor = np.array([[-1, 1], [1, -1], [-1, -1], [1, 1]])
expectedOutputXor = np.array([1, 1, 1, -1])

layer1 = Layer(4, 2)
layer2 = Layer(1, 4)

perceptron = MultilayerPerceptron([layer1, layer2], sigmoidTanhActivationFunc, sigmoidTanhActivationFuncDerivative, 0.1)
print("\nFunción lógica \"AND\"")
errors = perceptron.algorithm(trainDataXor, expectedOutputXor, 300)
plotError(errors)

