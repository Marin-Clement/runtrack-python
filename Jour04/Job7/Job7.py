def multiple_of_3():
    count = 0
    L = [8, 24, 48, 2, 16]
    for n in L:
        if n % 3 == 0:
            count += 1
    return count


print(multiple_of_3())
