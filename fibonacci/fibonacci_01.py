def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    # print(n, b)
    return b


# print([fib(i) for i in range(10)])


for i in range(10):
    print(fib(i), i)
