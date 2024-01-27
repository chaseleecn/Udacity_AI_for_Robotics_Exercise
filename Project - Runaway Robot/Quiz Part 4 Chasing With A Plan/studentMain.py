# ----------
# Part Four
#
# Again, you'll track down and recover the runaway Traxbot.
# But this time, your speed will be about the same as the runaway bot.
# This may require more careful planning than you used last time.
#
# ----------
# YOUR JOB
#
# Complete the next_move function, similar to how you did last time.
#
# ----------
# GRADING
#
# Same as part 3. Again, try to catch the target in as few steps as possible.

from robot import *
from math import *
from matrix import *
import random
t_list = []
d_list = []
max_count = 1
def avg_tlist():
    num = 1.0 * sum(t_list) / len(t_list)
    # print "avg t =", num
    return num
    # return t_list[-1]
def avg_dlist():
    num = 1.0 * sum(d_list) / len(d_list)
    # print "avg d =", num
    return num
    # return d_list[-1]
def next_move(hunter_position, hunter_heading, target_measurement, max_distance, OTHER = None):
    # This function will be called after each time the target moves.
    if not OTHER: # first time calling this function, set up my OTHER variables.
        measurements = [target_measurement]
        hunter_positions = [hunter_position]
        hunter_headings = [hunter_heading]
        # OTHER = (measurements, hunter_positions, hunter_headings) # now I can keep track of history
        x, y, h, t, d = target_measurement[0], target_measurement[1], 0., 0., 0.
        xx, yy = x, y
        xxx, yyy = xx, yy
    else: # not the first time, update my history
        # OTHER[0].append(target_measurement)
        # OTHER[1].append(hunter_position)
        # OTHER[2].append(hunter_heading)
        # measurements, hunter_positions, hunter_headings = OTHER # now I can always refer to these variables
        xp, yp, hp, tp, dp = OTHER
        x, y = target_measurement
        d = distance_between([x, y], [xp, yp])
        if len(d_list) < max_count:
            d_list.append(d)
        else:
            d_list.pop(0)
            d_list.append(d)
        # print x < xp, y < yp
        if x < xp and y >= yp:
            # print "acos"
            num = (x - xp) / avg_dlist()
            if abs(num) > 1:
                num /= abs(num)
            h = (acos(num))
        elif x < xp and y < yp:
            num = (x - xp) / avg_dlist()
            if abs(num) > 1:
                num /= abs(num)
            h = (-acos(num))
        else:
            # print "asin"
            num = (y - yp) / avg_dlist()
            if abs(num) > 1:
                num /= abs(num)
            h = angle_trunc(asin(num))
        t = (h - hp)
        if len(t_list) < max_count:
            t_list.append(t)
        else:
            t_list.pop(0)
            t_list.append(t)
        # print "[x, y] = [%f, %f], h = %f, t = %f, d = %f"%(x, y, h, t, d)
        xx = x + avg_dlist() * cos(angle_trunc(h + avg_tlist()))
        yy = y + avg_dlist() * sin(angle_trunc(h + avg_tlist()))
        xxx = xx + avg_dlist() * cos(angle_trunc(h + 2*avg_tlist()))
        yyy = yy + avg_dlist() * sin(angle_trunc(h + 2*avg_tlist()))
    target_future_position = [xxx, yyy]
    heading_to_target = get_heading(hunter_position, target_future_position)
    heading_difference = angle_trunc(heading_to_target - hunter_heading)
    # if heading_difference > 0:
    #     heading_difference = angle_trunc(heading_difference + 0.3)
    # else:
    #     heading_difference = angle_trunc(heading_difference - 0.01)
    turning =  heading_difference # turn towards the target
    distance = distance_between(hunter_position, target_future_position)
    print "distance =", distance
    if distance > max_distance:
        distance = max_distance # full speed ahead!

    OTHER = [x, y, h, t, d]
    return turning, distance, OTHER

