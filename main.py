from node import Node
from queue import Queue

initial_state = [
    [None, 0, 1],
    [2, 3, 4],
    [5, 6, 7]
]

desired_state = [
    [2, 0, 1],
    [3, None, 4],
    [5, 6, 7]
]


queue = Queue()
queue.push(Node(state=initial_state))
i = 0
while not queue.is_empty():
    a = queue.pop()
    if a.is_equal_to(desired_state):
        a.print()
        print(f"is desired state with cost of {a.cost}")
        break
    else:
        nodes = a.calculate_child_nodes()
        for n in nodes:
            queue.push(n)
        # print(f"added {len(nodes)} new nodes to queue")
        # print(f"total items in queue: {len(queue.items)}")
        i += 1
        print(i)
