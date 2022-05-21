from numpy.linalg import norm


class neuron:
    def __init__(self, weights):
        self.weights = weights
        self.matched = 0
        self.entriesMatched = []

    def distanceTo(self, other):
        return norm(other - self.weights)

    def addEntry(self, name):
        self.matched += 1
        self.entriesMatched.append(name)
