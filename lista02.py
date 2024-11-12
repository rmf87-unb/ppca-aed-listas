def decimal2binario(dec):
    digit = 0
    bin = ""
    while 2**digit <= dec:
        digit += 1
    digit -= 1
    while digit >= 0:
        if 2**digit <= dec:
            bin = bin + "1"
            dec -= 2**digit
        else:
            bin = bin + "0"
        digit -= 1
    return bin if bin != "" else "0"


def exe02():
    strip = str(input()).split()
    values = []
    for item in strip:
        if item not in ["+", "*"]:
            values.append(item)
        else:
            a = values.pop()
            b = values.pop()
            values.append(int(a) + int(b) if item == "+" else int(a) * int(b))
    print(values[0])


def exe03():
    list = input()
    stack = []
    for p in list:
        if p == "(":
            stack.append(p)
        else:
            if len(stack) > 0:
                stack.pop()
            else:
                stack.append(p)
    if len(stack) == 0:
        print(True)
    else:
        print(False)


def exe04():
    n = int(input())

    def fibo(n):
        if n == 1 or n == 2:
            return 1
        else:
            fib_n_minus_1 = 1
            fib_n = 1
            i = 3
            while i in range(3, n + 1):
                fib_n = fib_n + fib_n_minus_1
                fib_n_minus_1 = fib_n - fib_n_minus_1
                # print(f"fib_n: {fib_n} fib_n_minus_1: {fib_n_minus_1}")
                i += 1
            return fib_n

    print(fibo(n))


def exe05():
    list = input()
    stack = []
    pares = {"(": ")", "{": "}", "[": "]"}

    broke = False
    for s in list:
        if s in pares.keys():
            stack.append(s)
        else:
            if len(stack) > 0:
                p = stack.pop()
                if s != pares[p]:
                    broke = True
            else:
                broke = True
    if len(stack) == 0 and not broke:
        print(True)
    else:
        print(False)
