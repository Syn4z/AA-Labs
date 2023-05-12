import time
import numpy as np
from matplotlib import pyplot as plt
from prettytable import PrettyTable
from algorithms import *


def bar(alg):
    plt.bar(1, alg[0], 0.4)
    plt.bar(2, alg[1], 0.4)
    plt.bar(3, alg[2], 0.4)
    plt.bar(4, alg[3], 0.4)
    plt.bar(5, alg[4], 0.4)


if __name__ == "__main__":

    n = [5, 50, 100, 200, 300]
    bbpTime = []
    legendreTime = []
    spigotTime = []
    xAxis = []
    for i in n:
        xAxis.append(str(i))

    arr = [i for i in range(len(n))]
    x = np.arange(1, len(arr) + 1)

    for nr in n:
        startTime = time.perf_counter()
        bbpPi(nr)
        endTime = time.perf_counter()
        bbpTime.append(endTime - startTime)
        startTime = time.perf_counter()
        legendrePi(nr)
        endTime = time.perf_counter()
        legendreTime.append(endTime - startTime)
        startTime = time.perf_counter()
        spigotPi(nr)
        endTime = time.perf_counter()
        spigotTime.append(endTime - startTime)

    # Plot graph
    bar(bbpTime)
    plt.xticks(x, xAxis)
    plt.xlabel('Nth digit')
    plt.ylabel('Search Time, s')
    plt.title('BBP algorithm')
    plt.show()

    bar(legendreTime)
    plt.xticks(x, xAxis)
    plt.xlabel('Nth digit')
    plt.ylabel('Search Time, s')
    plt.title('Legendre algorithm')
    plt.show()

    bar(spigotTime)
    plt.xticks(x, xAxis)
    plt.xlabel('Nth digit')
    plt.ylabel('Search Time, s')
    plt.title('Spigot algorithm')
    plt.show()

    plt.plot(n, bbpTime, linewidth=3, label='BBP')
    plt.plot(n, legendreTime, linewidth=3, label='Legendre')
    plt.plot(n, spigotTime, linewidth=3, label='Spigot')
    plt.xlabel('Nth digit')
    plt.ylabel('Search Time, s')
    plt.title('Algorithms comparison')
    plt.legend()
    plt.show()

    myTable = PrettyTable(["Algorithm/Nth digit", *n])
    myTable.add_row(["BBP", *bbpTime])
    myTable.add_row(["Legendre", *legendreTime])
    myTable.add_row(["Spigot", *spigotTime])
    print(myTable)
