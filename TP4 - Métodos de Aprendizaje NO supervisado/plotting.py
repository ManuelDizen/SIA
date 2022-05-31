import numpy as np
import seaborn as sns
import matplotlib.pylab as plt

plt.style.use("seaborn")


def print_heatmap(matrix, names=None, title=None):

    sns.set(font_scale=0.6)
    plt.figure(figsize=(len(matrix), len(matrix[0])))
    heat_map = sns.heatmap(matrix, annot=names, linewidth=1, fmt="", cmap='RdYlGn')

    plt.title(title)

    plt.show()
