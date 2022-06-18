import numpy as np

def printLetter(letter):
    arr = np.array(letter)
    test = np.array_split(letter, 5)
    aux = len(test)
    for line in range(0, aux):
        str = ''
        for i in range(0, len(test[0])):
            if test[line][i] > 0.5:
                str = str + '*'
            else:
                str = str + ' '
        print(str)