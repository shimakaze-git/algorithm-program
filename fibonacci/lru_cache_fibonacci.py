# http://python-remrin.hatenadiary.jp/entry/2017/05/19/153228
from functools import lru_cache

counter = 0


def fib1(n):
    global counter
    counter += 1
    if n in [0, 1]:
        return 1
    return fib1(n - 1) + fib1(n - 2)


print(fib1(3))
# print(fib1(24))
print(counter, "回の関数呼び出し")


counter = 0


@lru_cache(maxsize=1024)
def fib2(n):
    global counter
    counter += 1
    if n in [0, 1]:
        return 1
    return fib2(n - 1) + fib2(n - 2)


print(fib2(3))
# print(fib2(24))
print(counter, "回の関数呼び出し")

