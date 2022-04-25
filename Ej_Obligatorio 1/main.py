# -*- coding: utf-8 -*-
"""EjercicioSIA.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1D7Dj6ilBl-zU0oC2yJvVbWE_1JYxlzS5
"""

!pip install qiskit
from qiskit import algorithms
import numpy as np
import matplotlib.pyplot as plt
import math
import time
import random

training_set = [[4.4793, -4.0765, -4.0765], [-4.1793, -4.9218, 1.7664], [-3.9429, -0.7689, 4.8830]]
output = [0, 1, 1]


def g(x):
  return math.exp(x) / (1 + math.exp(x))

def F(W, w, w0, mu):
  outerSum = 0
  innerSum = 0
  # Chequear los índices de los arreglos
  for j in range(0,2):
    for k in range(0,3):
      innerSum += w[j][k]*mu[k]
    outerSum += W[j+1]*g(innerSum - w0[j])
    innerSum = 0
  return g(outerSum - W[0])

def error(W, w, w0):
  sum = 0
  for i in range(0,3):
    sum += ((output[i] - F(W, w, w0, training_set[i])) ** 2)
  return sum

def aux (arr):
  W = [arr[i] for i in range(0,3)]
  w = [[], []]
  w[0] = [arr[i] for i in range(3,6)]
  w[1] = [arr[i] for i in range(6,9)]
  w0 = [arr[i] for i in range(9,11)]
  return error(W, w, w0)

def restart():
  return np.zeros(11)

def print_result(w):
    auxi = w[0]
    print("\t-- 0 --")
    print("W = " + str(auxi[0:3]))
    print("w = " + str(auxi[3:6]) + "\n\t " + str(auxi[6:9]))
    print("w0 = " + str(auxi[9:11]))
    print("Error: " + str(w[1]))
    print("\t-- 0 --")

print("\nGradientes conjugados:\n------------------------")
x0 = restart()
t0 = time.time()
out = algorithms.optimizers.CG().optimize(11, aux, initial_point=x0)
tf = time.time()
print(f'Tiempo de ejecución: {(tf-t0)}s')
print('\nResultados:\n')
print_result(out)

print("\nGradientes descendientes:\n------------------------")
x0 = restart()
t0 = time.time()
out = algorithms.optimizers.GradientDescent().optimize(11, aux, initial_point=x0)
tf = time.time()
print(f'Tiempo de ejecución: {(tf-t0)}s')
print('\nResultados:\n')
print_result(out)

print("\nADAM:\n------------------------")
x0 = restart()
t0 = time.time()
out = algorithms.optimizers.ADAM().optimize(11, aux, initial_point=x0)
tf = time.time()
print(f'Tiempo de ejecución: {(tf-t0)}s')
print('\nResultados:\n')
print_result(out)