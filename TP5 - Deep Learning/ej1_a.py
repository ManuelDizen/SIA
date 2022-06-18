import numpy as np
from seaborn import heatmap
import matplotlib.pyplot as plt

from src.layer import Layer
from src.multilayer_perceptron import MultilayerPerceptron
from src.methods import sigmoidTanhActivationFunc, \
    sigmoidTanhActivationFuncDerivative
from res.fonts import *

layer1 = Layer(35, 12)
layer2 = Layer(12, 2)
layer3 = Layer(2, 12)
layer4 = Layer(12, 35)

perceptron = MultilayerPerceptron([layer1, layer2, layer3, layer4], sigmoidTanhActivationFunc, sigmoidTanhActivationFuncDerivative, 0.01)
letters = parse_letters_to_int(font_3)
perceptron.algorithm(letters, letters, letters[1], letters[1], 5000)
monocromatic_cmap = plt.get_cmap('binary')
monocromatic_cmap