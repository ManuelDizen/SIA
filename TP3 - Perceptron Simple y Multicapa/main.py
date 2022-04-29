import numpy
import pandas as pd
import matplotlib.pyplot as plt
from src.perceptron import *
from src.methods import *

print("TP3 - Perceptron simple y multicapa\n")
print("Ejercicio 1: Perceptron siple con función de activación escalón con dos funciones:"
      "\nFunción lógica \"Y\"")

trainDataAnd = numpy.array([[-1,1],[1,-1],[-1,-1],[1,1]])
expectedOutputAnd = numpy.array([-1,-1,-1,1])



print("\nFunción lógica \"XOR\"")

trainDataXor = numpy.array([[-1,1],[1,-1],[-1,-1],[1,1]])
expectedOutputXor = numpy.array([1,1,-1,-1])
perceptron2 = perceptron(trainDataXor, expectedOutputXor, 0.1, simpleActivationFunc, simpleErrorFunc)
perceptron2.algorithm(10)

print("\nFunción lógica \"AND\"")

perceptron = perceptron(trainDataAnd, expectedOutputAnd, 0.1, simpleActivationFunc, simpleErrorFunc)
perceptron.algorithm(10)
