import math


def type_triangle(a, b, c):
    # @ Verifie si possible @ #
    if a + b > c and a + c > b and b + c > a:

        # @ Rectangle @ #
        if a ** 2 + b ** 2 == c ** 2 or a ** 2 + c ** 2 == b ** 2 or b ** 2 + c ** 2 == a ** 2:
            print("C'est un triangle rectangle")

        # @ Équilatéral @ #
        elif a == b and b == c:
            print("C'est un triangle équilatéral")

        # @ Isocèle @ #
        elif a == b or a == c or b == c:

            # @ Rectangle @ #
            if a ** 2 + b ** 2 == int(c ** 2) or a ** 2 + int(c ** 2) == b ** 2 or b ** 2 + int(c ** 2) == a ** 2:
                print("C'est un triangle rectangle isocèle")
            else:
                print("C'est un triangle isocèle")

        # @ Quelconque @ #
        else:
            print("C'est un triangle quelconque")

    else:
        print("Error 404")


type_triangle(3, 4, 5)
type_triangle(3, 3, 3)
type_triangle(3, 3, 2)
type_triangle(1, 1, math.sqrt(2))
type_triangle(3, 4, 7)
