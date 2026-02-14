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

def misplaced_tile(state, target): # count # of tiles in the wrong spot
    n = len(state) # no. of rows
    m = len(state[0]) # no. of columns 

    misplaced = 0
    for row in range(n):
        for col in range(m): # we can use this for loop to iterate through state 
            if state[row][col] != target[row][col] and state[row][col] != 0: 
                # we check if a certain position is not equal to target and if its not the blank space (aka 0)
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

def EXPAND(node, problem): # how to go from one state to another
    children = []
    n = len(node.state) # no of row
    m = len(node.state[0]) # no of columns

    def valid(row, col):
        return 0 <= row < n and 0 <= col < m # checking if we're in bounds

    # find the blank
    blank_row, blank_col = 0, 0
    for i in range(n):
        for j in range(m):
            if node.state[i][j] == 0:
                blank_row, blank_col = i, j

    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]] # directions we canmove in

    for dx, dy in directions:
        nr, nc = blank_row + dx, blank_col + dy # new row and new column

        if valid(nr, nc): # if the new coordinate is valid 
            new_state = []
            for row in node.state:
                new_row = []
                for val in row:
                    new_row.append(val)
                new_state.append(new_row)

            # swap blank with the target tile
            new_state[blank_row][blank_col], new_state[nr][nc] = new_state[nr][nc], new_state[blank_row][blank_col]

            new_cost = node.cost + 1 # child's cost = parent's cost + 1
            child = Node(new_state, node, new_cost)
            children.append(child)

    return children 

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