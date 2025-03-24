from main import *

def has_cycle(val_matrix):
    num_nodes = len(val_matrix)
    visited = [False] * num_nodes
    rec_stack = [False] * num_nodes

    def dfs(node):
        if not visited[node]:
            visited[node] = True
            rec_stack[node] = True
            print(f"* Visiting node {node}")

            for neighbor in range(num_nodes):
                if val_matrix[node][neighbor] != '*':
                    if not visited[neighbor] and dfs(neighbor):
                        return True
                    elif rec_stack[neighbor]:
                        print("-> Cycle detected!")
                        return True

        rec_stack[node] = False
        return False

    print("* Detecting a cycle using DFS")
    for node in range(num_nodes):
        if not visited[node]:
            if dfs(node):
                return True

    print("-> No cycle detected")
    return False