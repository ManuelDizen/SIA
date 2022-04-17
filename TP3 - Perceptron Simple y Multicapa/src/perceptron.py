import numpy

class perceptron:
    def __init__(self, trainingData, expectedOutput, learnRate, activationFunc, errorFunc):
        self.w_min = None
        self.error_min = None
        self.trainingData = trainingData
        self.expectedOutput = expectedOutput
        self.learnRate = learnRate
        self.activationFunc = activationFunc
        self.errorFunc = errorFunc

    def algorithm(self, maxIterations):
        i = 0
        inputN = len(self.trainingData)
        inputSize = len(self.trainingData[0])
        w = numpy.zeros(inputSize)
        error = 1
        error_min = inputN*2
        while i < maxIterations and error > 0:
            position = numpy.random.randint(0, inputN)
            # TODO: ¿Producto interno en python? ¿Uso builtin de numpy?
            h = numpy.inner(self.trainingData[position], w)
            delta_w = self.learnRate*(self.expectedOutput[position] - self.activationFunc(h))*self.trainingData[position]
            w = w + delta_w
            error = self.errorFunc(self.trainingData, self.expectedOutput, w, self.activationFunc)
            if error < error_min:
                self.error_min = error
                self.w_min = w
            i = i + 1
        print("Despues de ", i, " iteraciones, minimo error fue: ", error_min, " y minimo w fue ", self.w_min)