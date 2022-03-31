"""Debugging Beispiel mit einer einfachen Funktionen"""

def sum_squares(n):
    sum = 0
    for i in range(n+1):
        i_square = i**2
    sum += i_square
    return sum

print(sum_squares(3)) # sollte 1+4+9 = 14 sein