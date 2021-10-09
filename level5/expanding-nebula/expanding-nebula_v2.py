import itertools
from collections import defaultdict

checked_combinations = {}


# final version, it passed all the tests
def solution(g):
    rows = len(g)
    cols = len(g[0])
    final_rows = defaultdict(int)
    tmp = generate_possible_rows(rows, column(g, 0))
    for a in tmp:
        final_rows[a] = 1

    for i in range(0, cols):
        possible_rows = generate_possible_rows(rows, column(g, i))
        final_rows = merge_rows(final_rows, possible_rows, column(g, i))

    return sum(final_rows.values())


def column(matrix, i):
    return [row[i] for row in matrix]


def generate_possible_rows(columns, expected):
    """Generate all possible combinations and remove some of the invalid ones based on Trues"""
    all = list(itertools.product([True, False], repeat=columns + 1))
    final = []
    # reduce the total number by removing impossible ones
    for p in all:
        to_remove = False
        for i in range(0, len(expected)):
            if expected[i] is True and p[i] is True and p[i+1] is True:
                to_remove = True
                break

        if to_remove is False:
            final.append(p)
    return final


def merge_rows(main_rows, new_rows, expected):
    """Given a 2 list of possible rows and the expected evolution, returns the valid rows that meet that criteria
    For performance improvements, the main rows are stored in a dict with the count of how many times they appear
    """
    final = defaultdict(int)
    for a, total in main_rows.items():
        for b in new_rows:
            # check valid or not row
            if valid_combination(a, b, expected) is True:
                final[b] += main_rows[a]
    return final


def valid_combination(row1, row2, expected):
    """Given 2 rows and a expected evolution, returns True or False if the given rows meet the expected"""
    result = []
    global checked_combinations
    if str(row1)+str(row2) in checked_combinations:
        if expected == checked_combinations[str(row1)+str(row2)]:
            return True
        else:
            return False
    else:
        for i in range(0, len(row1) - 1):
            cell = [[row1[i], row1[i + 1]], [row2[i], row2[i + 1]]]
            result.append(get_evolution(cell))
        checked_combinations[str(row1)+str(row2)] = result
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

print(solution([[False, False, False],
                [False, False, False],
                [False, False, False]]))  # 10148

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

print(solution(
[[True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True],
[True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True],
[True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True],
[True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True],
[True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True],
[True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True],
[True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True],
[True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True],
[True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]]))
#  100663356