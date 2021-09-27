import math


def solution(dimensions, your_position, trainer_position, distance):

    width = dimensions[0]
    height = dimensions[1]
    total = 0

    me = (your_position[0], your_position[1])
    trainer = (trainer_position[0], trainer_position[1])

    jump_x1 = trainer[0] * 2  # left
    jump_x2 = (width - trainer[0]) * 2  # right
    jump_y1 = trainer[1] * 2  # down
    jump_y2 = (width - trainer[0]) * 2  # up

    me_jump_x1 = me[0] * 2  # left
    me_jump_x2 = (width - me[0]) * 2  # right
    me_jump_y1 = trainer[1] * 2  # down
    me_jump_y2 = (width - me[0]) * 2  # up

    mirror_x = int(math.ceil(distance / width) + 2)
    mirror_y = int(math.ceil(distance / height) + 2)

    trainer_locations = []
    me_locations = []

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
            me_locations.append((me_x, me_y))
            me_locations.append((-me_x, me_y))
            me_locations.append((me_x, -me_y))
            me_locations.append((-me_x, -me_y))
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

    #print(trainer_locations)
    #print(me_locations)

    # check distance + valid shot
    for t in trainer_locations:
        distance_x = t[0] - me[0]
        distance_y = t[1] - me[1]
        total_distance = math.sqrt(math.pow(distance_x, 2) + math.pow(distance_y, 2))
        i = 1
        if total_distance < distance:

            me_distance_x = me_locations[i][0] - me[0]
            me_distance_y = me_locations[i][1] - me[1]

            x_0 = me_distance_x == 0 and distance_x == 0
            y_0 = me_distance_y == 0 and distance_y == 0

            m_x = distance_x != 0 and me_distance_x != 0 and me_distance_x <= distance_x and distance_x % me_distance_x == 0
            m_y = distance_y != 0 and me_distance_y != 0 and me_distance_y <= distance_y and distance_y % me_distance_y == 0

            if x_0 and me_distance_y != 0 and abs(me_distance_y) < abs(distance_y):
                total -= 0
            elif y_0 and me_distance_x != 0 and abs(me_distance_x) < abs(distance_x):
                total -= 0
            elif m_x and m_y and distance_x // me_distance_x == distance_y // me_distance_y:
                total -= 0
            else:
                print("(" + str(distance_x) + ", " + str(distance_y) + ")")
                total += 1
        i += 1

    return total










#print(solution([10, 10], [3, 3], [6, 6], 20))
print(solution([3, 2], [1, 1], [2, 1], 4))  # 7
print(solution([300, 275], [150, 150], [185, 100], 500))  # 9
#print(solution([1250, 1250], [150, 150], [185, 100], 500))  # 9