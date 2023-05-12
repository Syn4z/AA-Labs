import heapq
import sys


# Function to implement Prim's algorithm on a graph
def prim(graph):
    vertices = len(graph)

    key = [sys.maxsize] * vertices
    parent = [None] * vertices
    key[0] = 0
    mst_set = [False] * vertices

    heap = [(0, 0)]

    while heap:
        _, u = heapq.heappop(heap)

        if mst_set[u]:
            continue

        mst_set[u] = True

        for v in range(vertices):
            if 0 < graph[u][v] < key[v] and not mst_set[v]:
                key[v] = graph[u][v]
                parent[v] = u
                heapq.heappush(heap, (key[v], v))

    result = []
    for i in range(1, vertices):
        result.append([parent[i], i, graph[i][parent[i]]])

    return result


class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py: return False
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1
        return True


# Function to implement Kruskal's algorithm on a graph
def kruskal(graph):
    n = graph[-1][1] + 1
    dsu = DisjointSet(n)
    edges = sorted(graph, key=lambda x: x[2])
    res = []
    for u, v, w in edges:
        if dsu.union(u, v):
            res.append([u, v, w])
            if len(res) == n - 1: break
    return res
