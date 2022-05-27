from numpy.linalg import norm


class pairs:
    def __init__(self, label1, label2, input1, input2):
        self.label1 = label1
        self.label2 = label2
        self.dist = abs(norm(input1 - input2))

    def getDist(self):
        return self.dist

    def __str__(self):
        return f'{self.label1}, {self.label2}: {self.dist}'
