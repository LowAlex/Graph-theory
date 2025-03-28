from graph import *
from ranks import *
from cycle_detection import *
from scheduler import *
import sys

class Tee:
    def __init__(self, filename):
        self.file = open(filename, "w")
        self.stdout = sys.stdout  # Sauvegarde la sortie standard

    def write(self, message):
        self.stdout.write(message)  # Affiche dans le terminal
        self.file.write(message)    # Écrit dans le fichier

    def flush(self):
        self.stdout.flush()
        self.file.flush()

sys.stdout = Tee("output.txt")


def main():
    while True:
        filename = input("Enter the name of the .txt file (or 'exit' to quit): ")
        if filename.lower() == "exit":
            break

        try:
            val_matrix, tasks, neg = read_constraint_file(filename)

            num_vertices = len(val_matrix) - 2  # Exclude(0 et N+1)

            # edges = []
            #
            # for i in range(1, num_vertices + 1):
            #     if not tasks[i]['predecessors']:
            #         edges.append((0, i, 0))
            #
            #     has_successor = False
            #     for j in range(1, num_vertices + 1):
            #         if val_matrix[i][j] != '*':
            #             edges.append((i, j, val_matrix[i][j]))
            #             has_successor = True
            #
            #     if not has_successor:
            #         edges.append((i, num_vertices + 1, tasks[i]['duration']))
            #
            # edges.sort(key=lambda x: x[0])
            # print(f"{num_vertices} sommets")
            # print(f"{len(edges)} arêtes")
            # for edge in edges:
            #     print(f"{edge[0]} -> {edge[1]} = {edge[2]}")


            # Showing The value matrix
            print("\nValue matrix:")

            header = ['0'] + [str(i) for i in range(1, num_vertices + 2)]
            print("{:<4}".format(" "), end="")
            for h in header:
                print(f"{h:<4}", end="")
            print()

            for i in range(num_vertices + 2):
                print(f"{i:<4}", end="")
                for j in range(num_vertices + 2):
                    print(f"{val_matrix[i][j]:<4}", end="")
                print()

            # print("\nTask information:")
            #
            # print(f"Tâche 0: {{'duration': 0, 'predecessors': []}}")
            #
            # for task_id, task_info in tasks.items():
            #     if task_id == 1:
            #         task_info['predecessors'] = [0]
            #     elif task_id != num_vertices + 1:
            #         task_info['predecessors'] = [0] if not task_info['predecessors'] else task_info['predecessors']
            #
            #     print(f"Task {task_id}: {task_info}")
            #
            # print(f"Task {num_vertices + 1}: {{'duration': 0, 'predecessors': [", end="")
            # predecessors_of_n1 = [
            #     str(i) for i in range(1, num_vertices + 1)
            #     if val_matrix[i][num_vertices + 1] != 0
            # ]
            # print(", ".join(predecessors_of_n1), end="")
            # print("]}}")


            if neg == 0:
                print('No negative')
            else:
                print('Negative')


            if not has_cycle(val_matrix):
                if neg == 0:
                    ranks = compute_ranks(val_matrix)
                    print("\nVertex ranks:")
                    for i, rank in enumerate(ranks):
                        print(f"Vertex {i}: Rang {rank}")

                    scheduler = scheduling(ranks, val_matrix)


        except FileNotFoundError:
            print(f"File '{filename}' not found")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()