import pandas as pd
import plotting
from matplotlib import pyplot as plt
from src.kohonenNetwork import kohonenNetwork
from sklearn.preprocessing import StandardScaler
from plotting import *

df = pd.read_csv("europe.csv")
desired = ["Area", "GDP", "Inflation", "Life.expect", "Military", "Pop.growth", "Unemployment"]
labels = df[df.columns[0]].to_numpy()
inputs = df.loc[:, desired].values
inputs = StandardScaler().fit_transform(inputs)

learnRate = 0.001
nOfIterations = 5000

w = np.random.uniform(-1,1,len(inputs[0]))
outputWs = np.empty(shape=(nOfIterations, len(inputs[0])))
for epoch in range(0, nOfIterations):
    for i in range(0, len(inputs)):
        s = 0
        for j in range(0, len(inputs[i])):
            s += inputs[i][j] * w[j]
        w = w + learnRate*s*(inputs[i] - s*w)
    outputWs[epoch] = w

print(outputWs[-1])
str = "Autovector = "
for i in range(0, len(outputWs[-1])):
    if outputWs[-1][i] >= 0:
        str = str + " + "
    str = str + f'{outputWs[-1][i]} X{i+1} ({desired[i]})'
print(str)

columns = []
for i in range(0, len(outputWs[0])):
    columns.append(outputWs[:,i])

x = np.array(range(nOfIterations))
fig, ax = plt.subplots(figsize=(6, 4))
for i in range(0, len(outputWs[0])):
    ax.plot(x, columns[i], label=desired[i])
plt.title('Valor de cada Wi (η = 0.001)')
plt.xlabel('Epoch')
plt.ylabel('Valor')
plt.ylim([-0.8,0.8])
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

# Put a legend to the right of the current axis
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
#plt.legend(loc='best')
plt.show()

total = []
for i in range(0, len(inputs)):
    sum = 0
    for j in range(0, len(inputs[i])):
        sum += inputs[i][j] * columns[j]
    total.append(sum)

sum2 = np.sum(total)
print(f'sum2 = {sum2}')



