from main import *
from collections import deque

def compute_ranks(val_matrix):
    num_nodes = len(val_matrix)
    in_degree = [0] * num_nodes
    ranks = [-1] * num_nodes
    queue = deque()

    # Compute in-degrees
    print("* Calculating in-degrees")
    for i in range(num_nodes):
        for j in range(num_nodes):
            if val_matrix[i][j] != '*':
                in_degree[j] += 1

    print(f"In-degrees: {in_degree}")

    # Find entry points (nodes with in-degree 0)
    print("* Finding entry points")
    for i in range(num_nodes):
        if in_degree[i] == 0:
            queue.append(i)
            ranks[i] = 0
    print(f"Initial entry points: {list(queue)}")

    # Perform BFS to compute ranks
    print("* Performing BFS to calculate ranks")
    while queue:
        node = queue.popleft()
        print(f"Processing node {node}, Rank: {ranks[node]}")
        for neighbor in range(num_nodes):
            if val_matrix[node][neighbor] != '*':
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
                    ranks[neighbor] = max(ranks[neighbor], ranks[node] + 1)
                    print(f"Node {neighbor} now has Rank {ranks[neighbor]}")

    # Check for isolated nodes
    print("* Checking for isolated nodes")
    for i in range(num_nodes):
        if ranks[i] == -1:
            ranks[i] = 0
            print(f"Node {i} is isolated, setting Rank to 0")
    for i in range (1,num_nodes):
        ranks[i] = ranks[i]+1

    return ranks