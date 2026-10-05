from collections import deque

class Graph:

    def __init__(self):
        self.adj = {}


    def add_edge(self, u, v):

        self.adj.setdefault(u, []).append(v)
        self.adj.setdefault(v, []).append(u)

    def bfs(self, start, goal=None):

        visited = {start}
        queue = deque([start])

        parent = {start: None}
        order = []


        while queue:

            node = queue.popleft()

            order.append(node)


            # Goal check
            if goal is not None and node == goal:

                path = self.make_path(parent, node)

                return order, path


            # Add neighbours
            for neighbour in self.adj[node]:

                if neighbour not in visited:

                    visited.add(neighbour)

                    parent[neighbour] = node

                    queue.append(neighbour)


        # Normal BFS
        if goal is None:

            return order


        return order, None


    def make_path(self, parent, node):

        path = []


        while node is not None:

            path.append(node)

            node = parent[node]


        return path[::-1]


g = Graph()


for u, v in [
    (0, 1),
    (0, 4),
    (1, 4),
    (1, 3),
    (1, 2),
    (2, 3),
    (3, 4)
]:

    g.add_edge(u, v)


print("TASK 1 ")

print("Adjacency list:", g.adj)

print("BFS:", g.bfs(0))


tree = Graph()


for u, v in [
    ('A', 'B'),
    ('A', 'F'),
    ('A', 'D'),
    ('A', 'E'),
    ('B', 'K'),
    ('B', 'J'),
    ('D', 'G'),
    ('E', 'C'),
    ('E', 'H'),
    ('E', 'I'),
    ('K', 'N'),
    ('K', 'M'),
    ('I', 'L')
]:

    tree.add_edge(u, v)

print("\n TASK 2 ")

order, path = tree.bfs('A', 'J')

print("Visited order:", " -> ".join(order))

print("Path:", " -> ".join(path))
