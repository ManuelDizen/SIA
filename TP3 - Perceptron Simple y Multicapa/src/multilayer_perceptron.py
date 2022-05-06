import numpy as np


class MultilayerPerceptron:
    def __init__(self, layers, function, derivative, learnRate):
        self.layers = layers
        self.function = function
        self.derivative = derivative
        self.learnRate = learnRate


    def algorithm(self, trainData, expectedOutput, maxIters):
        i = 0
        while i <= maxIters:
            print()
            print(f'Iteration {i}:')
            for j in range(len(trainData)):
                # Propago la entrada
                activations = self.activate(trainData[j])
                self.layers[-1].error(expectedOutput[j] - activations[-1], self.derivative, activations[-1])
                for k in range(len(self.layers) - 2, -1, -1):
                    previousLayer = self.layers[k + 1]
                    self.layers[k].error(previousLayer.weights.dot(previousLayer.derivativeError), self.derivative,
                                         activations[k + 1])

                #Retropropago delta
                for k in range(len(self.layers)):
                    self.layers[k].delta(activations[k], self.learnRate)

                #Calculo el error
                error = 0
                for pos in range(trainData.shape[0]):
                    estimation = self.activate(trainData[pos])[-1]
                    error += (expectedOutput[pos] - estimation) * (expectedOutput[pos] - estimation)
                    print(f'h = {estimation}, expectedOut = {expectedOutput[pos]}, error = {np.sum(error) / trainData.shape[0]}')
            i = i + 1

    def activate(self, input):
        activations = [input]
        for i in range(len(self.layers)):
            activations.append(self.layers[i].activate(activations[-1], self.function))
        return activations
