import networkx as nx
import random
import heapq


def generateGraph(num_nodes, num_edges):
    G = nx.Graph()
    G.add_nodes_from(range(num_nodes))
    edge_count = 0
    while edge_count < num_edges:
        i = random.randint(0, num_nodes - 1)
        j = random.randint(0, num_nodes - 1)
        if i != j and not G.has_edge(i, j):
            weight = random.randint(1, 10)  # Assign a random weight between 1 and 10
            G.add_edge(i, j, weight=weight)  # Add edge with weight attribute
            edge_count += 1
    return G


def dijkstra(G, start, target):
    visited = set()
    distance = {start: 0}
    heap = [(0, start)]

    while heap:
        (dist, current) = heapq.heappop(heap)

        if current in visited:
            continue
        visited.add(current)

        if current == target:
            return distance[current]

        for neighbor, weight in G[current].items():
            if neighbor in visited:
                continue
            tentative_distance = dist + weight['weight']
            if neighbor not in distance or tentative_distance < distance[neighbor]:
                distance[neighbor] = tentative_distance
                heapq.heappush(heap, (tentative_distance, neighbor))

    return None  # if target node is not reachable from start node


# Floyd's algorithm for weighted graph
def floyd(G, start, target):
    n = len(G)
    dist = [[float('inf') for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i == j:
                dist[i][j] = 0
            elif G.has_edge(i, j):
                dist[i][j] = G[i][j]['weight']

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist[start][target]
