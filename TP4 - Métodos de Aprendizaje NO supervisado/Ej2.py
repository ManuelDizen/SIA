import matplotlib.pyplot as plt
import numpy as np
import random

EPSILON_NOISE = 0.01
N_LETTERS = 4

alphabet = [[1,1,1,1,1, 1,-1,-1,-1,1, 1,-1,-1,-1,1, 1,-1,-1,-1,1, 1,1,1,1,1],
            [1,1,1,1,-1, 1,-1,-1,-1,1, 1,1,1,1,-1, 1,-1,-1,-1,1, 1,1,1,1,-1],
            [-1,1,1,1,-1, 1,-1,-1,-1,1, 1,-1,-1,-1,-1, 1,-1,-1,-1,1, -1,1,1,1,-1],
            [1,1,1,1,-1, 1,-1,-1,-1,1, 1,-1,-1,-1,1, 1,-1,-1,-1,1, 1,1,1,1,-1],
            [1,1,1,1,1, 1,-1,-1,-1,-1, 1,1,1,-1,-1, 1,-1,-1,-1,-1, 1,1,1,1,1],
            [1,1,1,1,1, 1,-1,-1,-1,-1, 1,1,1,1,-1, 1,-1,-1,-1,-1, 1,-1,-1,-1,-1],
            [1,1,1,1,1, 1,-1,-1,-1,-1, 1,-1,1,1,1, 1,-1,-1,-1,1, 1,1,1,1,1],
            [1,-1,-1,-1,1, 1,-1,-1,-1,1, 1,1,1,1,1, 1,-1,-1,-1,1, 1,-1,-1,-1,1],
            [1,1,1,1,1, -1,-1,1,-1,-1, -1,-1,1,-1,-1, -1,-1,1,-1,-1, 1,1,1,1,1],
            [1,1,1,1,1, -1,-1,-1,1,-1, -1,-1,-1,1,-1, 1,-1,-1,1,-1, 1,1,1,-1,-1],
            [1,-1,-1,-1,1, 1,-1,-1,1,-1, 1,1,1,-1,-1, 1,-1,-1,1,-1, 1,-1,-1,-1,1],
            [1,-1,-1,-1,-1, 1,-1,-1,-1,-1, 1,-1,-1,-1,-1, 1,-1,-1,-1,-1, 1,1,1,1,1],
            [1,-1,-1,-1,1, 1,1,-1,1,1, 1,-1,1,-1,1, 1,-1,-1,-1,1, 1,-1,-1,-1,1],
            [1,-1,-1,-1,1, 1,1,-1,-1,1, 1,-1,1,-1,1, 1,-1,-1,1,1, 1,-1,-1,-1,1],
            [1,1,1,1,1, 1,-1,-1,-1,1, 1,-1,-1,-1,1, 1,-1,-1,-1,1, 1,1,1,1,1],
            [1,1,1,1,1, 1,-1,-1,-1,1, 1,1,1,1,1, 1,-1,-1,-1,-1, 1,-1,-1,-1,-1],
            [1,1,1,1,-1, 1,-1,-1,1,-1, 1,-1,-1,1,-1, 1,1,1,1,-1, -1,-1,-1,-1,1],
            [1,1,1,1,1, 1,-1,-1,-1,1, 1,1,1,1,1, 1,-1,-1,1,-1, 1,-1,-1,-1,1],
            [1,1,1,1,1, 1,-1,-1,-1,-1, 1,1,1,1,1, -1,-1,-1,-1,1, 1,1,1,1,1],
            [1,1,1,1,1, -1,-1,1,-1,-1, -1,-1,1,-1,-1, -1,-1,1,-1,-1, -1,-1,1,-1,-1],
            [1,-1,-1,-1,1, 1,-1,-1,-1,1, 1,-1,-1,-1,1, 1,-1,-1,-1,1, 1,1,1,1,1],
            [1,-1,-1,-1,1, 1,-1,-1,-1,1, -1,1,-1,1,-1, -1,1,-1,1,-1, -1,-1,1,-1,-1],
            [1,-1,-1,-1,1, 1,-1,-1,-1,1, 1,-1,-1,-1,1, 1,-1,1,-1,1, 1,1,-1,1,1],
            [1,-1,-1,-1,1, -1,1,-1,1,-1, -1,-1,1,-1,-1, -1,1,-1,1,-1, 1,-1,-1,-1,1],
            [1,-1,-1,-1,1, -1,1,-1,1,-1, -1,-1,1,-1,-1, -1,-1,1,-1,-1, -1,-1,1,-1,-1],
            [1,1,1,1,1, -1,-1,-1,1,-1, -1,-1,1,-1,-1, -1,1,-1,-1,-1, 1,1,1,1,1]
            ]
