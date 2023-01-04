alphabet = "abcdefghijklmnopqrstuvwxyz" * 10


pyramidList = []

i = 0

while i < len(alphabet):

    line = alphabet[i: i + len(pyramidList) + 1]

    if len(line) == len(pyramidList) + 1:
        pyramidList.append(line)

    i += len(line)

for line in pyramidList:
    print(line)
