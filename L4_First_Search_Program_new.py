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

def getList(xy, path):
    openList = []
    for i in range(len(delta)):
        new_xy = [xy[0] + delta[i][0], xy[1] + delta[i][1]]
        if 0 <= new_xy[0] < len(grid) and 0 <= new_xy[1] < len(grid[0]) and grid[new_xy[0]][new_xy[1]] == 0:
            openList.append([path + cost] + new_xy)
            grid[new_xy[0]][new_xy[1]] = -1
    return openList

def search(grid,init,goal,cost):
    # ----------------------------------------
    # insert code here
    # ----------------------------------------
    xy = init
    grid[init[0]][init[1]] = -1
    step = 0
    openList = [[step] + xy]
    while len(openList) > 0:
        for list in openList:
            xy = list[1:]
            step = list[0]
            if xy == goal:
                return list
            newList = getList(xy, step)
            # print newList
            openList.remove(list)
            openList += newList
    path = 'fail'
    return path
print search(grid,init,goal,cost)