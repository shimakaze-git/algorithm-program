import numpy as np
import matplotlib.pyplot as plt

# from general_term_fibonacci import fib
from fibonacci_01 import fib


x = np.arange(20)
print(x)
print(fib(10))
# print([fib(i) for i in range(20)])
# print([fib(i + 1) for i in range(20)])
# print([fib(i + 1) / fib(i) for i in range(20)])

y = np.array(
    [fib(i + 1) / fib(i) for i in range(20)]
)
plt.plot(x, y, "ro-")
plt.show()
# print(y)
