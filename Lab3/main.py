import time
import matplotlib.pyplot as plt
from alg1 import alg1
from alg2 import alg2
from alg3 import alg3
from alg4 import alg4
from alg5 import alg5

if __name__ == "__main__":

    times = []
    algorithms = [alg1, alg2, alg3, alg4, alg5]

    for n in range(1000, 5000, 1000):
        for el in algorithms:
            start_time = time.perf_counter()
            res = el(n)
            end_time = time.perf_counter()
            timeRes = (end_time - start_time)
            times.append(timeRes)

            print(el.__name__ + ":\n", res, "\n", timeRes)

    print(times)

    plt.plot(range(1000, 10000, 1000), times)
    plt.xlabel('n')
    plt.ylabel('Time (s)')
    plt.title('Execution time for alg5')
    plt.show()
