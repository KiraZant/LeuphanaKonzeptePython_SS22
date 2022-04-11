"""
Notation to specify data type of argument and return value
"""


def function(param1: int) -> list:
    result = []
    for i in range(param1):
        result.append(i)

    return result


function(10)
