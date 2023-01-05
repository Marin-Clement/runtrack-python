def return_product():
    buffer = 1
    L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
    for n in L:
        if 25 <= n <= 90:
            buffer *= n
    return buffer


# print(return_product())
