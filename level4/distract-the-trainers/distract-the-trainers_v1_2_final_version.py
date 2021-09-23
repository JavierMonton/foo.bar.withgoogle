# checking pairs in order, put not paired at the beginning and repeat
# shuffle if we are in a loop of ordering
# statistically we should find the result
import random

def solution(banana_list):
    bunnies = []
    # first of all, remove bunnies without bananas
    zeros = banana_list.count(0)
    if zeros > 0:
        banana_list = list(filter(lambda a: a != 0, banana_list))

    new_list = list(banana_list)

    # a little bit crazy, but with 100 elements, 1000 iterations with this formula will probably test all the combinations that we need (better than all possible pairs in order)
    for l in range(0, 1000):
        given_list = list(new_list) # keep given list to compare at the end
        new_list, bunnies = count_bunnies(new_list, bunnies)
        if new_list == given_list:  # if returned list is exactly as given, we could be in a bad infinite loop
            random.shuffle(new_list)

        if bunnies[-1] <= 1:
            return bunnies[-1] + zeros

    return min(bunnies) + zeros


def count_bunnies(bananas, bunnies):
    new_list = [] # new list with unpaired elements at the beginning
    tmp = 0
    found = False
    for i, current in enumerate(bananas):
        for j, pair in enumerate(bananas[i+1:]):
            if check_infinite2(current, pair):  # infinite pair, we break this loop
                # remove valid pair from the list
                new_list.append(current)
                new_list.append(pair)
                bananas.pop(j+i+1)  # we removed the paired, while breaking we will move to the next
                found = True
                break
            # not break, meaning not paired elements, prepending them, to have them at the beginning
        if found is False:
            new_list.insert(0, current)
            tmp = tmp + 1
        found = False
    bunnies.append(tmp)
    return new_list, bunnies


def check_infinite(current, pair):
    if current == pair:
        return False
    if current > pair:
        bigger = current
        lower = pair
    else:
        bigger = pair
        lower = current

    return (is_prime(current + pair - 1) is False) \
           or abs(current - pair) == 1 \
           or (abs(current - pair) == current or abs(current - pair) == pair) \
           or (bigger % lower == 0)


def check_infinite2(current, pair):
    n = current + pair
    while n % 2 == 0:
        n = n / 2
    return (current % n) != 0


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

#print(solution([])) # 0
#print(solution([5])) # 1
#print(solution([1, 1])) # 2
#print(solution([1, 2])) # 2
#print(is_prime(8589935681))
#print(solution([1, 7, 3, 21, 13, 19])) # 0
#print(solution([1, 7, 3, 21, 13, 19, 0])) # 1
#print(solution([1, 7, 3, 21, 13, 19, 7])) # 1
#print(solution([1, 7, 3, 21, 13, 19, 7, 0])) # 2
#print(solution([1, 7, 3, 21, 13, 19, 7, 0, 1])) # 3
#print(solution([1073741823, 1073741823])) # 2
#print(solution([1073741823, 1073741823, 1])) # 1
#print(solution([1073741823, 1073741823, 1, 1])) # 0
#print(solution([1, 1, 0])) # 3
#print(solution([4, 0])) # 2
#print(solution([0, 0, 0])) # 3
print(solution([2, 1])) # 0
print(solution([2, 4])) # 0
print(solution([22, 2, 1])) # 0
print(solution([2, 1, 2, 1])) # 0

#print(solution([1, 2, 2, 2, 1, 1, 1, 2, 1, 2, 2, 2, 1, 1, 1, 2, 1, 2, 2, 2, 1, 1, 1, 2, 1, 2, 2, 2, 1, 1, 1, 2, 1, 2, 2, 2, 1, 1, 1, 2, 1, 2, 2, 2, 1, 1, 1, 2, 1, 2, 2, 2, 1, 1, 1, 2, 1, 2, 2, 2, 1, 1, 1, 2, 1, 2, 2, 2, 1, 1, 1, 2, 1, 2, 2, 2, 1, 1, 1, 2])) # 0
#print(solution([1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1])) # 100
#print(solution([1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1, 1])) # 101
#print(solution([3, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 3, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1])) # 96
#print(solution([3, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 3, 2, 1, 2, 1, 2, 1, 2, 1, 2, 3, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1])) # 94
#print(solution([3, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 3, 2, 1, 2, 1, 2, 1, 2, 1, 2, 3, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 1, 2, 1, 2])) # 93

print(solution([1, 1, 1, 1, 1, 1])) # 6
print(solution([1, 1, 1, 1, 1, 1, 1])) # 7
#print(solution([1, 21, 1, 21, 1, 1])) # 2
print(solution([1, 21, 1, 1, 1, 1, 21])) # 3
#print(solution([1, 21, 1, 21, 1, 1, 1, 1, 21, 1, 21, 1, 1, 1, 1, 21, 1, 21, 1, 1, 1, 1, 21, 1, 21, 1, 1, 1, 1, 21, 1, 21, 1, 1, 1, 1, 21, 1, 21, 1, 1, 1, 1, 21, 1, 21, 1, 1, 1, 1, 21, 1, 21, 1, 1, 1, 1, 21, 1, 21, 1, 1, 1, 1, 21, 1, 21, 1, 1, 1])) #30?
#print(solution([1, 21, 1, 21, 1, 1, 1, 1, 21, 1, 21, 1, 1, 1, 1, 21, 1, 21, 1, 1, 1, 1, 21, 1, 21, 1, 1, 1, 1, 21, 1, 21, 1, 1, 1, 1, 21, 1, 21, 1, 1, 1, 1, 21, 1, 21, 1, 1, 1, 1, 21, 1, 21, 1, 1, 1, 1, 21, 1, 21, 1, 1, 1, 1, 21, 1, 21, 1, 1, 1, 2])) #31?
