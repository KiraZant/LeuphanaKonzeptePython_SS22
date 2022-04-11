"""
This code demonstrates side effects when mutable objects are modified inside of a function
"""

# Dictionary
x = {"a": 1, "b": 2}


def foo(a):

    a["b"] = 9
    return a


print(f"Value of x before executing function: {x}")
foo(x)
print(f"Value of x after executing function: {x}")

# List
x = [1, 2, 3]


def foo(a):

    a[0] = 9
    return a


print(f"Value of x before executing function: {x}")
foo(x)
print(f"Value of x after executing function: {x}")


# Integer: Immutable => changes do not affect the original object
x = 1


def foo(a):

    a += 1
    return a


print(f"Value of x before executing function: {x}")
foo(x)
print(f"Value of x after executing function: {x}")
