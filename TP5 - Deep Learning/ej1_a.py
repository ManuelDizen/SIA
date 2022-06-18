import numpy as np
from src.layer import Layer
from src.multilayer_perceptron import MultilayerPerceptron
from src.methods import sigmoidTanhActivationFunc, \
    sigmoidTanhActivationFuncDerivative

layer1 = Layer(4, 2)
layer2 = Layer(2, 4)

perceptron = MultilayerPerceptron([layer1, layer2], sigmoidTanhActivationFunc, sigmoidTanhActivationFuncDerivative, 0.1)