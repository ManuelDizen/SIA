import pandas as pd

import plotting
from src.kohonenNetwork import kohonenNetwork
from sklearn.preprocessing import StandardScaler
from plotting import *

df = pd.read_csv("europe.csv")

labels = df[df.columns[0]].to_numpy()
inputs = df.loc[:, ["Area", "GDP", "Inflation", "Life.expect", "Military", "Pop.growth", "Unemployment"]].values
inputs = StandardScaler().fit_transform(inputs)
#print(labels)
#print(len(labels))
#inputs = df[["Area", "GDP", "Inflation", "Life.expect", "Military", "Pop.growth", "Unemployment"]].to_numpy()

#print(inputs)

k = 10
r_0 = 10
n0 = 1

network = kohonenNetwork(k, r_0, False, n0, inputs)
network.train(inputs, labels)

matrix = []
for i in range(0, len(network.grid)):
    row = []
    for j in range(0, len(network.grid[0])):
        row.append(network.grid[i][j].matched)
    matrix.append(row)
plotting.print_heatmap(matrix)
