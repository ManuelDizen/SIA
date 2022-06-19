import numpy as np
import matplotlib.pyplot as plt

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

def graph_digits(original, output):
    fig, (ax1, ax2) = plt.subplots(1, 2)
    for i in range(len(output)):
        ax1.set_title('Original')
        ax2.set_title('AE result')
        ax1.imshow(np.array(original[i-1]).reshape((7, 5)), cmap='gray')
        ax2.imshow(np.array(output[i-1]).reshape((7, 5)), cmap='gray')
        fig.show()