alphabet_chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                  'p','q','r','s','t','u','v','w','x','y','z']

#TODO: Revisar la K

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def pickLetters():
    lettersReturn = np.empty((N_LETTERS,25), dtype=int)
    for i in range(0,N_LETTERS):
        p = random.randint(0,len(alphabet)-1) # No debería dar una lista circular nunca, tomo 5 de mas de 5
        #while alphabet[p] in lettersReturn.tolist():
        #    p += 1
        while alphabet[p] in lettersReturn.tolist():
            p = p+1
            if p == len(lettersReturn):
                p = 0
        lettersReturn[i] = alphabet[p]
        print(f'Letra pickeada: {alphabet_chars[p]}, ({lettersReturn[i]})')
    return lettersReturn

#def calculateOrthogonality(matrix):
#    orth = 0
#    lastVector = None
#    for i in range(0, len(matrix)-1):
#        orth += np.dot(matrix[i], matrix[i+1])
#        lastVector =

def calculateWeights(letters):
    matrix = np.zeros((len(letters[0]), len(letters[0])))
    #matrix = [[de 25], [de 25], ... , [de 25]]
#TODO

    # Las entradas son las letters[i] (osea los E_i)
    for i in range(0, len(letters[0])):
        for j in range(i, len(letters[0])):
            if i == j:
                matrix[i][j] = 0
                matrix[j][i] = 0
            else:
                sum = 0.0
                for element in range(0, len(letters)-1):
                    sum += (letters[element][i] * letters[element][j])
                matrix[i][j] = sum / len(letters[0])
                matrix[j][i] = matrix[i][j]
    return matrix

def randomLetterWithNoise(selected):
    for i in range(0, len(selected)):
        p = np.random.uniform()
        if p < EPSILON_NOISE:
            selected[i] = -1 if selected[i] == 1 else 1

    return selected

def pickRandomLetterFromPatterns(letters):
    n = random.randint(0, len(letters)-1)
    selected = letters[n]
    print("\n" + f'Letra seleccionada: {selected}')
    return selected

def hopfield(name):
    letters = pickLetters()
    # Aca me cree la función pickLetters para que sea random, pero es cierto
#    ort = calculateOrthogonality(letters)
# TODO: calculatOrthogonality(letters)

    # ya pickee las letras
    weights = calculateWeights(letters)
    #print(weights)
    aux1 = pickRandomLetterFromPatterns(letters)
    originalLetter = np.copy(aux1)
    inputValue = randomLetterWithNoise(aux1)
    #print(f'Letra con ruido: {inputValue}')
    prevState = inputValue
    actualState = np.zeros(len(prevState))
    iterations = 0

    while np.array_equal(prevState,actualState) == False:
        for i in range(0, len(inputValue)):
            sum = 0
            for j in range(0, len(inputValue)):
                if i != j:
                    sum += weights[i][j]*prevState[j]
            aux = int(np.sign(sum))
            actualState[i] = aux
        if np.array_equal(prevState,actualState):
            #print(f'Patrón matcheado: {actualState}')
            break
        else:
            prevState = actualState
            actualState = np.zeros(len(prevState))
        #print(actualState)
    actualState = actualState.astype(int)
    print(f'ActualState: {actualState}')
    print(f'OriginalLetter: {originalLetter}')

    if np.array_equal(originalLetter,actualState):
        print('Se devolvió el patrón correcto')
    else:
        print('Se devolvió el patrón incorrecto')
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    hopfield('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
