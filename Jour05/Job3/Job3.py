def draw_carpet(n):
    diagonal = n + 1
    print("+" + "-" * (n + 1) + "+")
    for i in range(n + 1):
        print("|" + "#" * (diagonal - 1) + " " + ("#" * ((n + 1) - diagonal)) + "|")
        diagonal -= 1
    print("+" + "-" * (n + 1) + "+")


draw_carpet(50)
