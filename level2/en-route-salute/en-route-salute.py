
def solution(s):
    salute = 0
    total = 0
    for c in s:
        if c == '>':
            salute += 1
        if c == '<':
            total = total + salute * 2
    return total

print(solution("<<>><"))
