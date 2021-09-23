final = 999999
# make a list of all possible combinations checking while creating them
def solution(banana_list):

    results = []
    plus1 = 0
    if len(banana_list) % 2 == 1:
        plus1 = 1

    for row in all_pairs(banana_list):
        if final == 0:
            return 0 + plus1

    return final + plus1


def all_pairs(lst):
    global final
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
        bunnies = 0
        for i in range(1,len(lst)):
            pair = (a,lst[i])

            if is_prime(pair[0] + pair[1] - 1) is False or pair[0] == pair[1]:
                bunnies = bunnies + 2

            print(pair)
            for rest in all_pairs(lst[1:i]+lst[i+1:]):
                yield [pair] + rest

        final = bunnies

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




#print(solution([1, 1])) # 2
#print(solution([1, 7, 3, 21, 13, 19])) # 0
#print(solution([1, 7, 3, 21, 13, 19, 1])) # 1
print(solution([1, 1, 1, 1, 1, 1])) # 6
#print(solution([1, 21, 1, 21, 1, 1])) # 2
#print(solution([1, 21, 1, 21, 1, 1, 1])) # 3
