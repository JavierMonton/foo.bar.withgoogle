import math


def solution(dimensions, your_position, trainer_position, distance):

    width = dimensions[0]
    height = dimensions[1]

    me = (your_position[0], your_position[1])
    trainer = (trainer_position[0], trainer_position[1])

    jump_x1 = trainer[0] * 2  # left
    jump_x2 = (width - trainer[0]) * 2  # right
    jump_y1 = trainer[1] * 2  # down
    jump_y2 = (height - trainer[1]) * 2  # up

    me_jump_x1 = me[0] * 2  # left
    me_jump_x2 = (width - me[0]) * 2  # right
    me_jump_y1 = me[1] * 2  # down
    me_jump_y2 = (height - me[1]) * 2  # up

    mirror_x = int(math.ceil(distance / width) + 2)
    mirror_y = int(math.ceil(distance / height) + 2)

    trainer_locations = []
    me_distances = {}  # key angle, value distance

    # build mirrors
    x = trainer[0]
    me_x = me[0]
    i = 0
    for a in range(1, mirror_x + 1):
        y = trainer[1]
        me_y = me[1]
        j = 0
        for b in range(1, mirror_y + 1):

            trainer_locations.append((x, y))
            trainer_locations.append((-x, y))
            trainer_locations.append((x, -y))
            trainer_locations.append((-x, -y))

            put_clones(me, me_distances, (me_x, me_y))
            put_clones(me, me_distances, (-me_x, me_y))
            put_clones(me, me_distances, (me_x, -me_y))
            put_clones(me, me_distances, (-me_x, -me_y))

            if j % 2 == 1:
                y = y + jump_y1
                me_y = me_y + me_jump_y1
            else:
                y = y + jump_y2
                me_y = me_y + me_jump_y2
            j += 1

        if i % 2 == 1:
            x = x + jump_x1
            me_x = me_x + me_jump_x1
        else:
            x = x + jump_x2
            me_x = me_x + me_jump_x2
        i += 1

    total_angles = set()  # to avoid duplicates
    for t in trainer_locations:
        new_distance = compute_distance(t, me)
        if new_distance <= distance:
            angle = astr(t, me)
            if angle not in me_distances or me_distances[angle] > new_distance:
                total_angles.add(angle)

    return len(total_angles)


def put_clones(me, me_distances, new_me):
    """
    Insert a "new me" using angle as key. If the "new me" is closer, it replaces the old one
    """
    new_me_distance = compute_distance(new_me, me)
    if new_me_distance != 0:
        # if it doesn't exists or it's greater than new distance
        if astr(new_me, me) not in me_distances or me_distances[astr(new_me, me)] > new_me_distance:
            me_distances[astr(new_me, me)] = new_me_distance


def astr(a, b):
    return str(compute_angle(a, b))


def compute_angle(a, b):
    return math.atan2(a[0] - b[0], a[1] - b[1])


def compute_distance(a, b):
    return math.sqrt(math.pow(a[0] - b[0], 2) + math.pow(a[1] - b[1], 2))


print(solution([10, 10], [3, 3], [6, 6], 20))  # 11
print(solution([3, 2], [2, 1], [1, 1], 4))  # 7
print(solution([3, 2], [1, 1], [2, 1], 4))  # 7
print(solution([300, 275], [150, 150], [185, 100], 500))  # 9
print(solution([2, 5], [1, 2], [1, 4], 11))  # 27
print(solution([10, 10], [6, 6], [5, 5], 60))  # 103

