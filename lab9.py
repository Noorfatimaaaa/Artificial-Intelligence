#Q1: minimax.py:
import math

def minimax(node, depth, is_max):
    if not isinstance(node, list):      # leaf
        return node

    if is_max:
        best = -math.inf
        for child in node:
            best = max(best, minimax(child, depth + 1, False))
        return best
    else:
        best = math.inf
        for child in node:
            best = min(best, minimax(child, depth + 1, True))
        return best


#          A
#       B     C
#      D E   F G
# leaves: H I J K L M N O
tree = [[[-1, 4], [2, 6]], [[-3, -5], [0, 7]]]

print("Optimal value:", minimax(tree, 0, True))



#Q2: alphabeta.py:
import math

def alphabeta(node, depth, is_max, alpha, beta):
    if not isinstance(node, list):      # leaf
        return node

    if is_max:
        best = -math.inf
        for child in node:
            best = max(best, alphabeta(child, depth + 1, False, alpha, beta))
            alpha = max(alpha, best)
            if beta <= alpha:
                print("Pruned!")
                break
        return best
    else:
        best = math.inf
        for child in node:
            best = min(best, alphabeta(child, depth + 1, True, alpha, beta))
            beta = min(beta, best)
            if beta <= alpha:
                print("Pruned!")
                break
        return best


#        A
#     B     C
#   D   E  F   G
tree = [[[3, 5], [6, 9]], [[1, 2], [0, -1]]]

print("Optimal value:", alphabeta(tree, 0, True, -math.inf, math.inf))
