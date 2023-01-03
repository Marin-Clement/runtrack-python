import operator

ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '%': operator.mod,
    '^': operator.xor,
}

def Calcule(num1, operator, num2):
    return ops[operator](num1, num2)


print(Calcule(1, '+', 3))
