# --------------
# USER INSTRUCTIONS
#
# Write a function called stochastic_value that
# returns two grids. The first grid, value, should
# contain the computed value of each cell as shown
# in the video. The second grid, policy, should
# contain the optimum policy for each cell.
#
# --------------
# GRADING NOTES
#
# We will be calling your stochastic_value function
# with several different grids and different values
# of success_prob, collision_cost, and cost_step.
# In order to be marked correct, your function must
# RETURN (it does not have to print) two grids,
# value and policy.
#
# When grading your value grid, we will compare the
# value of each cell with the true value according
# to this model. If your answer for each cell
# is sufficiently close to the correct answer
# (within 0.001), you will be marked as correct.

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>'] # Use these when creating your policy grid.

# ---------------------------------------------
#  Modify the function stochastic_value below
# ---------------------------------------------

def stochastic_value(grid,goal,cost_step,collision_cost,success_prob):
    failure_prob = (1.0 - success_prob)/2.0 # Probability(stepping left) = prob(stepping right) = failure_prob
    value = [[collision_cost for col in range(len(grid[0]))] for row in range(len(grid))]
    policy = [[' ' for col in range(len(grid[0]))] for row in range(len(grid))]
    x = goal[0]
    y = goal[1]
    value[x][y] = 0.0
    changed = True
    while changed:
        changed = False
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                for i, a in enumerate(delta):
                    x2 = x + a[0]
                    y2 = y + a[1]
                    if 0 <= x2 < len(grid) and 0 <= y2 < len(grid[0]) and grid[x2][y2] == 0:
                        v3 = success_prob * value[x][y] + 1
                        x3 = x2 + delta[(i - 1) % 4][0]
                        y3 = y2 + delta[(i - 1) % 4][1]
                        if 0 <= x3 < len(grid) and 0 <= y3 < len(grid[0]):
                            f_val = value[x3][y3]
                        else:
                            f_val = collision_cost
                        v3 += failure_prob * f_val
                        x3 = x2 + delta[(i + 1) % 4][0]
                        y3 = y2 + delta[(i + 1) % 4][1]
                        if 0 <= x3 < len(grid) and 0 <= y3 < len(grid[0]):
                            f_val = value[x3][y3]
                        else:
                            f_val = collision_cost
                        v3 += failure_prob * f_val
                        if v3 < value[x2][y2]:
                            changed = True
                            value[x2][y2] = v3
                            policy[x2][y2] = delta_name[(i + 2) % 4]
    return value, policy

# ---------------------------------------------
#  Use the code below to test your solution
# ---------------------------------------------

grid = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 1, 1, 0]]
goal = [0, len(grid[0])-1] # Goal is in top right corner
cost_step = 1
collision_cost = 100.0
success_prob = 0.5

value, policy = stochastic_value(grid, goal, cost_step, collision_cost, success_prob)
for row in value:
    print row
for row in policy:
    print row

# Expected outputs:
#
# [57.9029, 40.2784, 26.0665,  0.0000]
# [47.0547, 36.5722, 29.9937, 27.2698]
# [53.1715, 42.0228, 37.7755, 45.0916]
# [77.5858, 100.00, 100.00, 73.5458]
#
# ['>', 'v', 'v', '*']
# ['>', '>', '^', '<']
# ['>', '^', '^', '<']
# ['^', ' ', ' ', '^']
