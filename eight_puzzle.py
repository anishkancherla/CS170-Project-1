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
    # ucs is just A* but with h(n) hardcoded to 0
    return 0

def misplaced_tile(state, target):
    n = len(state)
    m = len(state[0])
    
    misplaced = 0
    for row in range(n):
        for col in range(m):
            if state[row][col] != target[row][col] and state[row][col] != 0:
                misplaced += 1
    
    return misplaced

def manhattan_distance(state, target):
    n = len(state) # no of rows
    m = len(state[0]) # no of columns

    total_dist = 0

    for row in range(n): # iterate over the board 
        for col in range(m):
            if state[row][col] != 0: # don't count blank space
                new_row, new_col = 0, 0

                for i in range(n): # for every single tile in board we find the match in target board
                    for j in range(m):
                        if target[i][j] == state[row][col]: # store coordinates if its a match
                            new_row, new_col = i, j
                # distance calculation
                row_total_distance = abs(row - new_row) # find # of steps up or down 
                col_total_distance = abs(col - new_col) # find # of steps left or right
                total_dist = total_dist + row_total_distance + col_total_distance
    
    return total_dist

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