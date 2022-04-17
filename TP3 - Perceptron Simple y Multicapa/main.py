import numpy
import pandas as pd
from src.perceptron import *
from src.methods import *

print("TP3 - Perceptron simple y multicapa\n")
print("Ejercicio 1: Perceptron siple con función de activación escalón con dos funciones:"
      "\nFunción lógica \"Y\"\nFunción lógica \"O exclusivo\"")

trainDataY = numpy.array([[-1,1],[1,-1],[-1,-1],[1,1]])
expectedOutputY = numpy.array([-1,-1,-1,1])

perceptron = perceptron(trainDataY, expectedOutputY, 0.1, simpleActivationFunc, simpleErrorFunc)
perceptron.algorithm(100)


