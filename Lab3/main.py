import time
import matplotlib.pyplot as plt
from alg1 import alg1
from alg2 import alg2
from alg3 import alg3
from alg4 import alg4
from alg5 import alg5

if __name__ == "__main__":

    times = [[0] * 10 for x in range(5)]
    algorithms = [alg1, alg2, alg3, alg4, alg5]

    for n in range(1000, 11000, 1000):
        for i in range(len(algorithms)):
            start_time = time.perf_counter()
            res = algorithms[i](n)
            end_time = time.perf_counter()
            timeRes = (end_time - start_time)
            x = int(n/1000-1)
            times[i][x] = timeRes

    plt.plot(range(1000, 11000, 1000), times[0], linewidth=3, label='Algorithm 1')
    plt.xlabel('nr of elements')
    plt.ylabel('Time (s)')
    plt.title('Algorithm 1')
    plt.legend()
    plt.show()

    plt.plot(range(1000, 11000, 1000), times[1], 'y', linewidth=3, label='Algorithm 2')
    plt.xlabel('nr of elements')
    plt.ylabel('Time (s)')
    plt.title('Algorithm 2')
    plt.legend()
    plt.show()

    plt.plot(range(1000, 11000, 1000), times[2], 'g', linewidth=3, label='Algorithm 3')
    plt.xlabel('nr of elements')
    plt.ylabel('Time (s)')
    plt.title('Algorithm 3')
    plt.legend()
    plt.show()

    plt.plot(range(1000, 11000, 1000), times[3], 'r', linewidth=3, label='Algorithm 4')
    plt.xlabel('nr of elements')
    plt.ylabel('Time (s)')
    plt.title('Algorithm 4')
    plt.legend()
    plt.show()

    plt.plot(range(1000, 11000, 1000), times[4], 'm', linewidth=3, label='Algorithm 5')
    plt.xlabel('nr of elements')
    plt.ylabel('Time (s)')
    plt.title('Algorithm 5')
    plt.legend()
    plt.show()

    plt.plot(range(1000, 11000, 1000), times[0], linewidth=3, label='1')
    plt.plot(range(1000, 11000, 1000), times[1], 'y', linewidth=3, label='2')
    plt.plot(range(1000, 11000, 1000), times[2], 'g', linewidth=3, label='3')
    plt.plot(range(1000, 11000, 1000), times[3], 'r', linewidth=3, label='4')
    plt.plot(range(1000, 11000, 1000), times[4], 'm', linewidth=3, label='5')
    plt.xlabel('nr of elements')
    plt.ylabel('Time (s)')
    plt.title('Execution time for all Algorithms')
    plt.legend()
    plt.show()
