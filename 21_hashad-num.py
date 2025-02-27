mynum = 10
mystr = list('10')
mynum2 = 0
for i in range(len(mystr)):
    mynum2 += int(mystr[i])
print(mynum%mynum2)    
print(mystr)

def solution(x):
    myStr = list(str(x))
    myNum = x
    myNum2 = 0
    for i in range(len(myStr)):
        myNum2 += int(myStr[i])
    return myNum % myNum2 == 0

print(solution(10)) # True
print(solution(12)) # True
print(solution(11)) # False
print(solution(13)) # False