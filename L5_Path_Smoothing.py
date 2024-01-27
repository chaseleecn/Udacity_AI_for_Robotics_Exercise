# -----------
# User Instructions
#
# Define a function smooth that takes a path as its input
# (with optional parameters for weight_data, weight_smooth,
# and tolerance) and returns a smooth path. The first and 
# last points should remain unchanged.
#
# Smoothing should be implemented by iteratively updating
# each entry in newpath until some desired level of accuracy
# is reached. The update should be done according to the
# gradient descent equations given in the instructor's note
# below (the equations given in the video are not quite 
# correct).
# -----------

from copy import deepcopy

# thank you to EnTerr for posting this on our discussion forum
def printpaths(path,newpath):
    for old,new in zip(path,newpath):
        print '['+ ', '.join('%.3f'%x for x in old) + \
               '] -> ['+ ', '.join('%.3f'%x for x in new) +']'

# Don't modify path inside your function.
path = [[0, 0],
        [0, 1],
        [0, 2],
        [1, 2],
        [2, 2],
        [3, 2],
        [4, 2],
        [4, 3],
        [4, 4]]

def smooth(path, weight_data = 0.5, weight_smooth = 0.1, tolerance = 0.000001):

    # Make a deep copy of path into newpath
    newpath = deepcopy(path)

    #######################
    ### ENTER CODE HERE ###
    #######################
    cost1 = 0
    cost2 = abs(path[0][0] - newpath[0][0] + path[0][1] - newpath[0][1]) + \
            abs(newpath[0][0] - newpath[1][0] + newpath[0][1] - newpath[1][1])
    delta = 999999
    count = 0
    while delta >= tolerance:
        count += 1
        for i in range(1, len(path) - 1):
            newpath[i][0] += weight_data * (path[i][0] - newpath[i][0]) + \
                             weight_smooth * (newpath[i + 1][0] + newpath[i - 1][0] - 2 * newpath[i][0])
            newpath[i][1] += weight_data * (path[i][1] - newpath[i][1]) + \
                             weight_smooth * (newpath[i + 1][1] + newpath[i - 1][1] - 2 * newpath[i][1])
        cost1 = 0
        for i in range(1, len(path)):
            cost1 += abs(path[i][0] - newpath[i][0]) + abs(path[i][1] - newpath[i][1]) + \
                     abs(newpath[i - 1][0] - newpath[i][0]) + abs(newpath[i - 1][1] - newpath[i][1])

        delta = abs(cost2 - cost1)
        cost2 = cost1
    return newpath # Leave this line for the grader!

printpaths(path,smooth(path, 0, 0.1))
