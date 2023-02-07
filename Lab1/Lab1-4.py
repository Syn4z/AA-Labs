import matplotlib.pyplot as plt
import datetime


# Fibonacci series using Power of the Matrix
def fibonacci(n):
    F = [[1, 1],
         [1, 0]]
    if (n == 0):
        return 0
    power(F, n - 1)

    return F[0][0]


def multiply(F, M):
    x = (F[0][0] * M[0][0] +
         F[0][1] * M[1][0])
    y = (F[0][0] * M[0][1] +
         F[0][1] * M[1][1])
    z = (F[1][0] * M[0][0] +
         F[1][1] * M[1][0])
    w = (F[1][0] * M[0][1] +
         F[1][1] * M[1][1])

    F[0][0] = x
    F[0][1] = y
    F[1][0] = z
    F[1][1] = w


def power(F, n):
    M = [[1, 1],
         [1, 0]]

    for i in range(2, n + 1):
        multiply(F, M)


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
    plt.title("Fibonacci Power of the Matrix")
    plt.show()
