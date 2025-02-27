def solution(n):
    answer = 0
    for i in range(1, n+1):
        if n % i == 0:
            answer += i
    return answer

def solution2(n):
    answer = 0
    array = []
    for i in range(1, n+1):
        if n % i == 0:
            array.append(i)
    for j in array:
        answer += j
    return answer

print(solution2(12)) # 28