from Jour04.Job12.Job12 import sort_list

numbers = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]


def round_list(n):
    round_number = []
    for i in n:
        if int(i) <= i - 0.50:
            round_number = round_number + [int(i) + 1]
        else:
            round_number = round_number + [int(i)]
    return sort_list(round_number)


# print(round_list(numbers))



