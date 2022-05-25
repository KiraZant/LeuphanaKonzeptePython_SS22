import itertools
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

x = np.array([3, 3.5])
y = np.array([.75, 0.25])

# Euclidean distance
d = np.sqrt(np.sum((x - y) ** 2))
fig, axs = plt.subplots()
axs.scatter(x[0], x[1], label='A')
axs.scatter(y[0], y[1], label='B')
plt.plot([x[0], y[0]], [x[1], y[1]], label='Euklidische Distanz', color='black')
axs.legend()
axs.annotate(f'd={np.round(d, 2)}', (2.0, 1.75))
axs.set(xlim=(0, 4), ylim=(0, 4), title='Euklidische Distanz')
fig.savefig(f'Euclidean_Distance.png')
plt.show()

# Manhattan distance
d = np.sum(np.abs((x - y)))
fig, axs = plt.subplots()
axs.scatter(x[0], x[1], label='A')
axs.scatter(y[0], y[1], label='B')
plt.plot([x[0], x[0], y[0]], [x[1], y[1], y[1]], label='Manhattan Distanz', color='black')
axs.legend()
axs.annotate(f'd={np.round(d, 2)}', (1.75, .5))
axs.set(xlim=(0, 4), ylim=(0, 4), title='Manhattan Distanz')
fig.savefig(f'Manhattan_Distance.png')
plt.show()

# Cosine distance
d = 1 - (np.dot(y, x)) / (np.sqrt(np.dot(y, y)) * np.sqrt(np.dot(x, x)))
fig, axs = plt.subplots()
axs.scatter(x[0], x[1], label='A')
axs.scatter(y[0], y[1], label='B')
plt.plot([0, x[0]], [0, x[1]], color='black', label='Ortsvektoren')
plt.plot([0, y[0]], [0, y[1]], color='black')
axs.legend()
axs.annotate(f'd={np.round(d, 2)}', (.75, .5))
axs.set(xlim=(0, 4), ylim=(0, 4), title='Cosine Distanz')
fig.savefig(f'Cosine_Distance.png')
plt.show()

# Selection of distance metrics
fig, axs = plt.subplots()
axs.scatter(x[0], x[1], label='A')
axs.scatter(y[0], y[1], label='B')
axs.scatter(2.5, 2.0, label='?', color='gray')
axs.legend()
axs.set(xlim=(0, 4), ylim=(0, 4), title='Auswahl der Distanzmetrik')
fig.savefig(f'Distance_Metrics_Selection.png')
plt.show()

# Threshold visualization: Manhattan distance
fig, axs = plt.subplots()
axs.scatter(x[0], x[1], label='A', color='orange')
axs.scatter(y[0], y[1], label='B', color='blue')
for i, j in tqdm(itertools.product(np.arange(0, 4, 0.1), np.arange(0, 4, 0.1))):
    p = np.array([i, j])
    if np.sum(np.abs((y - p))) < np.sum(np.abs((x - p))):
        axs.scatter(i, j, color='blue', marker='+')
    else:
        axs.scatter(i, j, color='orange', marker='+')
axs.legend()
axs.set(xlim=(0, 4), ylim=(0, 4), title='Manhattan zu A & B')
fig.savefig(f'Distance_Threshold_Man.png')
plt.show()

# Threshold visualization: Euclidean distance
fig, axs = plt.subplots()
axs.scatter(x[0], x[1], label='A', color='orange')
axs.scatter(y[0], y[1], label='B', color='blue')
for i, j in tqdm(itertools.product(np.arange(0, 4, 0.1), np.arange(0, 4, 0.1))):
    p = np.array([i, j])
    if np.sqrt(np.sum((y - p) ** 2)) < np.sqrt(np.sum((x - p) ** 2)):
        axs.scatter(i, j, color='blue', marker='+')
    else:
        axs.scatter(i, j, color='orange', marker='+')
axs.legend()
axs.set(xlim=(0, 4), ylim=(0, 4), title='Euclidean zu A & B')
fig.savefig(f'Distance_Threshold_Euc.png')
plt.show()

# Threshold visualization: Euclidean distance VS.Manhattan distance
fig, axs = plt.subplots()
axs.scatter(x[0], x[1], label='A', color='orange')
axs.scatter(y[0], y[1], label='B', color='blue')
for i, j in tqdm(itertools.product(np.arange(0, 4, 0.1), np.arange(0, 4, 0.1))):
    p = np.array([i, j])
    if np.sqrt(np.sum((y - p) ** 2)) < np.sum(np.abs((x - p))):
        axs.scatter(i, j, color='blue', marker='+')
    else:
        axs.scatter(i, j, color='orange', marker='+')
axs.legend()
axs.set(xlim=(0, 4), ylim=(0, 4), title='Manhatten zu A & Euclidean zu B')
fig.savefig(f'Distance_Threshold_ManEuc.png')
plt.show()

# Threshold visualization: Manhattan distance VS Euclidean Distance
fig, axs = plt.subplots()
axs.scatter(x[0], x[1], label='A', color='orange')
axs.scatter(y[0], y[1], label='B', color='blue')
for i, j in tqdm(itertools.product(np.arange(0, 4, 0.1), np.arange(0, 4, 0.1))):
    p = np.array([i, j])
    if np.sum(np.abs((y - p))) < np.sqrt(np.sum((x - p) ** 2)):
        axs.scatter(i, j, color='blue', marker='+')
    else:
        axs.scatter(i, j, color='orange', marker='+')
axs.legend()
axs.set(xlim=(0, 4), ylim=(0, 4), title='Euclidean zu A & Manhatten zu B')
fig.savefig(f'Distance_Threshold_EucMan.png')
plt.show()
