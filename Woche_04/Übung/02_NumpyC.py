"""
a. Schreiben Sie eine Funktion, die kleinsten Zahl und deren Index aus der vorgegebenen 4x3 Matrix mit zufälligen
natürlichen Zahlen zwischen 0 und 100 herausgibt. Sie dürfen Numpy Methoden nutzen.
"""
import numpy as np


# Matrix aus Zufallszahlen erstellen
A = np.random.randint(0, 100, (4, 3))
print(A)

def smallest(A):
    pass


"""
b. In der Vorlesung haben Sie das Konzept der Vectorization kennengelernt, die es uns erlaubt Operationen mit dem Array
durchzuführen. Schreiben Sie die Funktion scale(x), die die Werte eines Arrays durch sogenannte Min-Max Skalierung
ausschließlich im Wertebereich zwischen 0 und 1 legt. Der kleinste Wert des originalen Arrays wird also zu 0 und der
größte zu 1. Alle weiteren Werte liegen dazwischen. Die Formel hierfür is im Woche4.md file zu sehen.

Testen Sie Ihre Funktionen mit einem Array mit den Zahlen von 0 bis 10.
"""

def normalize(array):
    pass



