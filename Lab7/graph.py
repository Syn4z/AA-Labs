import random
import networkx as nx


# Function to generate a random undirected graph with n nodes and m edges
import random


# `nodes` is the number of nodes in the graph
# `density` is the probability that a node will be connected to another node
def generate_matrix(nodes=5, density=0.5):
    matrix = [[0] * nodes for i in range(nodes)]
    for i in range(nodes):
        for j in range(i, nodes):
            if i == j:
                matrix[i][j] = 0
            else:
                if random.random() <= density:
                    matrix[i][j] = random.randint(1, 1000)
                    matrix[j][i] = matrix[i][j]

    return matrix