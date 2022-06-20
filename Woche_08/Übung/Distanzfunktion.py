"""
Implementieren Sie die in der Vorlesung vorgestellte a) Euklidische und b) Manhatten Distanz als Funktion um die Distanz
zwischen zwei Punkten x und y zu berechnen.

Hinweis: Nutzen Sie die Möglichkeiten von numpy Rechenoperationen über ganze
Arrays hinweg zu vollführen (Vectorization), wie in VL 4 besprochen wurden. Wenn Sie dies
sinnvoll anwenden, sind die Funktionen in jeweils einer Zeile Code möglich.
"""
# Pakete importieren
import numpy as np
#a)
def euclidean_distance(x, y):
    return np.sqrt(np.sum(np.square(x-y)))

#b)
def manhattan_distance(x, y):
    return np.sum(np.abs(x-y))


# Test Case
#x = np.array([2, 3, 4])
#y = np.array([4, 5, 6])

#print(euclidean_distance(x, y))  # 3.46
#print(manhattan_distance(x, y))  # 6
