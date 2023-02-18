import matplotlib.pyplot as plt
import datetime


# Fibonacci series using Space Optimisation
def fibonacci(n):
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n + 1):
            c = a + b
            a = b
            b = c
        return b


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
    plt.title("Fibonacci Space Optimisation")
    plt.show()
