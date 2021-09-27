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

    mirror_x = math.ceil(distance / width) + 2
    mirror_y = math.ceil(distance / height) + 2

    trainer_locations = []

    # build mirrors
    x = trainer[0]
    i = 0
    for a in range(1, mirror_x + 1):
        y = trainer[1]
        j = 0
        for b in range(1, mirror_y + 1):
            trainer_locations.append((x, y))
            trainer_locations.append((-x, y))
            trainer_locations.append((x, -y))
            trainer_locations.append((-x, -y))
            if j % 2 == 1:
                y = y + jump_y1
            else:
                y = y + jump_y2
            j += 1

        if i % 2 == 1:
            x = x + jump_x1
        else:
            x = x + jump_x2
        i += 1

    print(trainer_locations)

    # check distance + valid shot
    for option in trainer_locations:
        distance_x = option[0] - me[0]
        distance_y = option[1] - me[1]
        if math.sqrt(math.pow(distance_x, 2) + math.pow(distance_y, 2)) < distance:
            print("(" + str(distance_x) + ", " + str(distance_y) + ")")
            total += 1

    return total










#print(solution([10, 10], [3, 3], [6, 6], 20))
print(solution([3, 2], [1, 1], [2, 1], 4))  # 7
print(solution([300, 275], [150, 150], [185, 100], 500))  # 9
#print(solution([1250, 1250], [150, 150], [185, 100], 500))  # 9