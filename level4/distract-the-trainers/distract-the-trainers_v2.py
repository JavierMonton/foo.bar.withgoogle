# make a list of all possible combinations and check one by one
def solution(banana_list):

    checked_primes = {}

    results = []
    plus1 = 0
    if len(banana_list) % 2 == 1:
        plus1 = 1

    for row in all_pairs(banana_list):
        bunnies = 0
        for pair in row:
            key = str(pair[0])+"-"+str(pair[1])
            if key in checked_primes:
                test_prime = checked_primes[key]
            else:
                test_prime = is_prime(pair[0] + pair[1] - 1)
                checked_primes[key] = True

            if test_prime is True or pair[0] == pair[1]:
                bunnies = bunnies + 2
        if bunnies == 0:  # halt quickly
            return 0 + plus1
        results.append(bunnies)

    return min(results) + plus1


def all_pairs(lst):
    if len(lst) < 2:
        yield []
        return
    if len(lst) % 2 == 1:
        # Handle odd length list
        for i in range(len(lst)):
            for result in all_pairs(lst[:i] + lst[i+1:]):
                yield result
    else:
        a = lst[0]
        for i in range(1,len(lst)):
            pair = (a,lst[i])
            for rest in all_pairs(lst[1:i]+lst[i+1:]):
                yield [pair] + rest

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
print(solution([1, 21, 1, 21, 1, 1, 1, 1, 21, 1, 21, 1, 1, 1, 1, 21, 1, 21, 1, 1, 1, 1, 21, 1, 21, 1, 1, 1, 1, 21, 1, 21, 1, 1, 1, 1, 21, 1, 21, 1, 1, 1, 1, 21, 1, 21, 1, 1, 1])) # 3
