import numpy as np
from fractions import Fraction


def solution(m):
    matrix = np.matrix(m)
    if matrix.sum() == 0 or matrix[0].sum() == 0:
        result = []
        for i in range(0, matrix.shape[0]):
            result.append(1)
        result.append(1)
        return result
    not_finals = np.where(matrix.any(axis=1))[0]
    finals = np.where(~matrix.any(axis=1))[0]

    # build new matrix with for not final states following markov absorving chains
    R = []
    Q = []
    for ending in not_finals:
        denominator = matrix[ending].sum(axis=1)  # for Q elements
        denominator = denominator.sum()
        tmp_r = []
        tmp_q = []
        for values in finals:  # build R
            v = matrix.item(ending, values)
            if v != 0:
                v = Fraction(v, denominator)
            tmp_r.append(v)
        R.append(tmp_r)

        for values in not_finals:  # build Q
            v = matrix.item(ending, values)
            if v != 0:
                v = Fraction(v, denominator)
            tmp_q.append(v)
        Q.append(tmp_q)
    R = np.matrix(R)
    Q = np.matrix(Q)
    I = np.identity(Q.shape[0], dtype=Fraction)

    i_q = np.subtract(I, Q)
    test = np.matrix(i_q, dtype='float')

    F = np.matrix(np.linalg.inv(test), dtype=Fraction)
    final = F * R
    elements = []
    for i in range(0, final[0].size):
        elements.append(Fraction(final.item(0, i)).limit_denominator(1000))

    denominator = Fraction(np.gcd.reduce(elements)).denominator
    result = []
    for a in elements:
        if a != 0:
            if a.denominator == denominator:
                result.append(a.numerator)
            else:
                factor = denominator / a.denominator
                result.append(int(a.numerator * factor))
        else:
            result.append(0)

    result.append(denominator)
    return result




print(solution([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]]))
print(solution([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))
print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]))
print(solution([[0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [1, 0, 0, 0, 2], [0, 0, 0, 0, 0]]))
print(solution([[1, 99, 3, 6548, 453], [0, 1504, 1504, 6659865, 6547125], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]))


