from algorithms import generateGraph, dijkstra, floyd
import matplotlib.pyplot as plt
import networkx as nx
import random
import time
from prettytable import PrettyTable


def drawGraph(G):
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, font_weight='bold')
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()


def computeAlg(times, r):
    for i in range(num_paths):
        print(f"Path {i+1}:")
        startTime = time.perf_counter()
        d = dijkstra(G, start_node, target_node)
        endTime = time.perf_counter()
        timesSparse[0].append(round((endTime - startTime), 4))
        print("Dijkstra's: ", d)
        startTime = time.perf_counter()
        f = floyd(G, start_node, target_node)
        endTime = time.perf_counter()
        timesSparse[1].append(round((endTime - startTime), 4))
        print("Floyd-Warshall: ", f)
    times = 0
    print(timesSparse[0])
    for n in range(len(timesSparse[0])):
        times = times + timesSparse[0][n]
    timesSparse[0] = [times / num_paths]
    print(timesSparse)

    return times


if __name__ == "__main__":

    random.seed(69)

    nodes = [10, 20, 40, 80, 160, 320]
    timesSparse = [[], []]
    timesDense = [[], []]

    num_paths = 2

    for g in nodes:
        # Sparse
        print("\nSparse:\n")
        G = generateGraph(g, g / 2)
        drawGraph(G)
        start_node = random.randint(0, g - 1)
        target_node = random.randint(0, g - 1)
        if target_node == start_node:
            target_node = random.randint(0, g - 1)
        startTime = time.perf_counter()
        d = dijkstra(G, start_node, target_node)
        endTime = time.perf_counter()
        timesSparse[0].append(round((endTime - startTime), 4))
        print("Dijkstra's: ", d)
        startTime = time.perf_counter()
        f = floyd(G, start_node, target_node)
        endTime = time.perf_counter()
        timesSparse[1].append(round((endTime - startTime), 4))
        print("Floyd-Warshall: ", f)

        # Dense
        print("\nDense:\n")
        G = generateGraph(g, g * 2)
        drawGraph(G)
        start_node = random.randint(0, g - 1)
        target_node = random.randint(0, g - 1)
        if target_node == start_node:
            target_node = random.randint(0, g - 1)
        startTime = time.perf_counter()
        d = dijkstra(G, start_node, target_node)
        endTime = time.perf_counter()
        timesDense[0].append(round((endTime - startTime), 4))
        print("Dijkstra's: ", d)
        startTime = time.perf_counter()
        f = floyd(G, start_node, target_node)
        endTime = time.perf_counter()
        timesDense[1].append(round((endTime - startTime), 4))
        print("Floyd-Warshall: ", f)

    myTable = PrettyTable(["Nr of Nodes", *nodes])
    myTable.add_row(["Sparse Dijkstra's", *timesSparse[0]])
    myTable.add_row(["Sparse Floyd-Warshall", *timesSparse[1]])
    myTable.add_row(["Dense Dijkstra's", *timesDense[0]])
    myTable.add_row(["Dense Floyd-Warshall", *timesDense[1]])
    print(myTable)
