"""Schreiben Sie eine Funktion, die für den Punkt x eine beliebige Funktion aus dem Distanzfunktion.py Datei nimmt und
aus einem Numpy Array beliebig viele andere Punkte den 1) zu x am nächsten liegenden Punkt y, 2) den Abstand zwischen x
und diesem Punkt y und 3) dessen Index in dem Array der Optionen ausgibt.

Hinweis: Versuchen Sie diese Aufgabe ohne for-loop zu lösen.
"""
from sklearn import datasets


def optimize():
    """
    """
    pass


# 1. Test Case Numpy

#options = np.array([[1, 2, 8], [3, 4, 5], [1, 2, 11]])
#x = np.array([1, 2, 9])
#print(optimize(euclidean_distance, x, options))  # (array([1, 2, 8]), 1.0, 0)

# 2. Test Case Iris
# Wir laden das Iris Dataset von sklearn (https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/)

#dataset = datasets.load_iris().data

# Wir nehmen den Punkt in der ersten Reihe und finden den nächsten Punkt aus allen anderen Punkten

#print(optimize(euclidean_distance, dataset[0], dataset[1:]))