def solution(x, n):
    answer = []
    for i in range(1, n+1):
        answer.append(x * i)        
    return answer

print(solution(2, 5)) # [2, 4, 6, 8, 10]