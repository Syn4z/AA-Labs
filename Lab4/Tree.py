import graphviz


class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children is not None else []

    # Define the string representation of the node
    def __repr__(self):
        return f"Node({self.value})"


def unbalancedTree():
    # Define the unbalanced tree structure
    root = Node(1, [
        Node(2, [
            Node(4, [
                Node(14, [
                ]),
            ]),
            Node(5, [
                Node(10, [
                    Node(11, [
                        Node(17),
                    ]),
                    Node(8, [
                        Node(9, [
                            Node(16, [
                                Node(18, [
                                    Node(20),
                                ]),
                            ])
                        ])
                    ]),
                ]),
                Node(7, [
                    Node(12, [
                        Node(13, [
                            Node(15),
                        ]),
                    ]),
                ]),
            ])
        ]),
        Node(3, [
            Node(6, [
                Node(19),
            ]),
        ]),
    ])

    return root


def balancedTree():
    # Define the balanced tree structure
    root = Node(1, [
        Node(2, [
            Node(4, [
                Node(14),
            ]),
            Node(5, [
                Node(10),
                Node(11)
            ])
        ]),
        Node(3, [
            Node(6, [
                Node(12),
                Node(13)
            ]),
            Node(7, [
                Node(8, [
                    Node(15),
                    Node(16)
                ]),
                Node(9, [
                    Node(17),
                    Node(18),
                    Node(19)
                ])
            ])
        ])
    ])

    return root


def bfs(node, target):
    queue = [(node, [])]
    visited = set()

    while queue:
        current, path = queue.pop(0)
        if current.value == target:
            return path + [current]
        visited.add(current)

        for child in current.children:
            if child not in visited:
                queue.append((child, path + [current]))

    return None


def dfs(node, target, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    if node.value == target:
        return path + [node]

    visited.add(node)
    for child in node.children:
        if child not in visited:
            result = dfs(child, target, visited, path + [node])
            if result is not None:
                return result

    return None


# Function to output the tree graphically
def draw_tree(root, treeType):
    graphName = ''

    def add_node(node, tree):
        tree.node(str(id(node)), label=str(node.value))
        for child in node.children:
            tree.edge(str(id(node)), str(id(child)))
            add_node(child, tree)

    if treeType == 'u':
        graphName = 'Unbalanced Tree'
    elif treeType == 'b':
        graphName = 'Balanced Tree'

    graph = graphviz.Digraph(directory="C:/Users/Admin/git_repository/AA-Labs/Lab4/graphs", name=graphName)
    add_node(root, graph)
    graph.render(view=True)

    return graph
