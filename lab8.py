# Task 1 + Task 2: Greedy Best First Search and A* on the Romania map
import heapq


class Romania:
    def __init__(self):
        # Road distances between cities
        self.graph = {
            "Arad": {"Zerind": 75, "Sibiu": 140, "Timisoara": 118},
            "Zerind": {"Arad": 75, "Oradea": 71},
            "Oradea": {"Zerind": 71, "Sibiu": 151},
            "Timisoara": {"Arad": 118, "Lugoj": 111},
            "Lugoj": {"Timisoara": 111, "Mehadia": 70},
            "Mehadia": {"Lugoj": 70, "Dobreta": 75},
            "Dobreta": {"Mehadia": 75, "Craiova": 120},
            "Craiova": {"Dobreta": 120, "Rimnicu Vilcea": 146, "Pitesti": 138},
            "Sibiu": {"Arad": 140, "Oradea": 151, "Fagaras": 99, "Rimnicu Vilcea": 80},
            "Rimnicu Vilcea": {"Sibiu": 80, "Craiova": 146, "Pitesti": 97},
            "Fagaras": {"Sibiu": 99, "Bucharest": 211},
            "Pitesti": {"Rimnicu Vilcea": 97, "Craiova": 138, "Bucharest": 101},
            "Bucharest": {"Fagaras": 211, "Pitesti": 101, "Giurgiu": 90, "Urziceni": 85},
            "Giurgiu": {"Bucharest": 90},
            "Urziceni": {"Bucharest": 85, "Hirsova": 98, "Vaslui": 142},
            "Hirsova": {"Urziceni": 98, "Eforie": 86},
            "Eforie": {"Hirsova": 86},
            "Vaslui": {"Urziceni": 142, "Iasi": 92},
            "Iasi": {"Vaslui": 92, "Neamt": 87},
            "Neamt": {"Iasi": 87},
        }
        # Straight-line distance to Bucharest (heuristic h)
        self.h = {
            "Arad": 366, "Bucharest": 0, "Craiova": 160, "Dobreta": 242,
            "Eforie": 161, "Fagaras": 176, "Giurgiu": 77, "Hirsova": 151,
            "Iasi": 226, "Lugoj": 244, "Mehadia": 241, "Neamt": 234,
            "Oradea": 380, "Pitesti": 100, "Rimnicu Vilcea": 193, "Sibiu": 253,
            "Timisoara": 329, "Urziceni": 80, "Vaslui": 199, "Zerind": 374,
        }

    # Task 1: Greedy Best First Search   f(n) = h(n)
    def greedy(self, start, goal):
        open_list = [(self.h[start], start, [start])]   # (h, city, path)
        closed = set()

        while open_list:
            _, city, path = heapq.heappop(open_list)    # lowest h first

            if city == goal:
                return path, self.path_cost(path)
            if city in closed:
                continue
            closed.add(city)

            for neighbour in self.graph[city]:
                if neighbour not in closed:
                    heapq.heappush(open_list, (self.h[neighbour], neighbour, path + [neighbour]))
        return None, None

    # Task 2: A* Search   f(n) = g(n) + h(n)
    def a_star(self, start, goal):
        open_list = [(self.h[start], 0, start, [start])]   # (f, g, city, path)
        closed = set()

        while open_list:
            f, g, city, path = heapq.heappop(open_list)    # lowest f first

            if city == goal:
                return path, g
            if city in closed:
                continue
            closed.add(city)

            for neighbour, cost in self.graph[city].items():
                if neighbour not in closed:
                    new_g = g + cost
                    new_f = new_g + self.h[neighbour]
                    heapq.heappush(open_list, (new_f, new_g, neighbour, path + [neighbour]))
        return None, None

    def path_cost(self, path):
        return sum(self.graph[path[i]][path[i + 1]] for i in range(len(path) - 1))


if __name__ == "__main__":
    romania = Romania()

    path, cost = romania.greedy("Arad", "Bucharest")
    print("Greedy:", " -> ".join(path))
    print("Cost  :", cost)
    print()

    path, cost = romania.a_star("Arad", "Bucharest")
    print("A*    :", " -> ".join(path))
    print("Cost  :", cost)






# Task 3: 8 Puzzle using A*   (0 = empty square)
# Heuristic: number of misplaced tiles
import heapq

start = (1, 2, 3,
         5, 6, 0,
         7, 8, 4)

goal  = (1, 2, 3,
         5, 8, 6,
         0, 7, 4)

def heuristic(state):
    return sum(1 for i in range(9) if state[i] != 0 and state[i] != goal[i])

def get_neighbours(state):
    result = []
    i = state.index(0)            # position of empty square
    row, col = divmod(i, 3)
    moves = {"Up": (-1, 0), "Down": (1, 0), "Left": (0, -1), "Right": (0, 1)}
    for name, (dr, dc) in moves.items():
        r, c = row + dr, col + dc
        if 0 <= r < 3 and 0 <= c < 3:
            j = r * 3 + c
            new = list(state)
            new[i], new[j] = new[j], new[i]   # slide tile into empty square
            result.append((tuple(new), name))
    return result

def solve(start, goal):
    open_list = [(heuristic(start), 0, start, [])]   # (f, g, state, moves)
    closed = set()

    while open_list:
        f, g, state, moves = heapq.heappop(open_list)

        if state == goal:
            return moves
        if state in closed:
            continue
        closed.add(state)

        for new_state, move in get_neighbours(state):
            if new_state not in closed:
                new_g = g + 1
                heapq.heappush(open_list,
                               (new_g + heuristic(new_state), new_g, new_state, moves + [move]))
    return None

def show(state):
    for r in range(3):
        print(" ".join(str(x) if x != 0 else "_" for x in state[r * 3:r * 3 + 3]))
    print()

print("Start:");  show(start)
print("Goal:");   show(goal)

solution = solve(start, goal)
if solution is None:
    print("No solution")
else:
    print("Moves (of the empty square):", ", ".join(solution))
    print("Number of moves:", len(solution))



