def solution(s):
    num_set = {1,2,3,4,5,6,7,8,9,0}
    temp = set([i for i in s])
    print(temp)
    if temp <= num_set:
        return True
    else:
        return False
    
print(solution("1234")) # True
print(solution("1234a")) # False
    