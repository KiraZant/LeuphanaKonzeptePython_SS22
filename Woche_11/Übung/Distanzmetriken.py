"""
In Woche 8 haben Sie bereits Distanzmaße kennengelernt, um die Ähnlichkeit von numerischen Vektoren bzw. Datenpunkten zu
bestimmen. Für Wörter gibt es spezielle Distanzmetriken, die im Folgenden implementiert sind.
"""

import numpy as np

def similarity(dok):
    """Berechnet die Summe der Überlappenden Worte zwischen zwei Texteiheiten"""
    matrix = dok.minimum(1.0)
    return matrix @ matrix.T

def cosine_similarity(x, y):
    """ Berechnet die Cosine Ähnlichkeit zwischen zwei Texten"""
    return np.dot(x, y) / (np.sqrt(np.dot(x, x)) * np.sqrt(np.dot(y, y)))

def cosine_distance(x, y):
    return 1 - cosine_similarity(x, y)
