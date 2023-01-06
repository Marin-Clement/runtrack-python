def draw_rectangle(w,h):
    print("|", "-" * (w - 2), "|")
    for i in range (h - 2):
        print("|", " " * (w - 2), "|")
    print("|", "-" * (w - 2), "|")


draw_rectangle(10, 5)
