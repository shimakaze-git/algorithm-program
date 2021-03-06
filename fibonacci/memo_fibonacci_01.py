fib_memo = {}


def fib(n):
    if n < 3:
        return 1
    if n not in fib_memo:
        fib_memo[n] = fib(n-1) + fib(n-2)
    return fib_memo[n]


print(fib(3))
print(fib(10))
