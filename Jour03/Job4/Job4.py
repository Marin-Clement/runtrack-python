def CountNumber():
    for i in range(1, 101):
        buffer = ""
        if i % 3 == 0:
            buffer += "Fizz"
        if i % 5 == 0:
            buffer += "Buzz"
        print(buffer or i)


CountNumber()


"""

<< Shorter Version But less Readable >>

def CountNumber():
    for i in range(1, 101):
        print("Fizz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0) or i)


CountNumber()
  
"""