def exe01():
    text = input()
    # adiciona um \n
    print(f"{text}")


def exe02():
    r1 = float(input())
    r2 = float(input())
    m = (r1 + r2) / 2
    print(f"{m:.2f}")


def exe03():
    sum = 0
    for num in range(5):
        sum += float(input()) * (num + 1)
    print(f"{sum / 15:.3f}")


def exe04():
    x1, y1 = input().split()
    x1, y1 = [float(x1), float(y1)]
    x2, y2 = input().split()
    x2, y2 = [float(x2), float(y2)]
    z = complex(input())
    print(f"{((x2-x1)**2+(y2-y1)**2)**0.5:.4f}")
    print(f"{(z.real**2 + z.imag**2)**0.5:.4f}")


def exe05():
    num_tests = int(input())
    biggest_sum = 0
    smallest_sum = 0
    for i in range(num_tests):
        x, y = input().split()
        x, y = [int(x), int(y)]
        current = x
        sum = 0
        for j in range(y):
            if current % 2 == 1:
                sum += current
                current += 2
            else:
                current += 1
                sum += current
                current += 2
        print(sum)
        if i == 0:
            biggest_sum = sum
            smallest_sum = sum
            mean_sum = sum
        else:
            if sum > biggest_sum:
                biggest_sum = sum
            if sum < smallest_sum:
                smallest_sum = sum
    print(biggest_sum)
    print(smallest_sum)
    print(f"{biggest_sum*0.5+smallest_sum*0.5:.2f}")


def exe06():
    n = int(input())
    div = 1
    while div <= n:
        if n % div == 0:
            print(div)
        div += 1


def exe07():
    x = int(input())
    y = int(input())
    if x == y:
        print("x e igual a y")
    elif x < y:
        print("x e menor que y")
    else:
        print("x e maior que y")


def exe08():
    maior = 0
    n = 0
    for i in range(10):
        x = int(input())
        if i == 0:
            n = x
            maior = x
        else:
            if x > maior:
                maior = x
    print(maior)
    if maior % n == 0:
        print(n)


def exe09():
    s1 = input()
    s2 = input()

    def concat(s1, s2):
        if not s1:
            return s2
        else:
            return s1[0:1] + concat(s1[1:], s2)

    def rev(s1):
        if not s1:
            return ""
        else:
            return concat(rev(s1[1:]), s1[0:1])

    def prefix(s1, s2):
        if s1 == "" and s2 != "":
            return True
        else:
            if s1[0:1] == s2[0:1]:
                return prefix(s1[1:], s2[1:])
            else:
                return False

    print(concat(s1, s2))
    if s1:
        print(rev(s1))
    else:
        print()
    if s1 or s2:
        print(prefix(s1, s2))


def exe10():
    n = int(input())

    def fib(n):
        if n == 1 or n == 2:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)

    def fat(n):
        if n == 1:
            return 1
        else:
            return n * fat(n - 1)

    fibN = fib(n)
    print(f"{fibN} {fat(n)}" if fibN % 2 == 1 else f"{fibN} {fat(n)} {fib(n+1)-fibN}")


def exe11():
    ra, lu = input().split()
    ra, lu = [int(ra), int(lu)]

    def mdc_euclides(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    print(mdc_euclides(ra, lu))


def exe12():
    pa, pi = input().split()
    pa, pi = [int(pa), int(pi)]
    analise = "ok" if pi > 0 and pi - pa <= 1 and pi - pa >= 0 else "errados"
    print(f"{pa} {pi} {analise}")


def exe13():
    acertou = False
    n = float(input())
    while acertou is not True:
        guess = float(input())
        if n > guess:
            print("O número correto é maior.")
        elif n < guess:
            print("O número correto é menor.")
        else:
            print("Parabéns! Você acertou.")
            acertou = True