def distance_between(point1, point2):
    """Computes distance between point1 and point2. Points are (x, y) pairs."""
    x1, y1 = point1
    x2, y2 = point2
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def demo_grading(hunter_bot, target_bot, next_move_fcn, OTHER = None):
    """Returns True if your next_move_fcn successfully guides the hunter_bot
    to the target_bot. This function is here to help you understand how we
    will grade your submission."""
    max_distance = 0.98 * target_bot.distance # 0.98 is an example. It will change.
    separation_tolerance = 0.02 * target_bot.distance # hunter must be within 0.02 step size to catch target
    caught = False
    ctr = 0
    #For Visualization
    import turtle
    window = turtle.Screen()
    window.bgcolor('white')
    chaser_robot = turtle.Turtle()
    chaser_robot.shape('arrow')
    chaser_robot.color('blue')
    chaser_robot.resizemode('user')
    chaser_robot.shapesize(0.8, 0.8, 0.8)
    broken_robot = turtle.Turtle()
    broken_robot.shape('turtle')
    broken_robot.color('green')
    broken_robot.resizemode('user')
    broken_robot.shapesize(0.8, 0.8, 0.8)
    size_multiplier = 15.0 #change size of animation
    chaser_robot.hideturtle()
    chaser_robot.penup()
    chaser_robot.goto(hunter_bot.x*size_multiplier, hunter_bot.y*size_multiplier-100)
    chaser_robot.showturtle()
    broken_robot.hideturtle()
    broken_robot.penup()
    broken_robot.goto(target_bot.x*size_multiplier, target_bot.y*size_multiplier-100)
    broken_robot.showturtle()
    measuredbroken_robot = turtle.Turtle()
    measuredbroken_robot.shape('circle')
    measuredbroken_robot.color('red')
    measuredbroken_robot.penup()
    measuredbroken_robot.resizemode('user')
    measuredbroken_robot.shapesize(0.1, 0.1, 0.1)
    broken_robot.pendown()
    chaser_robot.pendown()
    #End of Visualization
    # We will use your next_move_fcn until we catch the target or time expires.
    while not caught and ctr < 1000:
        # Check to see if the hunter has caught the target.
        hunter_position = (hunter_bot.x, hunter_bot.y)
        target_position = (target_bot.x, target_bot.y)
        separation = distance_between(hunter_position, target_position)
        print separation
        if separation < separation_tolerance:
            print "You got it right! It took you ", ctr, " steps to catch the target."
            caught = True

        # The target broadcasts its noisy measurement
        target_measurement = target_bot.sense()

        # This is where YOUR function will be called.
        turning, distance, OTHER = next_move_fcn(hunter_position, hunter_bot.heading, target_measurement, max_distance, OTHER)

        # Don't try to move faster than allowed!
        if distance > max_distance:
            distance = max_distance

        # We move the hunter according to your instructions
        hunter_bot.move(turning, distance)

        # The target continues its (nearly) circular motion.
        target_bot.move_in_circle()
        #Visualize it
        measuredbroken_robot.setheading(target_bot.heading*180/pi)
        measuredbroken_robot.goto(target_measurement[0]*size_multiplier, target_measurement[1]*size_multiplier-100)
        measuredbroken_robot.stamp()
        broken_robot.setheading(target_bot.heading*180/pi)
        broken_robot.goto(target_bot.x*size_multiplier, target_bot.y*size_multiplier-100)
        chaser_robot.setheading(hunter_bot.heading*180/pi)
        chaser_robot.goto(hunter_bot.x*size_multiplier, hunter_bot.y*size_multiplier-100)
        #End of visualization
        ctr += 1
        if ctr >= 1000:
            print "It took too many steps to catch the target."
    return caught



def angle_trunc(a):
    """This maps all angles to a domain of [-pi, pi]"""
    while a < 0.0:
        a += pi * 2
    return ((a + pi) % (pi * 2)) - pi

def get_heading(hunter_position, target_position):
    """Returns the angle, in radians, between the target and hunter positions"""
    hunter_x, hunter_y = hunter_position
    target_x, target_y = target_position
    heading = atan2(target_y - hunter_y, target_x - hunter_x)
    heading = angle_trunc(heading)
    return heading

def naive_next_move(hunter_position, hunter_heading, target_measurement, max_distance, OTHER):
    """This strategy always tries to steer the hunter directly towards where the target last
    said it was and then moves forwards at full speed. This strategy also keeps track of all
    the target measurements, hunter positions, and hunter headings over time, but it doesn't
    do anything with that information."""
    if not OTHER: # first time calling this function, set up my OTHER variables.
        measurements = [target_measurement]
        hunter_positions = [hunter_position]
        hunter_headings = [hunter_heading]
        OTHER = (measurements, hunter_positions, hunter_headings) # now I can keep track of history
    else: # not the first time, update my history
        OTHER[0].append(target_measurement)
        OTHER[1].append(hunter_position)
        OTHER[2].append(hunter_heading)
        measurements, hunter_positions, hunter_headings = OTHER # now I can always refer to these variables

    heading_to_target = get_heading(hunter_position, target_measurement)
    heading_difference = angle_trunc(heading_to_target - hunter_heading)
    turning =  heading_difference # turn towards the target
    distance = max_distance # full speed ahead!
    return turning, distance, OTHER

target = robot(0.0, 10.0, 0.0, 2*pi / 30, 1.5)
measurement_noise = .05*target.distance
target.set_noise(0.0, 0.0, measurement_noise)

hunter = robot(-10.0, -10.0, 0.0)

# print demo_grading(hunter, target, naive_next_move)
print demo_grading(hunter, target, next_move)





