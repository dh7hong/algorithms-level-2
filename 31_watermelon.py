def solution(n):
    # if n = 5
    # floor divsion: 5//2 = floor(2.5) = 2
    # ceiling divsion: 5//2 + 1 = floor(2.5) + 1 = 3
    # 5//2 = 2
    # 5%2 = 1
    # "수박" * 2 + "수" * 1
    return "수박"*(n//2) + "수"*(n%2)

print(solution(3)) # 수박수
print(solution(4)) # 수박수박
print(solution(5)) # 수박수박수

def solution2(n):
    answer = '수박'
    if n % 2 == 0:
        return answer * int(n/2)
    else:
        return answer * int(n/2) + '수'

print(solution2(3)) # 수박수
print(solution2(4)) # 수박수박
print(solution2(5)) # 수박수박수
