# Generate all possible directions, follow them, break if repeated path
import math

def solution(dimensions, your_position, trainer_position, distance):

    width = dimensions[0]
    height = dimensions[1]

    me = (your_position[0], your_position[1])
    trainer = (trainer_position[0], trainer_position[1])

    #p = []
    #p.append(Direction(0, 1))
    #p.append(Direction(1, 0))
    #p.append(Direction(0, -1))
    #p.append(Direction(-1, 0))
    #p1 = generate_direct_possibilities(p, width-me[0]+1, height-me[1]+1, True, True)
    #p2 = generate_direct_possibilities(p, width, height, False, False)
    #p3 = generate_direct_possibilities(p, width - me[0] + 1, height, True, False)
    #p4 = generate_direct_possibilities(p, width, height - me[1] + 1, False, True)
    p = generate_possibilities(width, height)
    total = 0
    directions = []
    max_distance = distance
    distance = 0

    for direction in p:
        orig_direction = Direction(direction.x, direction.y)
        #if orig_direction.x == 7 and orig_direction.y == -10:
        #    print("pass")
        passed = {}
        first_step, new_distance = step(me, direction, width, height)
        found = follow_path(first_step, me, trainer, width, height, direction, distance + new_distance, max_distance, passed)
        if found is True:
            total += 1
            #directions.append(orig_direction)

    #for d in directions:
     #   print("(" + str(d.x) + ", " + str(d.y) + ")")
    return total


class Direction:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def generate_possibilities(width, height):
    """
    Given an scenario, creates an array of possibilities where the trainer can shot
    """
    p = []
    p.append(Direction(0, 1))
    p.append(Direction(1, 0))
    p.append(Direction(0, -1))
    p.append(Direction(-1, 0))
    for i in range(1, width+1):
        for j in range(1, height+1):
            if check_repeated(i, j) is True:
                p.append(Direction(i, j))
                p.append(Direction(-i, j))
                p.append(Direction(i, -j))
                p.append(Direction(-i, -j))
    return p


def generate_direct_possibilities(p, width, height, x_sign, y_sign):
    """
    Given an scenario, creates an array of possibilities where the trainer can shot in one direction
    """

    for i in range(1, width+1):
        for j in range(1, height+1):
            if check_repeated(i, j) is True:
                if x_sign is True and y_sign is True:
                    p.append(Direction(i, j))
                if x_sign is False and y_sign is False:
                    p.append(Direction(-i, -j))
                if x_sign is True and y_sign is False:
                    p.append(Direction(i, -j))
                if x_sign is False and y_sign is True:
                    p.append(Direction(-i, j))
    return p


def check_repeated(x, y):
    return x == 1 or y == 1 or (x % y != 0 and y % x != 0)


def follow_path(start_point, me, goal, width, height, direction, distance, max_distance, passed, found=False):
    """
    Follow the path of a bullet
    """
    if distance > max_distance:  # more distance than possible
        return False
    #if str(start_point) in passed:  # repeated step
    #    return False
    if start_point == goal:
        return True
    if start_point == me:  # we should skip first iteration of this outside of this function
        return False
    ####
    #passed[str(start_point)] = True
    point, new_distance = step(start_point, direction, width, height)
    return follow_path(point, me, goal, width, height, direction, distance + new_distance, max_distance, passed, found)


def step(a, direction, width, height):
    """
    Makes a move on tuples, using walls or not
    :param a: start point
    :param direction: direction
    :param width: max width
    :param height: max height
    :return: tuple with new location and number of walls used
    """
    x = a[0] + direction.x
    y = a[1] + direction.y
    x_distance = abs(direction.x)
    y_distance = abs(direction.y)
    if x > width:
        tmp = x - width
        x = width - tmp
        direction.x = direction.x * -1
        #x_distance = x_distance + x_distance
        #y_distance = y_distance + y_distance
    if y > height:
        tmp = y - height
        y = height - tmp
        direction.y = direction.y * -1
        #x_distance = x_distance + x_distance
        #y_distance = y_distance + y_distance
    if x < 1:
        x = abs(x)
        direction.x = direction.x * -1
    if y < 1:
        y = abs(y)
        direction.y = direction.y * -1

    tmp = (x, y)
    xd = x_distance * x_distance
    yd = y_distance * y_distance
    distance = math.sqrt(xd + yd)
    return tmp, distance


print(solution([3, 2], [1, 1], [2, 1], 4))  # 7
print(solution([3, 2], [1, 1], [2, 2], 8))  # 4?
print(solution([3, 2], [1, 1], [2, 2], 1))  # 0
print(solution([3, 3], [1, 1], [3, 3], 1))  # 0
print(solution([4, 4], [1, 1], [3, 3], 2))  # 0
print(solution([4, 4], [1, 1], [3, 3], 3))  # 1?
print(solution([3, 3], [1, 1], [1, 2], 1))  # 1
print(solution([300, 275], [150, 150], [185, 100], 500))  # 9
#print(solution([1250, 1250], [150, 150], [185, 100], 500))  # 9