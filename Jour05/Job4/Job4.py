def decal():
    sentence = input("phrase: ")
    key = int(input("Valeur de décalage: "))

    mapping = {}

    for i in range(26):
        i_ceasar = (i + key) % 26
        letter_ceasar = chr(i_ceasar + ord('a'))

        letter = chr(i + ord('a'))
        mapping[letter] = letter_ceasar

    result = ""
    for letter in sentence:
        result = result + mapping[letter]
    print(result)

decal()
