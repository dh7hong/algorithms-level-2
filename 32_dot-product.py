def solution(a, b):
    answer = []
    for i in range(len(a)):
        answer.append(a[i] * b[i])
    return sum(answer)

# Code test
print(solution([1, 2, 3, 4], [-3, -1, 0, 2])) # 3
print(solution([-1, 0, 1], [1, 0, -1])) # -2