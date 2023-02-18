import matplotlib.pyplot as plt
import datetime

# Fibonacci series using O(Log n) arithmetic operations
MAX = 100000

f = [0] * MAX


def fibonacci(n):
    if (n == 0):
        return 0
    if (n == 1 or n == 2):
        f[n] = 1
        return (f[n])

    if (f[n]):
        return f[n]

    if (n & 1):
        k = (n + 1) // 2
    else:
        k = n // 2

    if ((n & 1)):
        f[n] = (fibonacci(k) * fibonacci(k) + fibonacci(k - 1) * fibonacci(k - 1))
    else:
        f[n] = (2 * fibonacci(k - 1) + fibonacci(k)) * fibonacci(k)

    return f[n]


if __name__ == "__main__":
    fibNr = []
    timeSpent = []
    n = 10000
    for x in range(n + 1):
        start = datetime.datetime.now()
        print("fib nr " + str(x))
        print(fibonacci(x))
        end = datetime.datetime.now()
        timeSpent.append((end - start).microseconds / 1000)
        print("time " + str(timeSpent[x]))

    for i in range(n + 1):
        fibNr.append(i)

    plt.plot(fibNr, timeSpent, color='orange', linewidth=3)
    plt.xlabel("n-th fibonacci nr")
    plt.ylabel("time, ms")
    plt.title("Fibonacci O(Log n) arithmetic operations")
    plt.show()
