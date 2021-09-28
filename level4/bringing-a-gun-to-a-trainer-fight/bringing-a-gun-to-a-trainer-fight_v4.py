import math
from fractions import Fraction


def solution(dimensions, your_position, trainer_position, distance):

    if math.atan2(0,8) == math.atan2(0, -8):
        print("yes")

    width = dimensions[0]
    height = dimensions[1]
    total = 0

    me = (your_position[0], your_position[1])
    trainer = (trainer_position[0], trainer_position[1])

    jump_x1 = trainer[0] * 2  # left
    jump_x2 = (width - trainer[0]) * 2  # right
    jump_y1 = trainer[1] * 2  # down
    jump_y2 = (height - trainer[1]) * 2  # up

    me_jump_x1 = me[0] * 2  # left
    me_jump_x2 = (width - me[0]) * 2  # right
    me_jump_y1 = trainer[1] * 2  # down
    me_jump_y2 = (height - me[1]) * 2  # up

    mirror_x = int(math.ceil(distance / width) + 2)
    mirror_y = int(math.ceil(distance / height) + 2)

    trainer_locations = set()
    trainer_locations2 = set()
    me_locations = set()

    # build mirrors
    x = trainer[0]
    me_x = me[0]
    i = 0
    for a in range(1, mirror_x + 1):
        y = trainer[1]
        me_y = me[1]
        j = 0
        for b in range(1, mirror_y + 1):

            if math.sqrt(math.pow(x - me[0], 2) + math.pow(y - me[1], 2)) <= distance:
                if math.atan2(x - me[0], y - me[1]) not in me_locations:
                    trainer_locations.add(math.atan2(x - me[0], y - me[1]))
                    trainer_locations2.add((x - me[0], y - me[1]))

            me_locations.add(math.atan2(me_x - me[0], me_y - me[1]))
            me_locations.add(math.atan2(-me_x - me[0], me_y - me[1]))
            me_locations.add(math.atan2(me_x - me[0], -me_y - me[1]))
            me_locations.add(math.atan2(-me_x - me[0], -me_y - me[1]))


            if math.sqrt(math.pow(-x - me[0], 2) + math.pow(y - me[1], 2)) <= distance:
                if math.atan2(-x - me[0], y - me[1]) not in me_locations:
                    trainer_locations.add(math.atan2(-x - me[0], y - me[1]))
                    trainer_locations2.add((-x - me[0], y - me[1]))


            if math.sqrt(math.pow(x - me[0], 2) + math.pow(-y - me[1], 2)) <= distance:
                if math.atan2(x - me[0], -y - me[1]) not in me_locations:
                    trainer_locations.add(math.atan2(x - me[0], -y - me[1]))
                    trainer_locations2.add((x - me[0], -y - me[1]))


            if math.sqrt(math.pow(-x - me[0], 2) + math.pow(-y - me[1], 2)) <= distance:
                if math.atan2(-x - me[0], -y - me[1]) not in me_locations:
                    trainer_locations.add(math.atan2(-x - me[0], -y - me[1]))
                    trainer_locations2.add((-x - me[0], -y - me[1]))


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

    #print(trainer_locations2)
    #print(len(trainer_locations))
    return len(trainer_locations)


# print(solution([10, 10], [3, 3], [6, 6], 20))
print(solution([3, 2], [1, 1], [2, 1], 4))  # 7
print(solution([300, 275], [150, 150], [185, 100], 500))  # 9
print(solution([2, 5], [1, 2], [1, 4], 11)) # 27
#print(solution([2, 3], [1, 2], [1, 1], 4))  # 7

print(solution([23, 10], [6, 4], [3, 2], 23))  # 8
print(solution([3, 2], [1, 1], [2, 1], 4))  # 7
print(solution([2, 3], [1, 2], [1, 1], 4))  # 7
#print(solution([10, 10], [1, 1], [9, 9], 10))  # 0
#print(solution([10, 5], [1, 1], [1, 3], 3))  # 2
#print(solution([10, 2], [2, 1], [9, 1], 10))  # 5
#print(solution([3, 2], [1, 1], [2, 1], 8))  # 7?
#(solution([3, 2], [1, 1], [2, 2], 8))  # 4?
#print(solution([3, 2], [1, 1], [2, 2], 1))  # 0
#print(solution([3, 3], [1, 1], [3, 3], 1))  # 0
#print(solution([4, 4], [1, 1], [3, 3], 2))  # 0
#print(solution([4, 4], [1, 1], [3, 3], 3))  # 1?
#print(solution([3, 3], [1, 1], [1, 2], 1))  # 1
print(solution([10, 10], [1, 1], [1, 9], 8))  # 1
print(solution([10, 10], [1, 1], [9, 1], 8))  # 1
print(solution([10, 10], [9, 1], [1, 1], 8))  # 1
print(solution([10, 10], [1, 9], [1, 1], 8))  # 1
print(solution([10, 10], [5, 5], [5, 6], 3))  # 1
print(solution([10, 10], [2, 2], [4, 4], 10))  # 3


print(solution([10, 10], [4, 4], [3, 3], 5000))  # 739323?
# print(solution([1250, 1250], [150, 150], [185, 100], 500))  # 9
