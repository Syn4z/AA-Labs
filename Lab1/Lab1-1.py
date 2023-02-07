import matplotlib.pyplot as plt
import datetime


# Fibonacci series using recursion
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    fibNr = []
    timeSpent = []
    n = 41
    for x in range(n + 1):
        start = datetime.datetime.now()
        print(x)
        print(fibonacci(x))
        end = datetime.datetime.now()
        timeSpent.append((end - start).seconds)
        print(timeSpent[x])

    for a in range(n + 1):
        fibNr.append(a)

    plt.plot(fibNr, timeSpent, color='orange', linewidth=3)
    plt.xlabel("n-th fibonacci nr")
    plt.ylabel("time, s")
    plt.title("Fibonacci Recursive")
    plt.show()
