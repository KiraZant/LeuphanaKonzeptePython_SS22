"""
Live Coding task + solution
"""


# Solution with for loops
def starts_with_m(lst):
    return_list = []
    for name in lst:
        if name[0].upper() == "M":
            return_list.append(name)
    return return_list


print(starts_with_m(["Michael", "Anna", "Ali"])) # -> ["Michael"]


# Filter solution
def filter_function(word):
    return word[0].upper() == "M"


def start_with_m_filter(lst):
    # type-casting the return value of filter function to list
    return list(filter(filter_function, lst))


# List comprehensions
def start_with_m_lc(lst):
    return [name for name in lst if name[0].upper() == "M"]
