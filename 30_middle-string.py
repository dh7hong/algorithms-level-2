def solution(s):
    if len(s) % 2 == 0:
        return s[int(len(s)/2)-1:int(len(s)/2)+1]
    else:
        return s[len(s)//2]
    
# Code test
print(solution("abcde")) # c
print(solution("qwer")) # we