def return_list():

    L = [1, 2, 3, 4, 5]
    print(L[1])
    L = ReplaceInt(L, 3)
    print(L[-1])
    print(L)


def ReplaceInt(list, index):
    list[index] = list[index - 1] + list[index + 1]
    return list


return_list()
