def alpha():
    word = "abcde"
    letters = []
    n = 1
    check = False

    for w in word:
        letters.append(w.lower())
    while not check:
        if ord(letters[-n]) >= ord(letters[-(n + 1)]):
            letters[-n], letters[-(n + 1)] = letters[-(n + 1)], letters[-n]
            check = True
        else:
            n += 1
    return letters


print(alpha())

