# checking all valid pair + finding numbers outside of those pairs
def solution(banana_list):

    pairs = []
    remaining_list = list(banana_list)
    checked = []

    for _ in banana_list:
        n = remaining_list.pop(0)
        if n in checked:
            print("break")
        else:
            checked.append(n)
            for current in remaining_list:
                if is_prime(n + current - 1) is False and n != current:  # if they are in "infinite loop"
                    pairs.append((n, current))

    bunnies = []
    #print(pairs)
    found = False
    for missing in banana_list:

        for pair in pairs:
            if missing == pair[0] or missing == pair[1]:
                found = True
            if found is False:  # if it is not present in any infinite pair
                bunnies.append(missing)

    if len(pairs) == 0:
        return len(banana_list)
    else:
        if len(banana_list) % 2 == 1:
            return len(bunnies) + 1
        else:
            return len(bunnies)


def is_prime(n):
    """AKS - Returns True if n is prime."""
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True


print(solution([1, 1])) # 2
print(solution([1, 7, 3, 21, 13, 19])) # 0
print(solution([1, 7, 3, 21, 13, 19, 1])) # 1
print(solution([1, 1, 1, 1, 1, 1])) # 6
print(solution([1, 21, 1, 21, 1, 1])) # 2
print(solution([1, 21, 1, 21, 1, 1, 1])) # 3
