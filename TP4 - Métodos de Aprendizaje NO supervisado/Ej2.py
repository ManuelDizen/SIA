import matplotlib.pyplot as plt
import numpy as np
import random
import seaborn as sns

EPSILON_NOISE = 0.5
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
            [1,1,1,1,1, -1,-1,-1,1,-1, -1,-1,-1,1,-1, 1,-1,-1,1,-1, 1,1,1,1,-1],
            [1,-1,-1,-1,1, 1,-1,-1,1,-1, 1,1,1,-1,-1, 1,-1,-1,1,-1, 1,-1,-1,-1,1],
            [1,-1,-1,-1,-1, 1,-1,-1,-1,-1, 1,-1,-1,-1,-1, 1,-1,-1,-1,-1, 1,1,1,1,1],
            [1,-1,-1,-1,1, 1,1,-1,1,1, 1,-1,1,-1,1, 1,-1,-1,-1,1, 1,-1,-1,-1,1],
            [1,-1,-1,-1,1, 1,1,-1,-1,1, 1,-1,1,-1,1, 1,-1,-1,1,1, 1,-1,-1,-1,1],
            [1,1,1,1,1, 1,-1,-1,-1,1, 1,-1,-1,-1,1, 1,-1,-1,-1,1, 1,1,1,1,1],
            [1,1,1,1,1, 1,-1,-1,-1,1, 1,1,1,1,1, 1,-1,-1,-1,-1, 1,-1,-1,-1,-1],
            [1,1,1,1,1, 1,-1,-1,-1,1, 1,-1,-1,-1,1, 1,-1,-1,1,1, 1,1,1,1,1],
            [1,1,1,1,1, 1,-1,-1,-1,1, 1,1,1,1,1, 1,-1,-1,1,-1, 1,-1,-1,-1,1],
            [1,1,1,1,1, 1,-1,-1,-1,-1, 1,1,1,1,1, -1,-1,-1,-1,1, 1,1,1,1,1],
            [1,1,1,1,1, -1,-1,1,-1,-1, -1,-1,1,-1,-1, -1,-1,1,-1,-1, -1,-1,1,-1,-1],
            [1,-1,-1,-1,1, 1,-1,-1,-1,1, 1,-1,-1,-1,1, 1,-1,-1,-1,1, 1,1,1,1,1],
            [1,-1,-1,-1,1, 1,-1,-1,-1,1, -1,1,-1,1,-1, -1,1,-1,1,-1, -1,-1,1,-1,-1],
            [1,-1,-1,-1,1, 1,-1,-1,-1,1, 1,-1,-1,-1,1, 1,-1,1,-1,1, 1,1,-1,1,1],
            [1,-1,-1,-1,1, -1,1,-1,1,-1, -1,-1, 1,-1,-1, -1, 1, -1, 1, -1, 1,-1,-1,-1,1],
            [1,-1,-1,-1,1, -1,1,-1,1,-1, -1,-1,1,-1,-1, -1,-1,1,-1,-1, -1,-1,1,-1,-1],
            [1,1,1,1,1, -1,-1,-1,1,-1, -1,-1,1,-1,-1, -1,1,-1,-1,-1, 1,1,1,1,1]
            ]
alphabet_chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                  'p','q','r','s','t','u','v','w','x','y','z']

similar_letters = [alphabet[2], alphabet[4], alphabet[6], alphabet[14]] # c,e,g,o
orthogonal_letters = [alphabet[14], alphabet[-3], alphabet[10], alphabet[-5]] # o, x, k, v

def pickLetters():
    lettersReturn = np.empty((N_LETTERS,25), dtype=int)
    for i in range(0,N_LETTERS):
        p = random.randint(0,len(alphabet)-1) # No debería dar una lista circular nunca, tomo 5 de mas de 5
        #while alphabet[p] in lettersReturn.tolist():
        #    p += 1
        while alphabet[p] in lettersReturn.tolist():
            p = p+1
            if p == len(alphabet)-1:
                p = 0
        lettersReturn[i] = alphabet[p]
        print(f'Letra pickeada: {alphabet_chars[p]}, ({lettersReturn[i]})')
    return lettersReturn

def calculateWeights(letters):
    matrix = np.zeros((len(letters[0]), len(letters[0])))
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

def printLetter(letter):
    arr = np.array(letter)
    test = np.array_split(letter, 5)
    #print(test)
    aux = len(test)
    for line in range(0, aux):
        str = ''
        for i in range(0, len(test[0])):
            if test[line][i] == 1:
                str = str + '*'
            else:
                str = str + ' '
        print(str)

def printLetterHeatmap(letter):
    data = [letter[0:5], letter[5:10], letter[10:15], letter[15:20], letter[20:25]]
    plt.figure(figsize=(10, 10))
    heat_map = sns.heatmap(data, linewidth=1, annot=False, cmap="Greens")
    plt.show()

def hopfield(name):
    #letters = pickLetters()
    letters = orthogonal_letters

    # ya pickee las letras    matched = 0
    weights = calculateWeights(letters)
    aux1 = pickRandomLetterFromPatterns(letters)
    originalLetter = np.copy(aux1)
    inputValue = randomLetterWithNoise(aux1)
    prevState = inputValue
    actualState = np.zeros(len(prevState))
    iterations = 0

    #printLetterHeatmap(prevState)

    matched = 0
    counter = 0
    while np.array_equal(prevState,actualState) == False:
        for i in range(0, len(inputValue)):
            sum = 0
            for j in range(0, len(inputValue)):
                if i != j:
                    sum += weights[i][j]*prevState[j]
            h_i = int(np.sign(sum)) if sum != 0 else 0
            actualState[i] = h_i
        #printLetterHeatmap(actualState)

        if np.array_equal(prevState,actualState):
            #print(f'Patrón matcheado: {actualState}')
            break
        else:
            prevState = actualState
            actualState = np.zeros(len(prevState))
        counter += 1
        if counter >= 5:
            print(f'Itere mucho. Mi letra actual es: {prevState}')
            break
        #print(actualState)
    actualState = actualState.astype(int)
    #print(f'ActualState: {actualState}')
    #print(f'OriginalLetter: {originalLetter}')

    #print('Letra input con ruido: ')
    #printLetter(inputValue)
    #print('Resultado de Hopfield: ')
    #printLetter(actualState)
    #print('Resultado de letra original: ')
    #printLetter(originalLetter)

    if np.array_equal(originalLetter,actualState):
        print('Se devolvió el patrón correcto')
        matched = 1
    else:
        print('Se devolvió el patrón incorrecto')
    return matched

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    iterations = 500
    hits = 0
    for i in range(0, iterations):
        hits += hopfield("hola")
    print(f'Hits/Totales: {hits}/{iterations}')
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
