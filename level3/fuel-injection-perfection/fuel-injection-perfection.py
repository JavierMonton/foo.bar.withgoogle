
def solution(n):
    n = int(n)
    operations = 0
    while n > 1:
        operations += 1
        if n % 2 == 0:
            n = n / 2
        elif n % 4 == 1 or n == 3:
            n -= 1
        else:
            n += 1
    return operations


print(solution("3"))
print(solution("4"))
print(solution("15"))
print(solution("1523452345234523452345234523452145234523452345234623462345234567896789678967898967896784567456745674567458456754845685456545"))