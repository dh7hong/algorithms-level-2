def solution(s):
    return ''.join(sorted(s, reverse=True))
    
print(solution("Zbcdefg")) # gfedcbZ
print(solution("abcde")) # edcba