import numpy


class perceptron:
    def __init__(self, trainingData, expectedOutput, learnRate, activationFunc, errorFunc, isLinear=False, derivative=None, default_min_error=0.01):
        self.w_min = numpy.zeros(len(trainingData[0]))
        self.error_min = numpy.inf
        self.trainingData = trainingData
        self.expectedOutput = expectedOutput
        self.learnRate = learnRate
        self.activationFunc = activationFunc
        self.errorFunc = errorFunc
        self.isLinear = isLinear
        self.default_min_error = default_min_error
        self.errors = []
        self.min_errors = []
        self.derivative = derivative
            

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
            print(f'h = {actualOut}, expectedOut = {self.expectedOutput[position]}, w = {self.w_min}, error = {error}')
            if error < self.error_min:
                self.error_min = error
                self.w_min = w
            i = i + 1
        print(f'Iters: {i}, Min error: {self.error_min}, Min w: {self.w_min}')

    def algorithm2(self, maxIterations=30):
       i = 0
        w = self.w_min
        if self.activationFunc == simpleActivationFunc:
            w[len(self.trainingData[0])-1] = 1
        error = 1
        self.errors = numpy.zeros(maxIterations)
        self.min_errors = numpy.zeros(maxIterations)
        while error > self.default_min_error and i < maxIterations:
            idx = numpy.random.randint(0, len(self.trainingData) - 1)
    
            h_value = numpy.dot(self.trainingData[idx], w)
           
            activation = self.activationFunc(h_value)
            
            delta_w = self.learnRate * (self.expectedOutput[idx] - activation) * self.trainingData[idx]
            
            if self.isLinear is not True:
                delta_w *= self.derivative(activation)
            
            w += delta_w           
            error = self.errorFunc(self.trainingData, self.expectedOutput, w, self.activationFunc)
            self.errors[i] = error
            if error < self.error_min:
                self.error_min = error
                self.w_min = w
            self.min_errors[i] = self.error_min
            i = i+1

            
        def __str__(self):
            if self.activationFunc == simpleActivationFunc:
                return 'Perceptrón Escalón'
            elif self.activationFunc == linearActivationFunc:
                return 'Perceptrón Lineal'
            elif self.activationFunc == sigmoidTanhActivationFunc:
                return 'Perceptrón No Lineal (Tanh)'
            elif self.activationFunc == sigmoidLogisticActivationFunc:
                return 'Perceptrón No Lineal (Logistic)'
