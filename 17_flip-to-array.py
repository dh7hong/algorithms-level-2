def solution(n):
    answer = []
    for i in reversed(str(n)):
        answer.append(int(i))
    
    return answer

print(solution(21345)) # [5, 4, 3, 2, 1]
print(solution(123124214))