import pandas as pd

import plotting
from src.kohonenNetwork import *
from src.pairs import *
from sklearn.preprocessing import StandardScaler
from plotting import *

df = pd.read_csv("europe.csv")

labels = df[df.columns[0]].to_numpy()

for i in range(len(labels)):
    if labels[i] == 'Slovakia':
        labels[i] = 'Svk'
    elif labels[i] == 'Slovenia':
        labels[i] = 'Svn'
    elif labels[i] == 'United Kingdom':
        labels[i] = 'UK'
    else:
        labels[i] = labels[i][0:3:1]

inputs = df.loc[:, ["Area", "GDP", "Inflation", "Life.expect", "Military", "Pop.growth", "Unemployment"]].values
inputs = StandardScaler().fit_transform(inputs)
#print(labels)
#print(len(labels))
#inputs = df[["Area", "GDP", "Inflation", "Life.expect", "Military", "Pop.growth", "Unemployment"]].to_numpy()

#print(inputs)

pairArr = []

for i in range(len(inputs)):
    for j in range(len(inputs)):
        if i != j:
            pairArr.append(pairs(labels[i], labels[j], inputs[i], inputs[j]))

def getDist(obj):
    return obj.dist

pairArr.sort(key=getDist)


k = 4
r_0 = k
n0 = 0.5

network = kohonenNetwork(k, r_0, False, n0, inputs)
network.train(inputs, labels)
network.test(inputs, labels)

matrix = []
for i in range(0, len(network.grid)):
    row = []
    for j in range(0, len(network.grid[0])):
        row.append(network.grid[i][j].matched)
    matrix.append(row)
plotting.print_heatmap(matrix)

matrixNames = []
for i in range(0, len(network.grid)):
    row = []
    for j in range(0, len(network.grid[0])):
        names = ""
        for name in network.grid[i][j].entriesMatched:
            names += f'{name}\n'
        row.append(names)
    matrixNames.append(row)

plotting.print_heatmap(matrix, matrixNames)
