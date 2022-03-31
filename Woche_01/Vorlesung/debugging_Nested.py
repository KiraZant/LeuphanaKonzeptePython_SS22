"""Debugging Beispiel mit zwei Funktionen - Kein Fehler vorhanden"""

def eucl_dist(x, y):
    '''
    Calculate the euclidian distance between two points
    :param x: Point 1 as list with vector with n dimensions
    :param y: Point 2 with the same dimensions as point x
    :return: Euclidian distance between x and y
    '''
    ssq = 0
    for i in range(len(x)):
        ssq += (x[i]-y[i])**2
    return ssq**0.5


def nearest_neighbor(v, points):
    '''
        Find the nearest point to v from a list of possible points
        :param v: Point in question
        :param y: List of points with the same dimensions as point x
        :return: The point, the nearest neighbor and their distance
        '''
    min_dist = float("inf")
    for p in points:
        if eucl_dist(p, v) <= min_dist:
            min_dist = eucl_dist(p, v)
            neighbor = p
    return v, neighbor, min_dist


x, dist, point = nearest_neighbor([5, 5, 5], [[7, 3, 5], [5, 6, 5], [0, 0, 0]])
print('Der next neighbor zu {} ist {} mit Abstand {}'.format(x,point,dist))
