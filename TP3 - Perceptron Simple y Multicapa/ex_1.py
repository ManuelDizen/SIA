import numpy
import pandas as pd
import matplotlib.pyplot as plt
from src.perceptron import *
from src.methods import *

print("TP3 - Perceptron simple y multicapa\n")
print("Ejercicio 1: Perceptron siple con función de activación escalón con dos funciones:")

trainDataAnd = numpy.array([[-1,1,1],[1,-1,1],[-1,-1,1],[1,1,1]])
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
#print("\nFunción lógica \"XOR\"")
#
trainDataXor = numpy.array([[-1,1,1],[1,-1,1],[-1,-1,1],[1,1,1]])
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
# print("\nFunción lógica \"XOR\"")
#
# perceptron2 = perceptron(trainDataXor, expectedOutputXor, 0.1, simpleActivationFunc, simpleErrorFunc, True)
# perceptron.algorithm2(30)

# print("\nFunción lógica \"AND\"")
# #
# perceptron = perceptron(trainDataAnd, expectedOutputAnd, 0.1, simpleActivationFunc, simpleErrorFunc, True)
# perceptron.algorithm2(50)
# print(f'W mínimo = {perceptron.w_min}, Error mínimo = {perceptron.error_min}')
# x_axis_values = [-2, -1, 0, 1, 2]
# y_axis_values = []
# aux = perceptron.w_min*1.0
# print(f'{aux}')
# for i in range(len(x_axis_values)):
#     t = (aux[1] * 1.0 * x_axis_values[i] + aux[2]) / -aux[0]
#     y_axis_values.append(t)
# ax = plt.subplot()
# col = numpy.where(expectedOutputAnd < 1,'r','b')
# plt.scatter([row[0] for row in trainDataAnd], [row[1] for row in trainDataAnd], c=col, s=300)
# plt.title("Resultados de la función \"AND\"")
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.grid(visible=True)
# ax.plot(x_axis_values, y_axis_values)
# fig1 = plt.gcf()
# plt.show()
# plt.draw()

print("\nFunción lógica \"XOR\"")
#
perceptron = perceptron(trainDataXor, expectedOutputXor, 0.1, simpleActivationFunc, simpleErrorFunc, True)
perceptron.algorithm2(50)
print(f'W mínimo = {perceptron.w_min}, Error mínimo = {perceptron.error_min}')
x_axis_values = [-2, -1, 0, 1, 2]
y_axis_values = []
aux = perceptron.w_min*1.0
print(f'{aux}')
for i in range(len(x_axis_values)):
    t = (aux[1] * 1.0 * x_axis_values[i] + aux[2]) / -aux[0]
    y_axis_values.append(t)
ax = plt.subplot()
col = numpy.where(expectedOutputAnd < 1,'r','b')
plt.scatter([row[0] for row in trainDataXor], [row[1] for row in trainDataXor], c=col, s=300)
plt.title("Resultados de la función \"XOR\"")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(visible=True)
ax.plot(x_axis_values, y_axis_values)
fig1 = plt.gcf()
plt.show()
plt.draw()