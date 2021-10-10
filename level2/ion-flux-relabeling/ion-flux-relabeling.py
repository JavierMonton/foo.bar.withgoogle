import math


def solution(h, q):
    n = int(math.pow(2, h) - 1)
    main = Node(n, -1)
    main.min_value = n
    tree = create_tree(main, 1, h-1)
    result = []
    for find in q:
        result.append(find_parent(tree, find))

    return result


class Node:
    def __init__(self, value, parent):
        self.left = None
        self.right = None
        self.value = value
        self.min_value = value
        self.parent = parent


def create_tree(leaf, high, max_high):
    if leaf.value == 1:
        return leaf
    else:
        # final leaf nodes
        if high == max_high:
            # print(str(leaf.value-1) + " - " + str(leaf.value))
            leaf.right = Node(leaf.value-1, leaf.value)
            leaf.left = Node(leaf.value-2, leaf.value)
            # print(str(leaf.value - 2) + " - " + str(leaf.value))
            # update min value as this is going to jump to the next branch
            leaf.min_value = leaf.value-2
            return leaf

        if leaf.right is None:
            leaf.right = Node(leaf.value-1, leaf.value)
            # print(str(leaf.value - 1) + " - " + str(leaf.value))
            create_tree(leaf.right, high+1, max_high)
            leaf.min_value = leaf.right.min_value

        if leaf.left is None:
            leaf.left = Node(leaf.min_value - 1, leaf.value)
            # print(str(leaf.min_value - 1) + " - " + str(leaf.value))
            create_tree(leaf.left, high + 1, max_high)
            leaf.min_value = leaf.left.min_value

        return leaf


def find_parent(leaf, value, result=None):
    if value == leaf.value:
        result = leaf.parent
        return result
    if leaf.right is not None:
        result = find_parent(leaf.right, value)
        if result is None and leaf.left is not None:
            result = find_parent(leaf.left, value)
        else:
            return result
    return result


print(solution(3, [7, 3, 5, 1]))  # [-1, 7, 6, 3]

print(solution(5, [19, 14, 28]))  # [21, 15, 29]
