"""
Live coding task + solution
"""


# Solution using for loops
def length_of_all_elements(lst):
    return_list = []
    for name in lst:
        return_list.append(len(name))
    return return_list


print(length_of_all_elements(["Michael", "Anna", "Ali"]))  # -> [7, 4, 3]


# Solution using map
def length_of_all_elements_map(lst):
    # type-casting the return value of map function to list
    return list(map(len, lst))


# Solution using list comprehensions
def length_of_all_elements_map(lst):
    return [len(name) for name in lst]
