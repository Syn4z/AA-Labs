import random
import time
import matplotlib.pyplot as plt
import numpy as np
from prettytable import PrettyTable
from Tree import unbalancedTree, balancedTree, bfs, dfs, draw_tree


def timeRes(timeResNodes):
    timeResBfsFinal = [timeResNodes[0], (timeResNodes[0] + timeResNodes[1]) / 2,
                       (timeResNodes[0] + timeResNodes[1] + timeResNodes[2]) / 3,
                       (timeResNodes[0] + timeResNodes[1] + timeResNodes[2] + timeResNodes[3]) / 4,
                       (timeResNodes[0] + timeResNodes[1] + timeResNodes[2] + timeResNodes[3] + timeResNodes[4]) / 5]

    return timeResBfsFinal


def loop(nodeList, timeResBfsFinal, timeResDfsFinal):
    timeResBfs = []
    timeResDfs = []

    for i in range(len(nodeList)):
        for n in nodeList[i]:
            print("Node to find: ", n)
            print("Group of", len(nodeList[i]), "nodes")
            startTime = time.perf_counter()
            bfs_result_bal = bfs(balanced_root, n)
            endTime = time.perf_counter()
            print("Path:\n", bfs_result_bal)
            timeResBfs.append(endTime - startTime)
    timeResBfsFinal += timeRes(timeResBfs)

    plt.bar(X_axis - 0.2, timeResBfsFinal, 0.4, label='BFS')

    for i in range(len(nodeList)):
        for n in nodeList[i]:
            print("Node to find: ", n)
            print("Group of", len(nodeList[i]), "nodes")
            startTime = time.perf_counter()
            dfs_result_bal = dfs(balanced_root, n)
            endTime = time.perf_counter()
            print("Path:\n", dfs_result_bal)
            timeResDfs.append(endTime - startTime)
    timeResDfsFinal += timeRes(timeResDfs)

    plt.bar(X_axis + 0.2, timeResDfsFinal, 0.4, label='DFS')

    plt.xticks(X_axis, X)
    plt.xlabel('searched nodes')
    plt.ylabel('Time (s)')
    if nodeList == nodeListUnb:
        plt.title('Execution time for unbalanced tree with 20 nodes')
    else:
        plt.title('Execution time for balanced tree with 20 nodes')
    plt.legend()
    plt.show()

    return timeResBfsFinal, timeResDfsFinal


def node(treeType):
    if treeType == 'b':
        return random.randint(1, 14)
    else:
        return random.choice([1, 2, 3, 4, 5, 6, 10, 11, 12])


if __name__ == "__main__":
    nodeListB = [[node('b')], [node('b'), node('b')], [node('b'), node('b'), node('b')],
                 [node('b'), node('b'), node('b'), node('b')],
                 [node('b'), node('b'), node('b'), node('b'), node('b')]]
    nodeListUnb = [[node('u')], [node('u'), node('u')], [node('u'), node('u'), node('u')],
                   [node('u'), node('u'), node('u'), node('u')],
                   [node('u'), node('u'), node('u'), node('u'), node('u')]]

    root = unbalancedTree()
    graph = draw_tree(root, 'u')
    graph.render()

    balanced_root = balancedTree()
    graph = draw_tree(balanced_root, 'b')
    graph.render()

    X = ['1', '2', '3', '4', '5']
    X_axis = np.arange(len(X))
    timeBFSBal = []
    timeBFSUnb = []
    timeDFSBal = []
    timeDFSUnb = []

    loop(nodeListB, timeBFSBal, timeDFSBal)
    loop(nodeListUnb, timeBFSUnb, timeDFSUnb)

    myTable = PrettyTable(['Nr of Nodes searched', *X])
    myTable.add_row(["Balanced BFS", *timeBFSBal])
    myTable.add_row(["Balanced DFS", *timeDFSBal])
    myTable.add_row(["Unbalanced BFS", *timeBFSUnb])
    myTable.add_row(["Unbalanced DFS", *timeDFSUnb])
    print(myTable)
