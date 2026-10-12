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

    #  DFS using a stack
    def dfs(self, start, goal=None, show_stack=True):
       
        stack = [start]                 # Python list used as a stack (append = push, pop = pop)
        visited = set()                 # marks visited nodes
        parent = {start: None}          # to rebuild the path from start to goal
        order = []                      # order in which nodes are visited

        while stack:                    # repeat until stack is empty
            node = stack.pop()          # take the TOP of the stack
            if node in visited:
                continue
            visited.add(node)           # mark as visited
            order.append(node)
            if show_stack:
                print(f"Visited: {str(node):<3} | Stack after pop: {stack}")

            if node == goal:            # goal found -> stop
                print(f"\nGoal node '{goal}' found!")
                return order, self._build_path(parent, goal)

            # push neighbours in REVERSE so the left-most child is popped first
            for neighbour in reversed(self.adj.get(node, [])):
                if neighbour not in visited:
                    parent[neighbour] = node
                    stack.append(neighbour)

        if goal is not None:
            print(f"\nGoal node '{goal}' not found.")
        return order, None

    @staticmethod
    def _build_path(parent, goal):
        path = []
        while goal is not None:
            path.append(goal)
            goal = parent[goal]
        return path[::-1]


#  main program 
print("=" * 55)
print("GRAPH 1: Numbered tree (1 to 12) - visit all nodes")
print("=" * 55)
g1 = Graph()
g1.add_edge(1, 2)
g1.add_edge(1, 7)
g1.add_edge(1, 8)
g1.add_edge(2, 3)
g1.add_edge(2, 6)
g1.add_edge(3, 4)
g1.add_edge(3, 5)
g1.add_edge(8, 9)
g1.add_edge(8, 12)
g1.add_edge(9, 10)
g1.add_edge(9, 11)
g1.display()

print("\nDFS (visit all nodes, start = 1)\n")
order, _ = g1.dfs(1, show_stack=False)
print("Visiting order :", " -> ".join(map(str, order)))

# Graph 2: 
print("\n GRAPH 2: Letter tree - DFS using Stack (Start = A, Goal = G)")
g2 = Graph()
g2.add_edge('A', 'B')
g2.add_edge('A', 'F')
g2.add_edge('A', 'D')
g2.add_edge('A', 'E')
g2.add_edge('B', 'K')
g2.add_edge('B', 'J')
g2.add_edge('K', 'N')
g2.add_edge('K', 'M')
g2.add_edge('D', 'G')
g2.add_edge('E', 'C')
g2.add_edge('E', 'H')
g2.add_edge('E', 'I')
g2.add_edge('I', 'L')
g2.display()

print("\nDFS using Stack\n")
order, path = g2.dfs('A', 'G')
print("Visiting order :", " -> ".join(order))
print("Path to goal   :", " -> ".join(path) if path else "No path")
