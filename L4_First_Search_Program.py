# ----------
# User Instructions:
#
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']


def search(grid, init, goal, cost):
    # ----------------------------------------
    # insert code here
    # ----------------------------------------
    openlist = [[0, init[0], init[1]]]
    path = []
    while len(path) == 0 and len(openlist) > 0:
        for lst in openlist:
            if lst[1] == goal[0] and lst[2] == goal[1]:
                path = lst
            for d in delta:
                r = lst[1] + d[0]
                c = lst[2] + d[1]
                if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == 0:
                    openlist.append([lst[0] + cost, r, c])
                    grid[r][c] = 2
            openlist.remove(lst)
    if len(path) == 0:
        path = 'fail'
    return path

print search(grid, init, goal, cost)