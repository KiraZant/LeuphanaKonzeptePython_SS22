def fakultät(n):
    # Basisfall
    if n == 1:
        return 1
    # Rekursiver Aufruf
    else:
        return n * fakultät(n-1)    # Bsp: 6! = 5! * 6


def fakultät_iterativ(n):
    result = 1
    for i in range(n, 1, -1):
        result *= i
    return result


print(fakultät_iterativ(4))
#fakultät(0)
