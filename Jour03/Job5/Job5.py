def Premier(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


for i in range(1000):
    if Premier(i):
        print(i)

"""

<< Shorter Version But less Readable >>

def Premier(n):
    return n > 1 and all(n % i for i in range(2, int(n ** 0.5) + 1))

premiers = [i for i in range(1000) if Premier(i)]

print(premiers)

"""