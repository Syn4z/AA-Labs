import numpy as np
from algorithms import generateGraph, dijkstra, floyd
import matplotlib.pyplot as plt
import networkx as nx
import random
import time
from prettytable import PrettyTable


def drawGraph(node, graphType):
    if graphType == "sparse":
        G = generateGraph(node, node / 2)
    elif graphType == "dense":
        G = generateGraph(node, node * 2)
    else:
        return None
    # Uncomment to draw graph
    '''
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, font_weight='bold')
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()
    '''

    i = int(node/2)
    timesD = 0
    timesF = 0
    for n in range(i):
        start_node = random.randint(0, node - 1)
        target_node = random.randint(0, node - 1)
        if target_node == start_node:
            target_node = random.randint(0, node - 1)
        startTime = time.perf_counter()
        d = dijkstra(G, start_node, target_node)
        endTime = time.perf_counter()
        timesD += (endTime - startTime)
        # print("Dijkstra's: ", d)
        startTime = time.perf_counter()
        f = floyd(G, start_node, target_node)
        endTime = time.perf_counter()
        timesF += (endTime - startTime)
        # print("Floyd-Warshall: ", f)
    if graphType == "dense":
        timesDense[0].append(round(timesD, 4))
        timesDense[1].append(round(timesF, 4))
    elif graphType == "sparse":
        timesSparse[0].append(round(timesD, 4))
        timesSparse[1].append(round(timesF, 4))

    return timesSparse, timesDense


if __name__ == "__main__":

    random.seed(69)

    nodes = [10, 20, 40, 80]
    nodeSearch = [5, 10, 20, 40]
    xAxis = ["5", "10", "20", "40"]
    timesSparse = [[], []]
    timesDense = [[], []]

    for g in nodes:
        # Sparse
        drawGraph(g, "sparse")

        # Dense
        drawGraph(g, "dense")

    arr = [i for i in range(4)]
    x = np.arange(1, len(arr)+1)

    # Plot graph for Dijkstra's
    plt.bar(x-0.4, timesSparse[0][0], 0.2, label='Sparse 10 ')
    plt.bar(x-0.3, timesSparse[0][1], 0.2, label='Sparse 20')
    plt.bar(x-0.2, timesSparse[0][2], 0.2, label='Sparse 40')
    plt.bar(x-0.1, timesSparse[0][3], 0.2, label='Sparse 80')
    plt.bar(x+0.1, timesDense[0][0], 0.2, label='Dense 10')
    plt.bar(x+0.2, timesDense[0][1], 0.2, label='Dense 20')
    plt.bar(x+0.3, timesDense[0][2], 0.2, label='Dense 40')
    plt.bar(x+0.4, timesDense[0][3], 0.2, label='Dense 80')
    plt.xticks(x, xAxis)
    plt.xlabel('Nodes searched')
    plt.ylabel('Search Time, s')
    plt.title('Dijkstra shortest path')
    plt.legend()
    plt.show()

    # Plot graph for Floyd-Warshall
    plt.bar(x-0.5, timesSparse[1][0], 0.2, label='Sparse 10 ')
    plt.bar(x-0.4, timesSparse[1][1], 0.2, label='Sparse 20')
    plt.bar(x-0.3, timesSparse[1][2], 0.2, label='Sparse 40')
    plt.bar(x-0.2, timesSparse[1][3], 0.2, label='Sparse 80')
    plt.bar(x+0.1, timesDense[1][0], 0.2, label='Dense 10')
    plt.bar(x+0.2, timesDense[1][1], 0.2, label='Dense 20')
    plt.bar(x+0.3, timesDense[1][2], 0.2, label='Dense 40')
    plt.bar(x+0.4, timesDense[1][3], 0.2, label='Dense 80')
    plt.xticks(x, xAxis)
    plt.xlabel('Nodes searched')
    plt.ylabel('Search Time, s')
    plt.title('Floyd-Warshall shortest path')
    plt.legend()
    plt.show()

    # Draw table of results
    myTable = PrettyTable(["Graph Type/Algorithm", "-------", "------", "-----", "----"])
    myTable.add_row(["Graph Nodes", *nodes])
    myTable.add_row(["Nodes searched", *nodeSearch])
    myTable.add_row(["Sparse Dijkstra's", *timesSparse[0]])
    myTable.add_row(["Sparse Floyd-Warshall", *timesSparse[1]])
    myTable.add_row(["Dense Dijkstra's", *timesDense[0]])
    myTable.add_row(["Dense Floyd-Warshall", *timesDense[1]])
    print(myTable)
