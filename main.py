from node import Node
from queue import Queue
import time

initial_state = [
    [None, 0, 1],
    [2, 3, 4],
    [5, 6, 7]
]

desired_state = [
    [6, 4, 0],
    [2, 3, None],
    [5, 7, 1],
]

explored_set = []

desired_node = Node(state=desired_state)

print(f"Desired node key: {desired_node.key}")


queue = Queue()
queue.push(Node(state=initial_state), desired_state)
start_time = time.process_time()
optimal_node = None
path_count = 0
while not queue.is_empty():
    a = queue.pop()
    explored_set.append(a.key)
    if optimal_node is not None:
        if a.cost > optimal_node.cost:
            continue
    if a.is_equal_to(desired_node.key):
        path_count += 1
        if optimal_node is None:
            optimal_node = a
        else:
            if a.cost < optimal_node.cost:
                optimal_node = a
    else:
        nodes = a.calculate_child_nodes()
        for n in nodes:
            if optimal_node is not None:
                if n.key not in explored_set and n.cost < optimal_node.cost:
                    queue.push(n, desired_state)
                    # print(n.key)
            else:
                if n.key not in explored_set:
                    queue.push(n, desired_state)
                    # print(n.key)
        # print(f"added {len(nodes)} new nodes to queue")
        # print(f"total items in queue: {len(queue.items)}")


if optimal_node is not None:
    optimal_node.print()
    print(f"is desired state with cost of {optimal_node.cost}")
    print(f"there are {path_count} paths to reach desired state")
    print(f"took {time.process_time() - start_time} to reach desired state")
else:
    print("there is no way to reach desired stat")
