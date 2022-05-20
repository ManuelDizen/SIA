import numpy as np
from numpy import random
import math
from src.neuron import neuron

class kohonenNetwork:
    def __init__(self, k, r_0, learnRate_0, inputs):
        self.k = k
        self.r_0 = r_0
        self.learnRate_0 = learnRate_0
        self.grid = [[None for _ in range(k)] for _ in range(k)]
        for i in range(k):
            for j in range(k):
                idx = random.randint(0, len(inputs))
                self.grid[i][j] = neuron(inputs[idx])
        self.iterations = 500 * len(inputs[0])

    def train(self, inputs):
        k = 0
        r = self.r_0
        n = self.learnRate_0
        while k < self.iterations:
            idx = random.randint(0, len(inputs))
            x, y = self.findBestCandidate(inputs[idx])
            self.updateNeighbours(x, y, self.grid, r, n, inputs[idx])
            k, r, n = updateParameters(k, self.r_0, self.learnRate_0)

    def findBestCandidate(self, candidate):
        distance = np.Infinity
        bestX = -1
        bestY = -1
        for x in range(0, self.k):
            for y in range(0, self.k):
                if self.grid[x][y].distanceTo(candidate) < distance:
                    distance = self.grid[x][y].distanceTo(candidate)
                    bestX = x
                    bestY = y
        return bestX, bestY

    def updateNeighbours(self, x, y, grid, r, n, input):
        for i in range(x - r, x + r + 1):
            for j in range(y - r, y + r + 1):
                # need to check for borders
                if 0 <= i < self.k and 0 <= j < self.k and math.hypot(x - i, y - j) <= r:
                    grid[i][j].weights += n*(input - grid[i][j].weights)
        self.grid = grid

    def updateNeighbours(self, iters, r_0, learnRate_0):
        iters += 1
        # update r_0 and n_0