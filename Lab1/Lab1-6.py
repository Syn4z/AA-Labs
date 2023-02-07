import matplotlib.pyplot as plt
import datetime
import decimal


# Fibonacci series using Binet
def fibonacci(n):
    decimal.getcontext().prec = 10000

    root_5 = decimal.Decimal(5).sqrt()
    phi = ((1 + root_5) / 2)

    a = ((phi ** n) - ((-phi) ** -n)) / root_5

    return round(a)


if __name__ == "__main__":
    fibNr = []
    timeSpent = []
    n = 100
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
    plt.title("Fibonacci Binet")
    plt.show()
