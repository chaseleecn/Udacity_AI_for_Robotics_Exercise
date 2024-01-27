# ----------
# User Instructions:
#
# Create a function compute_value which returns
# a grid of values. The value of a cell is the minimum
# number of moves required to get from the cell to the goal.
#
# If a cell is a wall or it is impossible to reach the goal from a cell,
# assign that cell a value of 99.
# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1 # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']


def compute_value(grid, goal, cost):
    # ----------------------------------------
    # insert code below
    # ----------------------------------------
    value = [[99 for i in range(len(grid[0]))] for j in range(len(grid))]
    x = goal[0]
    y = goal[1]
    val = 0
    openlist = [[val, x, y]]
    newlist = []
    value[x][y] = val
    while len(openlist) > 0 or len(newlist) > 0:
        if len(openlist) == 0:
            openlist = newlist
            newlist = []
        print openlist
        print
        for lst in openlist:
            val = lst[0]
            x = lst[1]
            y = lst[2]
            val += 1
            for i in range(len(delta)):
                x2 = x + delta[i][0]
                y2 = y + delta[i][1]
                if 0 <= x2 < len(grid) and 0 <= y2 < len(grid[0]):
                    if value[x2][y2] == 99 and grid[x2][y2] == 0:
                        newlist.append([val, x2, y2])
                        value[x2][y2] = val
            openlist.remove(lst)

    # make sure your function returns a grid of values as
    # demonstrated in the previous video.
    return value

value = compute_value(grid, goal, cost)
for v in value:
    print v