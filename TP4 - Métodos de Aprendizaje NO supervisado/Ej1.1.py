import pandas as pd

import plotting
from src.kohonenNetwork import *
from src.pairs import *
from sklearn.preprocessing import StandardScaler
import plotting

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

for i in range(len(pairArr)):
    # if p.label1 == 'Ukr':
    if i % 2 == 0:
        print(f'{i/2 + 1}: {pairArr[i]}')

#  print(len(pairArr))

k = 3
r_0 = k
n0 = 0.8

network = kohonenNetwork(k, r_0, False, n0, inputs, labels, True)

matrix = []
for i in range(0, len(network.grid)):
    row = []
    for j in range(0, len(network.grid[0])):
        row.append(network.grid[i][j].matched)
        print(f'{i}, {j}: {network.grid[i][j].entriesMatched}')
    matrix.append(row)


matrixNames = []
for i in range(0, len(network.grid)):
    row = []
    for j in range(0, len(network.grid[0])):
        names = ""
        for name in network.grid[i][j].entriesMatched:
            names += f'{name}\n'
        row.append(names)
    matrixNames.append(row)

plotting.print_heatmap(matrix, matrixNames, "Grilla inicial")

for i in range(0, len(network.grid)):
    for j in range(0, len(network.grid[0])):
        network.grid[i][j].clear()

network.train(inputs, labels)

network.test(inputs, labels)

matrix = []
for i in range(0, len(network.grid)):
    row = []
    for j in range(0, len(network.grid[0])):
        row.append(network.grid[i][j].matched)
        print(f'{i}, {j}: {network.grid[i][j].entriesMatched}')
    matrix.append(row)


matrixNames = []
for i in range(0, len(network.grid)):
    row = []
    for j in range(0, len(network.grid[0])):
        names = ""
        for name in network.grid[i][j].entriesMatched:
            names += f'{name}\n'
        row.append(names)
    matrixNames.append(row)

plotting.print_heatmap(matrix, matrixNames, "Países agrupados según características")

matrix2 = []
for i in range(0, len(network.grid)):
    row = []
    for j in range(0, len(network.grid[0])):
        acum = 0
        count = 0
        for x in range(i - 1, i + 2):
            for y in range(j - 1, j + 2):
                if 0 <= x < k and 0 <= y < k and math.hypot(i - x, j - y) <= 1 and (x != i or y != j):
                    acum += network.grid[i][j].distanceTo(network.grid[x][y].weights)
                    count += 1
        acum /= count
        row.append(acum)
    matrix2.append(row)

plotting.print_heatmap(matrix2, None, "Matriz U")

matrix3 = []
for x in range(0, k):
    row = []
    for y in range(0, k):
        if x != 0 or y != 0:
            row.append(network.grid[0][0].distanceTo(network.grid[x][y].weights))
        else:
            row.append(0)
    matrix3.append(row)

plotting.print_heatmap(matrix3, None, "Distancia de (0,0) a otras neuronas")

