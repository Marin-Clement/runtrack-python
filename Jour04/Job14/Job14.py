def my_long_word(n, s):

    current_word = ""
    words = []

    for word in s:
        if word == " ":
            words = words + [current_word]
            current_word = ""
        else:
            current_word += word
    if current_word:
        words.append(current_word)

    long_words = [word for word in words if check_world_length(word) > n]
    return long_words


def check_world_length(w):
    length = 0
    for i in w:
        length += 1
    return length


# print(my_long_word(3, "La peur est le chemin vers le côté obscur la peur mène à la colère lacolère mène à la haine la haine mène à la souffrance"))
