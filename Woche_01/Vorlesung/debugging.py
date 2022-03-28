"""Debugging Beispiel"""


def eucl_dist(x, y):
    ssq = 0
    for i in range(len(x)):
        ssq += (x[i]-y[i])**2
    return ssq**0.5


def nearest_neighbor(v, points):
    min_dist = float("inf")
    for p in points:
        if eucl_dist(p, v) <= min_dist:
            min_dist = eucl_dist(p, v)
            neighbor = p
    return v, neighbor, min_dist


"""Dieses Beispiel zeigt, dass die Berechnung des Abstandes nicht korrekt ist.
Die korrekte Ausgabe sollte der Punkt [5, 6, 5] sein mit Abstand 1.
"""
x, dist, point = nearest_neighbor([5, 5, 5], [[7, 3, 5], [5, 6, 5], [0, 0, 0]])


'''
Calculate the euclidian distance between two points
:param x: Point 1 as list with vector with n dimensions
:param y: Point 2 with the same dimensions as poin x
:return: Euclidian distance between x and y
'''

#print("Der quadrierte Abstand zwischen {} und {} betraegt {}".format(x, y, ssq))
#print("Aktueller naechster Nachbar ist {} mit Abstand {}".format(neighbor, min_dist))

#print('Der next neighbor zu {} ist {} mit Abstand {}'.format(x,point,dist))
"""Durch die Print Ausgaben sehen wir, dass der Abstand zwischen den Punkten falsch berechnet wird
Der Abstand sollte nicht negativ sein. Richtig waere ssq += (x[i] - y[i])**2 in Zeile 9.
"""
