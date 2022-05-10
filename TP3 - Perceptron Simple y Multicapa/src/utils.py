import numpy as np
from matplotlib import pyplot as plt


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
        else:
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
    ax.plot(x, errors, label="Error", color="r")
    ax.set_title("Error por cantidad de iteraciones")
    ax.legend()
    plt.show()

