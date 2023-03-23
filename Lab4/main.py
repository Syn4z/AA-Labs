import time
import matplotlib.pyplot as plt
from prettytable import PrettyTable
from Graph import Graph


if __name__ == "__main__":

    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    print("Following is BFS (starting from vertex 2)")
    startTime = time.perf_counter()
    g.BFS(2)
    endTime = time.perf_counter()
    timeRes = endTime - startTime
    print("\n", timeRes)

    plt.plot(2, timeRes, 'o', linewidth=3, label='BFS')

    print("\nFollowing is DFS from (starting from vertex 2)")
    startTime = time.perf_counter()
    g.DFS(2)
    endTime = time.perf_counter()
    timeRes = endTime - startTime
    print("\n", timeRes)

    plt.plot(2, timeRes, 'o', linewidth=3, label='DFS')

    plt.xlabel('nr of elements')
    plt.ylabel('Time (s)')
    plt.title('Execution time for BFS and DFS')
    plt.legend()
    plt.show()
