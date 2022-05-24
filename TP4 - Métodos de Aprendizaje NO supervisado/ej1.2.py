import pandas as pd
import plotting
from src.kohonenNetwork import kohonenNetwork
from sklearn.preprocessing import StandardScaler
from plotting import *

df = pd.read_csv("europe.csv")

labels = df[df.columns[0]].to_numpy()
inputs = df.loc[:, ["Area", "GDP", "Inflation", "Life.expect", "Military", "Pop.growth", "Unemployment"]].values
inputs = StandardScaler().fit_transform(inputs)

learnRate = 0.1
#w = np.zeros(len(inputs[0]))
w = np.random.rand(len(inputs[0]))
print(f'w inicial = {w}')
nOfIterations = 500

outputWs = np.empty(shape=(nOfIterations, len(inputs[0])))
print(f'outputWs inicial = {outputWs}')
for iter in range(0, nOfIterations):
    for i in range(0, len(inputs)):
        s = 0
        for j in range(0, len(inputs[i])):
            s += inputs[i][j] * w[j]
        #print(f'Previous w: {w}')
        w = w + learnRate*s*(inputs[i] - s*w)
        #print(f'New w= {w}, Delta_w={learnRate*s*(inputs[i] - s*w)}')
    outputWs[iter] = w

print(f'{outputWs[-1]}\nshape={outputWs.shape}')