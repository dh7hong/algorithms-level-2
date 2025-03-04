def solution(absolutes, signs):
    for i in range(len(absolutes)):
        if signs[i] == False:
            absolutes[i] = -absolutes[i]
    return sum(absolutes)
    

print(solution([4, 7, 12], [True, False, True])) # 9
print(solution([1, 2, 3], [False, False, True])) # 0
print(solution([1, 2, 3], [True, True, True])) # 6


def solution2(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        if signs[i] == True:
           answer += absolutes[i]
        else:
           answer -= absolutes[i]       
    return answer

print(solution2([4, 7, 12], [True, False, True])) # 9
print(solution2([1, 2, 3], [False, False, True])) # 0
print(solution2([1, 2, 3], [True, True, True])) # 6
