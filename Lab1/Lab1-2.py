import matplotlib.pyplot as plt
import datetime


# Fibonacci series using Dynamic Programming
def fibonacci(n):
    f = [0, 1]

    for i in range(2, n + 1):
        f.append(f[i - 1] + f[i - 2])
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
        timeSpent.append((end - start).microseconds/1000)
        print("time " + str(timeSpent[x]))

    for i in range(n + 1):
        fibNr.append(i)

    plt.plot(fibNr, timeSpent, color='orange', linewidth=3)
    plt.xlabel("n-th fibonacci nr")
    plt.ylabel("time, ms")
    plt.title("Fibonacci Dynamic Programming")
    plt.show()
