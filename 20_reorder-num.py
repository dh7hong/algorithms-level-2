def solution(n):
    return int(''.join(sorted(str(n), reverse = True)))

print(solution(21345)) # [5, 4, 3, 2, 1]