from itertools import groupby


def solution(input: str):
    # 100 because maximum is 200
    for n in range(1, 101):
        # try from smaller to greater chunks, as it is rounded, we don't need to shift and try different starting points
        chunks = [input[i:i + n] for i in range(0, len(input), n)]
        result = all_equal(chunks)
        if result and len(chunks) > 1:
            print(len(chunks))
            return len(chunks)

    # not possible chunks found
    return 1


def all_equal(iterable):
    g = groupby(iterable)
    return next(g, True) and not next(g, False)


# solution("abccbaabccba")