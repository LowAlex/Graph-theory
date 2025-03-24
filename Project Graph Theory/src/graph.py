def read_constraint_file(filename):
    val_matrix = []
    tasks = {}
    neg=0
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()

        num_tasks = 0
        for line in lines:
            if line.strip():
                num_tasks += 1

        val_matrix = [['*'] * (num_tasks + 2) for _ in range(num_tasks + 2)]


        for line in lines:
            if line.strip():
                parts = list(map(int, line.split()))
                task_id, duration = parts[0], parts[1]
                tasks[task_id] = {'duration': duration, 'predecessors': []}


        for line in lines:
            if line.strip():
                parts = list(map(int, line.split()))
                task_id = parts[0]
                predecessors = parts[2:]

                for pred in predecessors:
                    if pred in tasks:
                        tasks[task_id]['predecessors'].append(pred)
                        val_matrix[pred][task_id] = tasks[pred]['duration']
                        if tasks[pred]['duration']<0 :
                            neg=1



        for task_id in range(1, num_tasks + 1):
            if not tasks[task_id]['predecessors']:
                val_matrix[0][task_id] = 0


        for task_id in range(1, num_tasks + 1):
            if not any(task_id in tasks[t]['predecessors'] for t in range(1, num_tasks + 1)):
                val_matrix[task_id][num_tasks + 1] = tasks[task_id]['duration']

        return val_matrix, tasks, neg

    except FileNotFoundError:
        print(f"File {filename} not found")
    except Exception as e:
        print(f"Error: {e}")
