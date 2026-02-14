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

def MAKE_NODE(state, method, target): # first node in tree
    h = method(state, target)

    return Node(state, None, 0, h)

def MAKE_QUEUE(node): # create queue with just our initial state 
    return [node]

def EMPTY(nodes): # if queue is empty then return False
    return len(nodes) == 0

def REMOVE_FRONT(nodes): # we can get the lowest cost node from the queue
    return nodes.pop(0)

def QUEUEING_FUNCTION(nodes, children, method, target): 
    for child in children: # find h(n) 
        child.h = method(child.state, target)
        nodes.append(child)

    def total_cost(node): # F(n) = g(n) + h(n) 
        return node.cost + node.h
    # using python sort function here, and sorting by the cost
    nodes.sort(key=total_cost)
    return nodes

def general_search_algorithm(problem, method):
    # nodes = MAKE-QUEUE(MAKE-NODE(problem.INITIAL-STATE))
    nodes = MAKE_QUEUE(MAKE_NODE(problem.initial_state, method, problem.target))

    seen = set()
    nodes_expanded = 0
    max_queue_size = 0

    # loop do
    while True:
        # if EMPTY(nodes) then return failure
        if EMPTY(nodes):
            return "failure"

        # tracking peak of the queue size. 
        if len(nodes) > max_queue_size:
            max_queue_size = len(nodes)

        # node = REMOVE-FRONT(nodes)
        node = REMOVE_FRONT(nodes)

        # if problem.GOAL-TEST(node.STATE) succeeds then return node
        if problem.goal_test(node.state):
            return node, nodes_expanded, max_queue_size

        # this is so we can check with the seen set, python adjustment 
        key = []
        for vals in node.state:
            key.append(tuple(vals))
        key = tuple(key)

        # only expand if we havent seen this state before
        if key not in seen: # prevent cycles 
            seen.add(key)
            nodes_expanded += 1 # tracking how many nodes we expanded so far

            print("The best state to expand with a g(n) =" + str(node.cost) + "and h(n) =" + str(node.h) + "is:")

            for row in node.state:
                print(row)
            # nodes = QUEUEING-FUNCTION(nodes, EXPAND(node, problem.OPERATORS))
            children = EXPAND(node, problem)
            nodes = QUEUEING_FUNCTION(nodes, children, method, problem.target)
            
def main():
    print("8 puzzle")

if __name__ == "__main__":
    main()