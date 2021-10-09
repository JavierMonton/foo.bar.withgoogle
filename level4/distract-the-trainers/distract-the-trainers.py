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
            if check_infinite(current, pair):  # infinite pair, we break this loop
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
    n = current + pair
    while n % 2 == 0:
        n = n / 2
    return (current % n) != 0


print(solution([1, 1]))  # 2
print(solution([1, 7, 3, 21, 13, 19]))  # 0