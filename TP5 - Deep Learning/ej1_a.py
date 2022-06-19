import numpy as np
from seaborn import heatmap
import matplotlib.pyplot as plt

from src.layer import Layer
from src.multilayer_perceptron import MultilayerPerceptron
from src.methods import sigmoidTanhActivationFunc, \
    sigmoidTanhActivationFuncDerivative
from res.fonts import *
from src.utils import *

layer1 = Layer(20, 35)
layer2 = Layer(5, 20)
layer3 = Layer(20, 5)
layer4 = Layer(35, 20)
layer5 = Layer(35, 35)

f = 1
if f == 1:
    font = font_1
elif f == 2:
    font = font_2
else:
    font = font_3

perceptron = MultilayerPerceptron([layer1, layer2, layer3, layer4, layer5], sigmoidTanhActivationFunc, sigmoidTanhActivationFuncDerivative, 0.01)
letters = parse_letters_to_int(font)
errors, weights = perceptron.algorithm(letters, letters, 5000)
graph_digits(letters, weights)
plt.plot(errors)
plt.xlabel("Epochs")
plt.ylabel("Error")
plt.show()
#monocromatic_cmap = plt.get_cmap('binary')
