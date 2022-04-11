"""
Demonstrate local and global scope
"""

x = 2


def foo(y):
    x = 41
    z = 5
    print(locals())
    print(globals()["x"])
    print(x, y, z)


foo(3)
