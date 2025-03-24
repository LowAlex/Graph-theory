def scheduling(ranks, val_matrix, tasks):
    num_nodes = len(val_matrix)
    earliest_date = [0] * num_nodes
    total_float = [0] * num_nodes
    free_float = [0] * num_nodes

    # Compute ranks to determine processing order
    sorted_nodes = sorted(range(num_nodes), key=lambda x: ranks[x])

    # Compute earliest dates
    for node in sorted_nodes:
        if node == 0: # The only task with no predecessor is 0, whose earliest date is always 0
            earliest_date[node] = 0
            continue
        for predecessor in range(num_nodes):
            if val_matrix[predecessor][node] != '*':
                earliest_date[node] = max(earliest_date[node], earliest_date[predecessor] + val_matrix[predecessor][node])


    # Compute latest dates
    latest_date = [earliest_date[-1]] * num_nodes

    for node in sorted_nodes[::-1]:  # Reverse topological order
        if node == num_nodes - 1: # The latest date of the N+1 (or omega) task, is equal to its earliest date
            continue
        for successor in range(num_nodes):
            if val_matrix[node][successor] != '*':
                latest_date[node] = min(latest_date[node], latest_date[successor] - val_matrix[node][successor])


    # Compute Floats
    for node in range(num_nodes):
        total_float[node] = latest_date[node] - earliest_date[node]
        free_float[node] = total_float[node]
        if total_float[node] == 0:
            continue
        else:
            for successor in range(num_nodes):
                if val_matrix[node][successor] != '*':
                    free_float[node] = min(free_float[node], earliest_date[successor] - (earliest_date[node] + val_matrix[node][successor]))


    print("Sorted nodes: ", sorted_nodes)
    print("Earliest date: ", earliest_date)
    print("Latest date: ", latest_date)
    print("Total float: ", total_float)
    print("Free float: ", free_float)

    return earliest_date, latest_date, total_float, free_float