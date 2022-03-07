from node import calculate_f
import numpy as np


def find_nearest(array, value):
    array = np.asarray(array)
    try:
        idx = (np.abs(array - value)).argmin()
        return idx
    except Exception as e:
        return -1


class Queue:

    def __init__(self):
        self.items = []
        self.fs = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item, desired_state):
        f = calculate_f(item.state, desired_state)
        if self.is_empty():
            self.fs.append(f)
            self.items.append(item)
        else:
            nearest_idx = find_nearest(self.fs, f)
            insert_at = 0
            if nearest_idx >= 0:
                insert_at = nearest_idx if self.fs[nearest_idx] > f else nearest_idx + 1
            self.items.insert(insert_at, item)
            self.fs.insert(insert_at, f)
            # print(f"{f}, {self.fs[nearest_idx]}")
            print(f"inserted at {insert_at}")

    def pop(self):
        if self.is_empty():
            raise IndexError("Queue is Empty!")
        else:
            item = self.items[0]
            del self.items[0]
            del self.fs[0]
            return item
