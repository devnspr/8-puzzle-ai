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


def find_diff(a, desired_state):
    for k in range(0, 3):
        for l in range(0, 3):
            if desired_state[k][l] == a:
                return k, l
    return -1, -1


def calculate_f(state, desired_state):
    s = 0
    for i in range(0, 3):
        for j in range(0, 3):
            k, l= find_diff(state[i][j], desired_state)
            s += abs(k - i) + abs(l - j)
    return s


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
        self.key = self.generate_node_key()
        self.available_actions = self.calculate_available_actions()
        self.cost = parent_cost + 1
        pass

    def generate_node_key(self):
        keyarr = [f"{self.state[i][j] if self.state[i][j] is not None else '-'}" for i in range(0, 3) for j in range(0, 3)]
        return ''.join(keyarr)

    def calculate_available_actions(self):
        actions = [top, bottom, left, right]
        acc = []
        for action in actions:
            if is_valid_action(self.i, self.j, action):
                acc.append(action)
        return acc

    def is_equal_to(self, key):
        return self.key == key

    def calculate_child_nodes(self):
        nodes = []
        for action in self.available_actions:
            try:
                n = Node([self.state[i].copy() for i in range(0, 3)], action, self.cost)
                nodes.append(n)
            except Exception as e:
                print(e)
        return nodes

    def calculate_state(self, initial=None):
        if initial is None:
            self.state = self.parent_state
            initial_i, initial_j = 0, 0
            for i in range(0, 3):
                for j in range(0, 3):
                    if self.state[i][j] is None:
                        try:
                            initial_i, initial_j = i, j
                            self.i, self.j = calculate_to_ij(i, j, self.parent_action)
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


