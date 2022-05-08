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
            print(f'h = {actualOut}, expectedOut = {self.expectedOutput[position]}, w = {self.w_min}, error = {error}')
            if error < self.error_min:
                self.error_min = error
                self.w_min = w
            i = i + 1
        print(f'Iters: {i}, Min error: {self.error_min}, Min w: {self.w_min}')

    def algorithm2(self, maxIterations=30):
        i = 0
        w = numpy.zeros(len(self.trainingData[0]) - 1)
        w = numpy.append(w, 1)
        error = 1
        while error > self.default_min_error and i < maxIterations:
            idx = numpy.random.randint(0, len(self.trainingData) - 1)
            #print(f'Len de w = {len(w)} ({w}) y Len de training = {len(self.trainingData[idx])} ({self.trainingData[idx]})')
            h_value = numpy.dot(self.trainingData[idx], w)
            activation = self.activationFunc(h_value)
            #auxData = numpy.array(self.trainingData[idx])
            #print(f'learnrate = {self.learnRate} - exp = {self.expectedOutput[idx]} - auxDAta = {auxData}')
            #delta_w = self.learnRate * (self.expectedOutput[idx] - activation) * auxData
            delta_w = self.learnRate * (self.expectedOutput[idx] - activation) * self.trainingData[idx]
            if self.isLinear is not True:
                delta_w *= self.derivative(activation)
            w += delta_w
            # for j in range(0, len(w)):
            #     delta_w = self.learnRate * (self.expectedOutput[idx] - activation) * self.trainingData[idx][j]
            #     if self.isLinear is not True:
            #         delta_w *= self.derivative(activation)
            #     w[j] += delta_w
            error = self.errorFunc(self.trainingData, self.expectedOutput, w, self.activationFunc)
            if error < self.error_min:
                print(f'(Ya estoy cambiando) Error = {error}, self.error_min = {self.error_min}')
                self.error_min = error
                self.w_min = w
            i = i+1
        print(f'w = {w} error = {self.error_min}\n')