import numpy as np
from matplotlib import pyplot as plt


def normalize(output):
    outData = np.zeros(len(output))
    maxVal = np.max(output)
    minVal = np.min(output)
    for i in range(len(output)):
        current = (2*(output[i] - minVal)/(maxVal - minVal))-1
        outData[i] = current

    return outData

def parseNumbers(path):
    file = open(path, "r")
    lines = file.read()
    length = len(lines)
    numbers = []
    auxMatrix = []
    i = 0
    line = 0

    while i < length:
        if lines[i] == "0":
            auxMatrix.append(0)
        elif lines[i] == "1":
            auxMatrix.append(1)
        elif lines[i] == "\n":
            if line == 6:
                line = 0
                numbers.append(auxMatrix)
                auxMatrix = []
            else:
                line += 1
        else:  # es un " "
            pass
        i += 1
    return np.array(numbers)

def parseTrainingData(path):
    file = open(path, 'r')
    l = file.readline()
    inputData = []
    while l:
        singleInput = (l.strip('\n')).split('   ')[1:]
        singleInput = list(map(lambda x: float(x), singleInput))
        inputData.append(singleInput)
        l = file.readline()
    file.close()
    print(f'len = {len(inputData[0])}')
    return inputData

def parseOutputData(path):
    file = open(path, 'r')
    l = file.readline()
    outputData = []
    while l:
        data = float(l.strip(' '))
        outputData.append(data)
        l = file.readline()
    file.close()
    return outputData

def appendThreshold(data):
    data = list(map(lambda x: np.append(x, 1), data))
    return data

def plotError(errors):
    x = np.array(range(len(errors)))

    fig, ax = plt.subplots(figsize=(5, 3), layout="constrained")

    ax.set_xlabel("Iteración")
    ax.set_ylabel("Error")
    ax.locator_params("y")
    ax.locator_params("x")
    ax.plot(x, errors, label="Error", color="m")
    ax.set_title("Error por iteraciones")
    ax.legend()
    plt.show()

def plotErrorDouble(train, test):
    x = np.array(range(len(train)))
    y = np.array(range(len(test)))

    fig, ax = plt.subplots(figsize=(5, 3), layout="constrained")

    ax.set_xlabel("Iteración")
    ax.set_ylabel("Error")
    ax.locator_params("y")
    ax.locator_params("x")
    ax.plot(x, train, label="Train", color="m")
    ax.plot(y, test, label="Test", color="c")
    ax.set_title("Error por iteraciones")
    ax.legend()
    plt.show()

def plotAccuracies(training, test):
    x = np.array(range(len(training[1])))

    fig, ax = plt.subplots(figsize=(5, 3), layout="constrained")

    ax.set_xlabel("Época")
    ax.set_ylabel("Accuracy")
    ax.locator_params("y")
    ax.locator_params("x")

    ax.plot(x, test, label="K=0", color="b")
    ax.plot(x, training[1], label="K=1", color="r")
    ax.plot(x, training[2], label="K=2", color="g")
    ax.plot(x, training[3], label="K=3", color="y")
    ax.plot(x, training[4], label="K=4", color="m")
    #ax.plot(x, training[5], label="K=5", color="c")
    #ax.plot(x, training[6], label="K=6", color="k")
    #ax.plot(x, training[7], label="K=7", color="tab:purple")
    #ax.plot(x, training[8], label="K=8", color="tab:orange")
    #ax.plot(x, training[9], label="K=9", color="tab:brown")
    ax.set_title("Accuracy por épocas (error < 0.01)")
    ax.legend()
    plt.show()


def mutate_set(set, mutation_p):
    for elem in set:
        for i in range(len(elem)):
            if np.random.random() < mutation_p:
                elem[i] = (elem[i] + 1) % 2
    return set


def accuracy(trainData, expectedOutput):
    TP = 0
    TN = 0
    FP = 0
    FN = 0
    for i in range(trainData.shape[0]):
        if expectedOutput[i] == -1 and trainData[i] < -0.99:
            TP += 1
        elif expectedOutput[i] == 1 and trainData[i] > 0.99:
            TN += 1
        elif expectedOutput[i] == -1 and trainData[i] > -0.99:
            FN += 1
        elif expectedOutput[i] == 1 and trainData[i] < 0.99:
            FP += 1

    return (TP + TN) / (TP + TN + FN + FP)
