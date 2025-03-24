def scheduling(ranks, val_matrix):
    num_nodes = len(val_matrix)
    # Initialization of earliest date, total float, and free float
    earliest_date = [0] * num_nodes
    total_float = [0] * num_nodes
    free_float = [0] * num_nodes

    # Sort the nodes in topologocal order
    sorted_nodes = sorted(range(num_nodes), key=lambda x: ranks[x])

    # Compute earliest dates
    for node in sorted_nodes:
        if node == 0: # The only task with no predecessor is 0, whose earliest date is always 0
            earliest_date[node] = 0
            continue
        for predecessor in range(num_nodes):
            if val_matrix[predecessor][node] != '*':
                earliest_date[node] = max(earliest_date[node], earliest_date[predecessor] + val_matrix[predecessor][node]) # Course formula

    # Compute latest dates
    latest_date = [earliest_date[-1]] * num_nodes

    for node in sorted_nodes[::-1]:  # Reverse topological order
        if node == num_nodes - 1: # The latest date of the N+1 (or omega) task, is equal to its earliest date
            continue
        for successor in range(num_nodes):
            if val_matrix[node][successor] != '*':
                latest_date[node] = min(latest_date[node], latest_date[successor] - val_matrix[node][successor]) # Course formula

    # Compute Floats
    for node in range(num_nodes):
        total_float[node] = latest_date[node] - earliest_date[node] # Course formula
        free_float[node] = total_float[node]
        if total_float[node] == 0: # The free float of a task is always 0 if its total float is already 0
            continue
        else:
            for successor in range(num_nodes):
                if val_matrix[node][successor] != '*':
                    free_float[node] = min(free_float[node], earliest_date[successor] - (earliest_date[node] + val_matrix[node][successor])) # Course formula

    # Computation of all the steps in topological order
    earliest_date_top = [earliest_date[node] for node in sorted_nodes]
    latest_date_top = [latest_date[node] for node in sorted_nodes]
    total_float_top = [total_float[node] for node in sorted_nodes]
    free_float_top = [free_float[node] for node in sorted_nodes]

    print("Vertices in topological order: ", sorted_nodes)
    # print("Earliest date: ", earliest_date)
    print("Earliest date in topological order: ", earliest_date_top)
    # print("Latest date: ", latest_date)
    print("Latest date in topological order: ", latest_date_top)
    # print("Total float: ", total_float)
    print("Total float in topological order: ", total_float_top)
    # print("Free float: ", free_float)
    print("Free float in topological order: ", free_float_top)

    critical_path = [sorted_nodes[i] for i in range(len(total_float)) if total_float_top[i] == 0]
    print("Critical Path:", " -> ".join(map(str, critical_path)))

    return earliest_date, latest_date, total_float_top, free_float