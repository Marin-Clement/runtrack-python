word = input("Word: ")

count = 0

e_Dic = ["E", "e", "Æ", "È", "É", "Ê", "Ë", "è", "é", "ê", "ë"]


class Colors:
    OKGREEN = "\033[92m"
    HIGHLIGHT = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"


for letter in word:
    if letter in e_Dic:
        count += 1
        print(Colors.HIGHLIGHT + letter.upper() + Colors.ENDC, "<--", Colors.FAIL + str(count) + Colors.ENDC)
    else:
        print(letter)

if count > 0:
    print(Colors.OKGREEN + str(count > 0))
else:
    print(Colors.FAIL + str(count > 0))
