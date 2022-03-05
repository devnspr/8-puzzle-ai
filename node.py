left = "L"
right = "R"
bottom = "B"
top = "T"


def is_valid_action(i, j, action):
    actions = [
        [[right, bottom], [left, right, bottom], [left, bottom]],
        [[top, right, bottom], [top, right, left, bottom], [left, top, bottom]],
        [[top, right], [left, right, top], [top, left]]
    ]
    return True if action in actions[i][j] else False


def calculate_to_ij(i, j, action):
    if is_valid_action(i, j, action):
        if action == left:
            return i, j - 1
        elif action == right:
            return i, j + 1
        elif action == top:
            return i - 1, j
        else:
            return i + 1, j
    else:
        raise Exception("action is not valid!")


class Node:

    def __init__(self, parent_state=None, parent_action=None, parent_cost=-1, state=None):
        self.state = [[0 for i in range(0, 3)] for j in range(0, 3)]
        self.i, self.j = 0, 0
        self.parent_state = parent_state
        self.parent_action = parent_action
        try:
            self.calculate_state(state)
        except Exception as e:
            raise e
        self.available_actions = self.calculate_available_actions()
        self.cost = parent_cost + 1
        pass

    def calculate_available_actions(self):
        actions = [top, bottom, left, right]
        acc = []
        for action in actions:
            if is_valid_action(self.i, self.j, action):
                acc.append(action)
        return acc

    def is_equal_to(self, state):
        for o in range(0, 3):
            for w in range(0, 3):
                if self.state[o][w] != state[o][w]:
                    return False
        return True

    def calculate_child_nodes(self):
        nodes = []
        for action in self.available_actions:
            try:
                n = Node([self.state[i].copy() for i in range(0, 3)], action, self.cost)
                nodes.append(n)
            except Exception as e:
                pass
        return nodes

    def calculate_state(self, initial=None):
        if initial is None:
            self.state = self.parent_state
            initial_i, initial_j = 0, 0
            for i in range(0, 3):
                for j in range(0, 3):
                    if self.state[i][j] is None:
                        try:
                            self.i, self.j = calculate_to_ij(i, j, self.parent_action)
                            initial_j, initial_j = i, j
                            break
                        except Exception as e:
                            raise e
            self.transit(initial_i, initial_j, self.i, self.j)
        else:
            self.state = initial
            for i in range(0, 3):
                for j in range(0, 3):
                    if self.state[i][j] is None:
                        self.i, self.j = i, j
                        break

    def transit(self, from_i, from_j, to_i, to_j):
        self.state[from_i][from_j], self.state[to_i][to_j] = self.state[to_i][to_j], self.state[from_i][from_j]

    def print(self):
        for i in range(0, 3):
            print(" ----- ----- ----- ")
            print(f"|  {self.state[i][0] if self.state[i][0] is not None else ' '}  |  {self.state[i][1] if self.state[i][1] is not None else ' '}  |  {self.state[i][2] if self.state[i][2] is not None else ' '}  |")
        print(" ----- ----- ----- ")


