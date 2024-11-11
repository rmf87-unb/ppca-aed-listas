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
