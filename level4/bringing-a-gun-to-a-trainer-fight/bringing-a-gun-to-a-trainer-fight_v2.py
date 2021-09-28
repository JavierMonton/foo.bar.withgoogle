import math
from fractions import Fraction


def solution(dimensions, your_position, trainer_position, distance):

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
    # print(me_locations)
    # transform me_locations for me_direcitons
    print(len(trainer_locations))
    filter(lambda location: location[0] < distance and location[1] < distance, trainer_locations)
    print(len(trainer_locations))


    # check distance + valid shot
    for t in trainer_locations:
        distance_x = t[0] - me[0]
        distance_y = t[1] - me[1]
        total_distance = math.sqrt(math.pow(distance_x, 2) + math.pow(distance_y, 2))

        if total_distance <= distance:
            (str(distance_x) + ", " + str(distance_y))
            i = -1
            for t in me_locations:
                i += 1
                dir = (t[0] - me[0], t[1] - me[1])

                if distance_y != 0 and dir[1] != 0 and abs(dir[0]) <= abs(distance_x) and abs(dir[1]) <= abs(distance_y) and (distance_x != dir[0] or distance_y != dir[1]) and Fraction(distance_x, distance_y) == Fraction(dir[0], dir[1]) and (distance_x != dir[0]*-1 or distance_y != dir[1]*-1):
                    if distance_x == 0 and dir[0] == 0 and ((distance_y > 0 and dir[1] < 0) or (dir[1] > 0 and distance_y < 0)):
                        #print("weird case")
                        total = total
                    else:
                        #("got suicide on " + str(dir[0]) + ", " + str(dir[1]))
                        total -= 1
                        break
                elif distance_y == 0 and dir[1] == 0 and dir[0] != 0 and abs(dir[0]) <= abs(distance_x) and (distance_x != dir[0] or distance_y != dir[1]) and Fraction(distance_y, distance_x) == Fraction(dir[1], dir[0]):  # inverted Fraction to avoid division by 0
                    if ((distance_x > 0 and dir[0] < 0) or (dir[0] > 0 and distance_x < 0)):
                        #print("weird case x")
                        total = total
                    else:
                        #print(" -- got suicide on " + str(dir[0]) + ", " + str(dir[1]))
                        total -= 1
                        break
                # move this to a function, it's repeated
                dir = (trainer_locations[i][0] - me[0], trainer_locations[i][1] - me[1])
                if distance_y != 0 and dir[1] != 0 and abs(dir[0]) <= abs(distance_x) and abs(dir[1]) <= abs(distance_y) and (distance_x != dir[0] or distance_y != dir[1]) and Fraction(distance_x, distance_y) == Fraction(dir[0], dir[1]) and (distance_x != dir[0]*-1 or distance_y != dir[1]*-1):
                    #print("got repeated on " + str(dir[0]) + ", " + str(dir[1]))
                    total -= 1
                    break
                elif distance_y == 0 and dir[1] == 0 and dir[0] != 0 and abs(dir[0]) <= abs(distance_x) and (distance_x != dir[0] or distance_y != dir[1]) and Fraction(distance_y, distance_x) == Fraction(dir[1], dir[0]):  # inverted Fraction to avoid division by 0
                    #print(" -- got repeated on " + str(dir[0]) + ", " + str(dir[1]))
                    total -= 1
                    break
            total += 1

    return total


# print(solution([10, 10], [3, 3], [6, 6], 20))
#print(solution([3, 2], [1, 1], [2, 1], 4))  # 7
print(solution([300, 275], [150, 150], [185, 100], 500))  # 9
#print(solution([2, 5], [1, 2], [1, 4], 11)) # 27
#print(solution([2, 3], [1, 2], [1, 1], 4))  # 7

#print(solution([23, 10], [6, 4], [3, 2], 23))  # 8
#print(solution([3, 2], [1, 1], [2, 1], 4))  # 7
#print(solution([2, 3], [1, 2], [1, 1], 4))  # 7
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


print(solution([10, 10], [4, 4], [3, 3], 5000))  # 739323?
# print(solution([1250, 1250], [150, 150], [185, 100], 500))  # 9
