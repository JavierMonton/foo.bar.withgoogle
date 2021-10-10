class Step:
    def __init__(self, x=None, y=None, steps=0, barrier=False):
        self.x = x
        self.y = y
        self.barrier = barrier
        self.steps = steps


def solution(map):
    num_rows = len(map)
    num_cols = len(map[0])
    # cube with all possible locations, using barrier passed or not as dimension
    # cube with [x][y][barriers]
    cube = [[[Step(i, j) for k in range(2)] for j in range(num_cols)] for i in range(num_rows)]

    max_x = num_rows - 1
    max_y = num_cols - 1

    paths = []

    # init
    paths.append(Step(0, 0, 1))

    for minion in paths:

        if minion.x == max_x and minion.y == max_y:
            return minion.steps

        if minion.x != max_x:
            make_move(map, minion.x + 1, minion.y, minion, paths, cube)

        if minion.x > 0:
            make_move(map, minion.x - 1, minion.y, minion, paths, cube)

        if minion.y != max_y:
            make_move(map, minion.x, minion.y + 1, minion, paths, cube)

        if minion.y > 0:
            make_move(map, minion.x, minion.y - 1, minion, paths, cube)


def make_move(map, x, y, minion, paths, cube):
    is_barrier = map[x][y] == 1
    b = int(minion.barrier)

    if cube[x][y][b].steps == 0 or cube[x][y][b].steps > minion.steps+1: # skip if we have passed over here with more steps
        if minion.barrier is False or is_barrier is False:  # no barrier passed o no barrier in destination
            new_step = Step(x, y, minion.steps + 1, minion.barrier)
            if is_barrier is True and minion.barrier is False:  # first barrier passed, set to true + append
                new_step.barrier = True
                paths.append(new_step)
                cube[x][y][1] = new_step
            elif is_barrier is False:  # not barrier, append
                paths.append(new_step)
                cube[x][y][int(new_step.barrier)] = new_step

            # else: barrier + passed barrier = not append


print(solution(
[
    [0, 1, 1, 0, 0, 0],
    [1, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 0],
    [0, 1, 0, 1, 1, 0],
    [0, 0, 0, 1, 1, 0]]))  # should be 16

print(solution(
[[0, 1, 1, 0],
 [0, 0, 0, 1],
 [1, 1, 0, 0],
 [1, 1, 1, 0]]))

print(solution(
[
    [0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0]]))


print(solution(
    [[0],
     [0],
     [0]]
))

print(solution(
    [[0, 0, 0]]
))
print(solution(
    [[0, 0],
     [0, 0]]
))


print(solution(
[
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0],
    [0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0]]))



