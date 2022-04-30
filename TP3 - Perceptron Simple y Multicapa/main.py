import numpy
import pandas as pd
import matplotlib.pyplot as plt
from src.perceptron import *
from src.methods import *

print("TP3 - Perceptron simple y multicapa\n")
print("Ejercicio 1: Perceptron siple con función de activación escalón con dos funciones:")

trainDataAnd = numpy.array([[-1,1],[1,-1],[-1,-1],[1,1]])
expectedOutputAnd = numpy.array([-1,-1,-1,1])

# col = numpy.where(expectedOutputAnd < 1,'r','b')
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.title('Distribución de puntos función "AND"')
# plt.scatter([row[0] for row in trainDataAnd], [row[1] for row in trainDataAnd], c=col, s=300)
#
# plt.grid()
# plt.show()
# plt.savefig('graphs/puntos_and.png')
print("\nFunción lógica \"XOR\"")
#
trainDataXor = numpy.array([[-1,1],[1,-1],[-1,-1],[1,1]])
expectedOutputXor = numpy.array([1,1,-1,-1])

# col = numpy.where(expectedOutputXor < 1,'r','b')
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.title('Distribución de puntos función "XOR"')
# plt.scatter([row[0] for row in trainDataXor], [row[1] for row in trainDataXor], c=col, s=300)
#
# plt.grid()
# plt.show()
# plt.savefig('graphs/puntos_xor.png')
#perceptron2 = perceptron(trainDataXor, expectedOutputXor, 0.1, simpleActivationFunc, simpleErrorFunc, True)
#perceptron2.algorithm(10)

print("\nFunción lógica \"AND\"")
#
perceptron = perceptron(trainDataAnd, expectedOutputAnd, 0.1, simpleActivationFunc, simpleErrorFunc, True)
perceptron.algorithm2(50)
