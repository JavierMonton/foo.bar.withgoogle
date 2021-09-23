# checking pairs in order, shuffle and repeat, statistically we should find the result
import random

def solution(banana_list):
    plus1 = 0
    if len(banana_list) % 2 == 1:
        plus1 = 1

    results = []
    for i in range(0, 100):
        random.shuffle(banana_list)
        bunnies = count_bunnies(banana_list)
        if bunnies == 0:
            return 0 + plus1
        results.append(bunnies)

    return min(results) + plus1


def count_bunnies(banana_list):
    bunnies = 0
    for i in range(0, len(banana_list), 2):
        if i + 1 < len(banana_list):
            current = banana_list[i]
            next = banana_list[i + 1]
            if is_prime(current + next - 1) is True or current == next:  # not infinite loop pair
                ##### probando pareja y saltando a la siguiente no va, debería ir probando números hasta encontrar uno válido
                bunnies = bunnies + 2
    return bunnies


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

print(solution([5])) # 2
print(solution([1, 1])) # 2
print(solution([1, 7, 3, 21, 13, 19])) # 0
print(solution([1, 7, 3, 21, 13, 19, 1])) # 1
print(solution([1, 1, 1, 1, 1, 1])) # 6
print(solution([1, 21, 1, 21, 1, 1])) # 2
print(solution([1, 21, 1, 21, 1, 1, 1])) # 3
print(solution([1, 21, 1, 21, 1, 1, 1, 1, 21, 1, 21, 1, 1, 1, 1, 21, 1, 21, 1, 1, 1, 1, 21, 1, 21, 1, 1, 1, 1, 21, 1, 21, 1, 1, 1, 1, 21, 1, 21, 1, 1, 1, 1, 21, 1, 21, 1, 1, 1, 1, 21, 1, 21, 1, 1, 1, 1, 21, 1, 21, 1, 1, 1, 1, 21, 1, 21, 1, 1, 1])) #30?
