def solution(arr, divisor):
    answer = []
    for i in range(len(arr)):
        if arr[i] % divisor == 0:
            answer.append(arr[i])
    if len(answer) == 0:
        return [-1]
    else:
        return sorted(answer)
    
print(solution([5, 9, 7, 10], 5)) # [5, 10]

def solution2(arr, divisor):
    answer = []
    for i in range(len(arr)):
        if arr[i] % divisor == 0:
            answer.append(arr[i])
    if len(answer) > 0:
        return sorted(answer)
    else:
        return [-1]
    
print(solution2([2, 36, 1, 3], 1)) # [1, 2, 3, 36]