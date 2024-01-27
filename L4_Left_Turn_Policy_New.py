# ----------
# User Instructions:
#
# Implement the function optimum_policy2D below.
#
# You are given a car in grid with initial state
# init. Your task is to compute and return the car's
# optimal path to the position specified in goal;
# the costs for each motion are as defined in cost.
#
# There are four motion directions: up, left, down, and right.
# Increasing the index in this array corresponds to making a
# a left turn, and decreasing the index corresponds to making a
# right turn.

forward = [[-1,  0], # go up
           [ 0, -1], # go left
           [ 1,  0], # go down
           [ 0,  1]] # go right
forward_name = ['up', 'left', 'down', 'right']

# action has 3 values: right turn, no turn, left turn
action = [-1, 0, 1]
action_name = ['R', '#', 'L']

# EXAMPLE INPUTS:
# grid format:
#     0 = navigable space
#     1 = unnavigable space
grid = [[1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1]]

init = [4, 3, 0] # given in the form [row,col,direction]
                 # direction = 0: up
                 #             1: left
                 #             2: down
                 #             3: right

goal = [2, 0] # given in the form [row,col]

cost = [2, 1, 20] # cost has 3 values, corresponding to making
                  # a right turn, no turn, and a left turn

# EXAMPLE OUTPUT:
# calling optimum_policy2D with the given parameters should return
# [[' ', ' ', ' ', 'R', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', '#'],
#  ['*', '#', '#', '#', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', ' '],
#  [' ', ' ', ' ', '#', ' ', ' ']]
# ----------

# ----------------------------------------
# modify code below
# ----------------------------------------
def show_expand(expand):
    print "[up, left, down, right]"
    for ex in expand:
        print ex
def optimum_policy2D(grid,init,goal,cost):
    policy2D = [[' ' for col in range(len(grid[0]))] for row in range(len(grid))]
    heuristic = [[[999, 999, 999, 999] for col in range(len(grid[0]))] for row in range(len(grid))]
    # heuristic[goal[0]][goal[1]] = [0, 0, 0, 0]
    changed = True
    openlist = [[0, -1, goal[0], goal[1]]]
    while len(openlist) > 0 :
        newlist = []
        # print openlist
        for op in openlist:
            h = op[0]
            f = op[1]
            x = op[2]
            y = op[3]
            for i, a in enumerate(forward):
                x2 = x + a[0]
                y2 = y + a[1]
                if 0 <= x2 < len(grid) and 0 <= y2 < len(grid[0]) and grid[x2][y2] == 0:
                    real_orn =(i - 2) % 4
                    if f == -1:
                        f = real_orn
                        f2 = real_orn
                        h2 = h
                    else:
                        if (real_orn - f) % 4 == 2:
                            continue
                        f2 = real_orn
                        h2 = h + cost[(f - f2 + 1) % 4]
                    if heuristic[x][y][real_orn] > h2:
                        heuristic[x][y][real_orn] = h2
                        newlist.append([h2, f2, x2, y2])
                        # show_expand(heuristic)
        openlist = newlist
    # show_expand(heuristic)
    path = [0, -1, init[0], init[1]]
    changed = True
    while changed and path[1:] != goal:
        changed = False
        openlist = []
        h = path[0]
        f = path[1]
        x = path[2]
        y = path[3]
        for i, a in enumerate(forward):
            x2 = x + a[0]
            y2 = y + a[1]
            if 0 <= x2 < len(grid) and 0 <= y2 < len(grid[0]) and grid[x2][y2] == 0:
                if f == -1:
                    f = i
                if (i - f) % 4 == 2:
                    continue
                f2 = i
                h2 = 0
                for actInx, act in enumerate(action):
                    if (act + f) % 4 == f2:
                        h2 = cost[actInx] + heuristic[x2][y2][i]
                openlist.append([h2, f2, x2, y2])
                changed = True
        if len(openlist) > 0:
            openlist.sort()
            # print openlist
            path = openlist.pop(0)
            # print path
            f2 = path[1]
            x2 = path[2]
            y2 = path[3]
            for i, act in enumerate(action):
                if (act + f) % 4 == f2:
                    policy2D[x][y] = action_name[i]
    policy2D[goal[0]][goal[1]] = '*'
    return policy2D

policy = optimum_policy2D(grid,init,goal,cost)
for p in policy:
    print p
