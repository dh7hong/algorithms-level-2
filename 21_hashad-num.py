def solution(x):
    myStr = list(str(x)) # 10 -> ['1', '0']
    myNum = x   # x = 10
    myNum2 = 0  # 0
    for i in range(len(myStr)): # 0, 1
        myNum2 += int(myStr[i]) # +1, +0
    return myNum % myNum2 == 0 # 10 % 1 == 0

print(solution(10)) # True
print(solution(12)) # True
print(solution(11)) # False
print(solution(13)) # False