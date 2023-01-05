def max_min():
    L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
    min_value = float("inf")
    max_value = float("-inf")
    for n in L:
        if n < min_value:
            min_value = n
        if n > max_value:
            max_value = n
    return min_value, max_value


# print(max_min())
