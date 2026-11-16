#LAB7:
class Graph:

    def __init__(self):
        self.adj = {}

    # build the graph
    def add_edge(self, u, v):
        self.adj.setdefault(u, []).append(v)
        self.adj.setdefault(v, [])

    def display(self):
        print("Adjacency List:")
        for node, neighbours in self.adj.items():
            print(f"  {node} -> {neighbours}")

    # Depth Limited Search (recursive DFS with a depth cut-off)
    def dls(self, node, goal, limit, path, visited):
        visited.append(node)                 # record visiting order
        if node == goal:
            return True
        if limit <= 0:                       # depth limit reached, stop expanding
            return False
        for neighbour in self.adj.get(node, []):
            path.append(neighbour)
            if self.dls(neighbour, goal, limit - 1, path, visited):
                return True
            path.pop()                       # backtrack
        return False

    def run_dls(self, start, goal, limit):
        path, visited = [start], []
        found = self.dls(start, goal, limit, path, visited)
        return found, path, visited

    # Iterative Deepening Search (DLS with limit 0, 1, 2, ...)
    def iddfs(self, start, goal, max_depth):
        total = 0
        for limit in range(max_depth + 1):
            found, path, visited = self.run_dls(start, goal, limit)
            total += len(visited)
            print(f"Limit {limit}: {visited} -> {'Goal found' if found else 'Fail'}")
            if found:
                return path, total
        return None, total


# main program
g = Graph()
for u, v in [('A','B'), ('A','F'), ('A','D'), ('A','E'),
             ('B','K'), ('B','J'), ('K','N'), ('K','M'),
             ('D','G'), ('E','C'), ('E','H'), ('E','I'), ('I','L')]:
    g.add_edge(u, v)
g.display()

print("\n=== a) Depth Limited Search (Start = A, Goal = G) ===")
for limit in (1, 2):
    found, path, visited = g.run_dls('A', 'G', limit)
    print(f"Limit {limit}: found={found}, visited={visited}")
    if found:
        print("Path:", " -> ".join(path))

print("\n=== b) Iterative Deepening Search ===")
path, total = g.iddfs('A', 'G', 5)
print("Path:", " -> ".join(path) if path else "No path")
print("Total node visits:", total)
