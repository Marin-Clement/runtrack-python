def sum_even():
    total = 0
    L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]
    for n in L:
        if n % 2 == 0:
            total += n
    return total


print(sum_even())
