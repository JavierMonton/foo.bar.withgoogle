# Generate all possible directions, iterate over them, skipping repeated paths
def solution(dimensions, your_position, trainer_position, distance):

    width = dimensions[0]
    height = dimensions[1]

    me = (your_position[0], your_position[1])
    trainer = (trainer_position[0], trainer_position[1])

    p = generate_possibilities(width, height)
    total = 0
    directions = []

    for direction in p:
        passed = {}
        first_step = step(me, direction, width, height)
        found = follow_path(first_step, me, trainer, width, height, direction, distance - 1, passed)
        if found is True:
            total += 1
            directions.append(direction)

    print(directions)
    return total



def generate_possibilities(width, height):
    """
    Given an scenario, creates an array of possibilities where the trainer can shot
    """
    p = []
    p.append((0, 1))
    p.append((1, 0))
    for i in range(1, width+1):
        for j in range(1, height+1):
            if check_repeated(i, j) is True:
                p.append((i, j))
                p.append((-i, j))
                p.append((i, -j))
                p.append((-i, -j))
    return p


def check_repeated(x, y):
    return x == 1 or y == 1 or (x % y != 0 and y % x != 0)


def follow_path(start_point, me, goal, width, height, direction, distance, passed, found=False):
    """
    Follow the path of a bullet
    """
    if str(start_point) in passed:  # repeated step
        return False
    if start_point == goal:
        return True
    if start_point == me or distance == 0:  # we should skip first iteration of this outside of this function
        return False
    ####
    passed[str(start_point)] = True
    return follow_path(step(start_point, direction, width, height), me, goal, width, height, direction, distance - 1, passed, found)


def step(a, b, width, height):
    """
    Makes a move on tuples, using walls or not
    :param a: start point
    :param b: direction
    :param width: max width
    :param height: max height
    :return: tuple with new location
    """
    x = a[0] + b[0]
    y = a[1] + b[1]
    if x > width:
        tmp = x - width
        x = width - tmp
    if y > height:
        tmp = y - height
        y = height - tmp
    if x < 1:
        x = abs(x)
    if y < 1:
        y = abs(y)

    return (x, y)


print(solution([3, 2], [1, 1], [2, 1], 4))  # 7
print(solution([300, 275], [150, 150], [185, 100], 500))  # 9
#print(solution([1250, 1250], [150, 150], [185, 100], 500))  # 9