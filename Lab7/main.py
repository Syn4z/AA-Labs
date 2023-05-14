import time
from matplotlib import pyplot as plt
from prettytable import PrettyTable
from graph import generateGraph
from algorithms import prim, kruskal

if __name__ == "__main__":

    n = [10, 50, 100, 150, 200, 250]
    density = 1  # 0.3 for sparse graphs, 1 for dense graphs
    kruskalTime = []
    primTime = []

    for nr in n:
        graph = []
        matrix = generateGraph(nr, density)
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                if matrix[i][j] != 0:
                    graph.append([i, j, matrix[i][j]])

        startTime = time.perf_counter()
        mst_prim = prim(matrix)
        endTime = time.perf_counter()
        primTime.append(endTime - startTime)
        startTime = time.perf_counter()
        mst_kruskal = kruskal(graph)
        endTime = time.perf_counter()
        kruskalTime.append(endTime - startTime)

    # Plot the graph
    plt.plot(n, primTime, linewidth=3, label='Prim')
    plt.plot(n, kruskalTime, linewidth=3, label='Kruskal')
    plt.xlabel('Nodes')
    plt.ylabel('Search Time, s')
    plt.title('Algorithms comparison for sparse graphs')
    plt.legend()
    plt.show()

    myTable = PrettyTable(["Algorithm/Nth digit", *n])
    myTable.add_row(["Prim", *primTime])
    print(myTable)

    myTable = PrettyTable(["Algorithm/Nth digit", *n])
    myTable.add_row(["Kruskal", *kruskalTime])
    print(myTable)

    # Print the entire table
    myTable = PrettyTable(["Algorithm/Nth digit", *n])
    myTable.add_row(["Prim", *primTime])
    myTable.add_row(["Kruskal", *kruskalTime])
    print(myTable)
