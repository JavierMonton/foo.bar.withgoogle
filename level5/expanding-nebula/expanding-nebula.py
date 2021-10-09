import itertools


# this solution doesn't pass all the test due to performance issues. This is just my first approach
def solution(g):
    rows = len(g)
    cols = len(g[0])
    final_rows = generate_possible_rows(rows)
    for i in range(1, cols + 1):
        possible_rows = generate_possible_rows(rows)
        final_rows = merge_rows(final_rows, possible_rows, column(g, i - 1))

    return len(final_rows)


def column(matrix, i):
    return [row[i] for row in matrix]


def generate_possible_rows(columns):
    return list(itertools.product([True, False], repeat=columns + 1))


def merge_rows(main_rows, new_rows, expected):
    """Given a 2 list of possible rows and the expected evolution, returns the valid rows that meet that criteria"""
    final = []
    for a in main_rows:
        for b in new_rows:
            # check valid or not row
            if valid_combination(a, b, expected) is True:
                final.append(b)
    return final


def valid_combination(row1, row2, expected):
    """Given 2 rows and a expected evolution, returns True or False if the given rows meet the expected"""
    result = []
    for i in range(0, len(row1) - 1):
        cell = [[row1[i], row1[i + 1]], [row2[i], row2[i + 1]]]
        result.append(get_evolution(cell))
    if result == expected:
        return True
    else:
        return False


def get_evolution(cell):
    """Given a cell (2x2), returns True or False following the evolution of the gases"""
    total = 0
    if cell[0][0] is True:
        total += 1
    if cell[0][1] is True:
        total += 1
    if cell[1][0] is True:
        total += 1
    if cell[1][1] is True:
        total += 1
    if total == 1:
        return True
    else:
        return False


print(solution([[True, False],
                [True, True]]))  #10

print(solution([[True, False, True],
                [False, True, False],
                [True, False, True]]))  # 4

print(solution([[True, False, True, False, False, True, True, True],
                [True, False, True, False, False, False, True, False],
                [True, True, True, False, False, False, True, False],
                [True, False, True, False, False, False, True, False],
                [True, False, True, False, False, True, True, True]]))  # 254

print(solution([[True, True, False, True, False, True, False, True, True, False],
                [True, True, False, False, False, False, True, True, True, False],
                [True, True, False, False, False, False, False, False, False, True],
                [False, True, False, False, False, False, True, True, False, False]]))  # 11567
