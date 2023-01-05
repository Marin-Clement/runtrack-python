def sort_list(list):

    length = 0
    for i in list:
        length += 1

    for i in range(1, length):
        buffer = list[i]
        j = i-1
        while j >= 0 and buffer < list[j]:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = buffer
    return list


# print(sort_list([6, 5, 3, 1, 8, 7, 2, 4]))

# Commenter print() apres utilisation car sort_list() est importer dans pour Job15 (evite un double output dans la console pendant le job 15)

