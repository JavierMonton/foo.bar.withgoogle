# Generate all possible directions, follow them, break if repeated path
import math


def solution(dimensions, your_position, trainer_position, distance):

    width = dimensions[0]
    height = dimensions[1]

    me = (your_position[0], your_position[1])
    trainer = (trainer_position[0], trainer_position[1])

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
        found = follow_path_non_recursive(first_step, me, trainer, width, height, direction, distance + new_distance, max_distance, passed)
        if found is True:
            total += 1
            directions.append(orig_direction)

    #for d in directions:
    #    print("(" + str(d.x) + ", " + str(d.y) + ")")

    for d in directions:
        for e in directions:
            if d.x != 0 and d.y !=0 and (abs(d.x) != abs(e.x) and abs(e.y) != abs(d.y)) and e.x % d.x == 0 and e.y % d.y == 0 and e.x // d.x == e.y // d.y:  # repeated direction
                #print(" -- (" + str(e.x) + ", " + str(e.y) + ")")
                total -= 1
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


def check_repeated(x, y):
    return x == 1 or y == 1 or (x % y != 0 and y % x != 0)


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


def follow_path_non_recursive(start_point, me, goal, width, height, direction, distance, max_distance, passed, found=False):
    """
    Follow the path of a bullet without recursion (max recursion depth of python is 1000)
    """
    while True:
        if distance > max_distance:  # more distance than possible
            break
        #if str(start_point) in passed and passed[str(start_point)].x == direction.x and passed[str(start_point)].y == direction.y:  # repeated step - less performance but less steps
        #    return False
        if start_point == goal:
            found = True
            break
        if start_point == me:  # we should skip first iteration of this outside of this function
            break
        ####
        #passed[str(start_point)] = direction
        start_point, new_distance = step(start_point, direction, width, height)
        distance = distance + new_distance
    return found


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
    if y > height:
        tmp = y - height
        y = height - tmp
        direction.y = direction.y * -1
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
print(solution([2, 3], [1, 2], [1, 1], 8))  # 7
print(solution([10, 10], [1, 1], [9, 9], 10))  # 0
print(solution([3, 2], [1, 1], [2, 1], 8))  # 7?
print(solution([3, 2], [1, 1], [2, 2], 8))  # 4?
print(solution([3, 2], [1, 1], [2, 2], 1))  # 0
print(solution([3, 3], [1, 1], [3, 3], 1))  # 0
print(solution([4, 4], [1, 1], [3, 3], 2))  # 0
print(solution([4, 4], [1, 1], [3, 3], 3))  # 1?
print(solution([3, 3], [1, 1], [1, 2], 1))  # 1
print(solution([300, 275], [150, 150], [185, 100], 500))  # 9
#print(solution([300, 275], [150, 150], [185, 100], 5000))  # 133?
#print(solution([1250, 1250], [150, 150], [185, 100], 500))  # 4?
#print(solution([1250, 1250], [150, 150], [185, 100], 500))  # 9