
# Syntax Error
def even(n):
    if n % 2 == 0:
        print("Even number")
    else
        print("Odd number')


# Runtime Error - Bsp 1
def division(x, y):
    return x/y

result_dev = division(2, 0)
print(result_dev)

# Runtime Error - Bsp 2
def scalar(list1, list2):
    erg = 0
    for i in range(len(list1)):
        erg += list1[i] + list2[i]
    return erg

result_sca = scalar([1, 2, 3, 4], [1, 2, 3])
print(result_sca)


# Semantic Error
def sum_squares(n):
    sum = 0
    for i in range(n+1):
        i_square = i**2
    sum += i_square
    return sum

print(sum_squares(3)) # sollte 1+4+9 = 14 sein
