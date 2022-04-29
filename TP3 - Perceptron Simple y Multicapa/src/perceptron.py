import numpy


class perceptron:
    def __init__(self, trainingData, expectedOutput, learnRate, activationFunc, errorFunc, isLinear=False, derivative=None):
        self.w_min = None
        self.error_min = None
        self.trainingData = trainingData
        self.expectedOutput = expectedOutput
        self.learnRate = learnRate
        self.activationFunc = activationFunc
        self.errorFunc = errorFunc
        self.isLinear = isLinear
        self.derivative = derivative # Necesario para perceptron NO lineal, que usa la misma formula de delta_w
                                     # mulitplicada por g'(h)

    def algorithm(self, maxIterations):
        i = 0
        inputN = len(self.trainingData)
        inputSize = len(self.trainingData[0])
        w = numpy.zeros(inputSize)
        error = 1
        # error_min = (inputN * 2)*1.0
        self.error_min = (inputN * 2)*1.0
        while i < maxIterations and error > 0:
            position = numpy.random.randint(0, inputN - 1)
            # TODO: ¿Producto interno en python? ¿Uso builtin de numpy?
            h = numpy.dot(self.trainingData[position], w)
            actualOut = self.activationFunc(h)
            for pos in range(0, len(w)):
                delta_w = self.learnRate * (self.expectedOutput[position] - actualOut) * self.trainingData[
                    position][pos]
                if self.isLinear is not True:
                    delta_w *= self.derivative(actualOut)
                w[pos] += delta_w
            error = self.errorFunc(self.trainingData, self.expectedOutput, w, self.activationFunc)
            if error < self.error_min:
                self.error_min = error
                self.w_min = w
            i = i + 1
        print(f'Iters: {i}, Min error: {self.error_min}, Min w: {self.w_min}')
