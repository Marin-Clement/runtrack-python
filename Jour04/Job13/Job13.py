def remove_dup():

    list = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]

    elements = []

    for n in list:
        if n not in elements:
            elements = elements + [n]
        else:
            continue
    list = elements
    return list


# print(remove_dup())
