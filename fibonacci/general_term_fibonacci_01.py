# import math


def fib(n):
    f = ((1 + 5**0.5) / 2)**n / 5**0.5 + 0.5
    return int(f)
    # ans_1 = (((1 + math.sqrt(5)) / 2)**n) - (((1 - math.sqrt(5)) / 2)**n)
    # ans = ans_1 / math.sqrt(5)
    # return int(ans)


for i in range(10):
    print(fib(i))
