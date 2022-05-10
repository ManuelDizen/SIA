import numpy as np


class MultilayerPerceptron:
    def __init__(self, layers, function, derivative, learnRate):
        self.layers = layers
        self.function = function
        self.derivative = derivative
        self.learnRate = learnRate


    def algorithm(self, trainData, expectedOutput, maxIters):
        errors = []
        for i in range(maxIters):
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
            print(f'Iteration {i}:')
            errors.append(self.error(trainData, expectedOutput))
        return errors

    def activate(self, inputs):
        activations = [inputs]
        for i in range(len(self.layers)):
            aux = self.layers[i].activate(activations[-1], self.function)
            activations.append(aux)
        return activations

    def error(self, trainData, expectedOutput):
        # Calculo el error
        error = 0
        for pos in range(trainData.shape[0]):
            estimation = self.activate(trainData[pos])[-1]
            auxerror = (expectedOutput[pos] - estimation) * (expectedOutput[pos] - estimation)
            error += auxerror
            print(
                f'h = {estimation}, expectedOut = {expectedOutput[pos]}, error = {auxerror}')
        return np.sum(error)/trainData.shape[0]
