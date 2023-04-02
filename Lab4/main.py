import random
import time
import matplotlib.pyplot as plt
import numpy as np
from prettytable import PrettyTable
from Tree import unbalancedTree, balancedTree, bfs, dfs, draw_tree


# Time results function
def timeRes(timeResNodes):
    timeResBfsFinal = [timeResNodes[0], (timeResNodes[0] + timeResNodes[1]) / 2,
                       (timeResNodes[0] + timeResNodes[1] + timeResNodes[2]) / 3,
                       (timeResNodes[0] + timeResNodes[1] + timeResNodes[2] + timeResNodes[3]) / 4,
                       (timeResNodes[0] + timeResNodes[1] + timeResNodes[2] + timeResNodes[3] + timeResNodes[4]) / 5]

    return timeResBfsFinal


# Loop function to plot the graphs for both trees
def loop(nodeList, timeResBfsFinal, timeResDfsFinal, searchType):
    timeResBfs = []
    timeResDfs = []

    if searchType == 'bfs' or searchType == 'both':
        # BFS
        for i in range(len(nodeList)):
            for n in nodeList[i]:
                ''' # Uncomment to see the results
                print("Node to find: ", n)
                print("Group of", len(nodeList[i]), "nodes")
                '''
                startTime = time.perf_counter()
                bfs_result_bal = bfs(balanced_root, n)
                endTime = time.perf_counter()
                ''' print("Path:\n", bfs_result_bal) '''
                timeResBfs.append(endTime - startTime)
        timeResBfsFinal += timeRes(timeResBfs)

        plt.bar(X_axis - 0.2, timeResBfsFinal, 0.4, label='BFS', color='orange')

        if searchType == 'both':
            # DFS
            for i in range(len(nodeList)):
                for n in nodeList[i]:
                    ''' # Uncomment to see the results
                    print("Node to find: ", n)
                    print("Group of", len(nodeList[i]), "nodes")
                    '''
                    startTime = time.perf_counter()
                    dfs_result_bal = dfs(balanced_root, n)
                    endTime = time.perf_counter()
                    ''' print("Path:\n", dfs_result_bal) '''
                    timeResDfs.append(endTime - startTime)
            timeResDfsFinal += timeRes(timeResDfs)

            plt.bar(X_axis + 0.2, timeResDfsFinal, 0.4, label='DFS', color='green')

    elif searchType == 'dfs':
        # DFS
        for i in range(len(nodeList)):
            for n in nodeList[i]:
                ''' # Uncomment to see the results
                print("Node to find: ", n)
                print("Group of", len(nodeList[i]), "nodes")
                '''
                startTime = time.perf_counter()
                dfs_result_bal = dfs(balanced_root, n)
                endTime = time.perf_counter()
                ''' print("Path:\n", dfs_result_bal) '''
                timeResDfs.append(endTime - startTime)
        timeResDfsFinal += timeRes(timeResDfs)

        plt.bar(X_axis + 0.2, timeResDfsFinal, 0.4, label='DFS', color='green')

    # Plot the graph
    plt.xticks(X_axis, X)
    plt.xlabel('Nr of searched nodes')
    plt.ylabel('Time (s)')
    if nodeList == nodeListUnb:
        plt.title('Unbalanced tree with 20 nodes')
    else:
        plt.title('Balanced tree with 20 nodes')
    plt.legend()
    plt.grid(True)
    plt.show()

    return timeResBfsFinal, timeResDfsFinal


# Generate random nodes function
def node(treeType):
    if treeType == 'b':
        return random.randint(1, 14)
    else:
        return random.choice([1, 2, 3, 4, 5, 6, 10, 11, 12])


if __name__ == "__main__":
    # Create random nodes for search
    nodeListB = [[node('b')], [node('b'), node('b')], [node('b'), node('b'), node('b')],
                 [node('b'), node('b'), node('b'), node('b')],
                 [node('b'), node('b'), node('b'), node('b'), node('b')]]
    nodeListUnb = [[node('u')], [node('u'), node('u')], [node('u'), node('u'), node('u')],
                   [node('u'), node('u'), node('u'), node('u')],
                   [node('u'), node('u'), node('u'), node('u'), node('u')]]

    # Draw trees
    root = unbalancedTree()
    graph = draw_tree(root, 'u')
    graph.render()

    balanced_root = balancedTree()
    graph = draw_tree(balanced_root, 'b')
    graph.render()

    # X axis
    X = ['1', '2', '3', '4', '5']
    X_axis = np.arange(len(X))
    # Time results
    timeBFSBal = []
    timeBFSUnb = []
    timeDFSBal = []
    timeDFSUnb = []

    # Balanced tree
    loop(nodeListB, timeBFSBal, timeDFSBal, 'both')
    # Unbalanced tree
    loop(nodeListUnb, timeBFSUnb, timeDFSUnb, 'both')

    # Draw table
    myTable = PrettyTable(['Nr of Nodes searched', *X])
    myTable.add_row(["Balanced BFS", *timeBFSBal]) if timeBFSBal else None
    myTable.add_row(["Balanced DFS", *timeDFSBal]) if timeDFSBal else None
    myTable.add_row(["Unbalanced BFS", *timeBFSUnb]) if timeBFSUnb else None
    myTable.add_row(["Unbalanced DFS", *timeDFSUnb]) if timeDFSUnb else None
    print(myTable)

    # Separate time results
    print(myTable[0])
    print(myTable[1])
    try:
        if myTable[2]:
            print(myTable[2])
            print(myTable[3])
    except IndexError:
        print("No more results")
