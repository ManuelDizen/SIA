import numpy as np
from numpy import random
import math
from src.neuron import *


class kohonenNetwork:

    def __init__(self, k: int, r_0: int, learnRateConstant: False, learnRate_0: float, inputs, labels, isRandom=True):
        self.k = k
        self.r_0 = r_0
        self.learnRateConstant = learnRateConstant
        if not learnRateConstant:
            self.learnRate_0 = learnRate_0
        self.grid = [[None for _ in range(k)] for _ in range(k)]
        self.initialIdxs = []
        #rows = []
        #for j in range(0,k):
        #    row = [neuron(inputs[random.randint(0, len(inputs))]) for i in range(0, k)]
        #    rows.append(row)
        #self.grid = rows
        if isRandom is True:
            for i in range(0, k):
                for j in range(0, k):
                    idx = random.randint(0, len(inputs))
                    self.grid[i][j] = neuron(inputs[idx])
                    self.grid[i][j].addEntry(labels[idx])
                    self.initialIdxs.append(idx)

        else:
            idx = 0
            for i in range(0, k):
                for j in range(0, k):
                    self.grid[i][j] = neuron(inputs[idx])
                    idx += 1
                #  print(f'{i}, {j}: {inputs[idx]}')
        self.iterations = 50000
        print(self.initialIdxs)
        #  self.iterations = 5


    def train(self, inputs, labels):
        k = 0
        r = self.r_0
        n = self.learnRate_0
        while k < self.iterations:
            idx = random.randint(0, len(inputs))
            x, y = self.findBestCandidate(inputs[idx])
            self.updateNeighbours(x, y, self.grid, r, n, inputs[idx])
            k, r, n = self.updateParameters(k)

    def test(self, inputs, labels):

        for i in range(len(inputs)):
            x, y = self.findBestCandidate(inputs[i])
            self.grid[x][y].addEntry(labels[i])

    def findBestCandidate(self, candidate):
        distance = np.Infinity
        bestX = -1
        bestY = -1
        for x in range(0, self.k):
            for y in range(0, self.k):

                current = self.grid[x][y].distanceTo(candidate)
                #  print(f'candidate = {candidate}, name = {name}, current = {current}, distance = {distance}')
                #  print(current)
                if current < distance:
                    distance = current
                    bestX = x
                    bestY = y
        #  self.grid[bestX][bestY].addEntry(name)
        #  print(f'{bestX}, {bestY}')
        return bestX, bestY

    def updateNeighbours(self, x, y, grid, r, n, input):

        #  print(f'x={x}, y={y}, r={r}, n={n}')
        for i in range(x - r, x + r + 1):
            for j in range(y - r, y + r + 1):
                # need to check for borders
                if 0 <= i < self.k and 0 <= j < self.k and math.hypot(x - i, y - j) <= r:
                    #  print(i, j)
                    #  print(f'old weights = {grid[i][j].weights}, input = {input}')
                    grid[i][j].weights += n * (input - grid[i][j].weights)
                    # print(f'new weights = {grid[i][j].weights}')
        self.grid = grid

    def updateParameters(self, iters):
        iters += 1
        learnRate = self.learnRate_0
        if not self.learnRateConstant:
            learnRate =  self.learnRate_0 - ((1 - self.learnRate_0) / self.iterations * iters)
        r = int((1/self.r_0 - self.r_0) * (((iters / self.iterations))**0.5)) + self.r_0
        #  print(f'i: {iters} -> new r: {r}, new n = {learnRate}')
        return iters, r, learnRate
        # update r_0 and n_0
