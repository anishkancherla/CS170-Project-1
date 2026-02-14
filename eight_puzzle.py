class Node:
    def __init__(self, state, parent, cost, h=0):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.h = h

class Problem:
    def __init__(self, initial_state):
        self.initial_state = initial_state
        self.target = [[1, 2, 3],
                       [4, 5, 6],
                       [7, 8, 0]]
    
    def goal_test(self, state):
        return state == self.target

# Search algorithms
def uniform_cost_search(state, target): 
    return 0

def misplaced_tile(state, target):
    # implement
    pass

def manhattan_distance(state, target):
    # implement
    pass

def EXPAND(node, problem):
    
    pass

def MAKE_NODE(state, method, target):
    pass

def MAKE_QUEUE(node):
    return [node]

def EMPTY(nodes):
    return len(nodes) == 0

def REMOVE_FRONT(nodes):
    return nodes.pop(0)

def QUEUEING_FUNCTION(nodes, children, method, target):
    pass

def general_search_algorithm(problem, method):
    pass

def main():
    print("8 puzzle")

if __name__ == "__main__":
    main()