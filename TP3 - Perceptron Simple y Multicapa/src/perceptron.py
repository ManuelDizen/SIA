import numpy

class perceptron:
    def __init__(self, trainingData, expectedOutput, learnRate, activationFunc, errorFunc, isLinear=False, derivative=None, denormalize=None, default_min_error=0.000001):
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
        self.errors_denormalize = []
        self.min_errors_denormalize = []
        self.w = []
        self.derivative = derivative
        self.denormalize = denormalize


    def algorithm(self, maxIterations=30):
        i = 0
        w = self.w_min

        error = 1
        self.errors = numpy.zeros(maxIterations)
        self.min_errors = numpy.zeros(maxIterations)
        self.errors_denormalize = numpy.zeros(maxIterations)
        self.min_errors_denormalize = numpy.zeros(maxIterations)
        while error > self.default_min_error and i < maxIterations:
            idx = numpy.random.randint(0, len(self.trainingData) - 1)
            h_value = numpy.dot(self.trainingData[idx], w)
            activation = self.activationFunc(h_value)
            #  print(f'train={self.trainingData[idx]}, expected={self.expectedOutput[idx]}, h={h_value}, activation state={activation}')
            delta_w = self.learnRate * (self.expectedOutput[idx] - activation) * self.trainingData[idx]
            #  print(f'before->{delta_w}')
            if self.isLinear is not True:
                delta_w *= self.derivative(activation)

            w += delta_w

            #  print(f'after->{delta_w}')
            error = self.errorFunc(self.trainingData, self.expectedOutput, w, self.activationFunc)
            #  print(f'w={w}, error={error}')
            self.errors[i] = error
            if error < self.error_min:
                self.error_min = error
                self.w_min = w
            self.min_errors[i] = self.error_min
            if self.isLinear is not True:
                den = self.denormalize(self.trainingData, self.expectedOutput, w, self.activationFunc)
                self.min_errors_denormalize[i] = den
            i = i+1

    def __str__(self):
        if self.isLinear is not True:
            return "Non Linear Perceptron"
        else:
            return "Linear Perceptron"
