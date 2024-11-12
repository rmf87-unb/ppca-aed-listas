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
