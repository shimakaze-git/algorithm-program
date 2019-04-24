import math


def fib(n):
    ans_1 = (((1 + math.sqrt(5)) / 2)**n) - (((1 - math.sqrt(5)) / 2)**n)
    ans = ans_1 / math.sqrt(5)
    return int(ans)


for i in range(10):
    print(fib(i))
