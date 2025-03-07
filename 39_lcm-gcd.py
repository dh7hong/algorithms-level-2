def gcd(a, b):
    gcd = []
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            gcd.append(i)
    return max(gcd)
    
def lcm(a, b):
    return int(a * b / gcd(a, b))

def solution(n, m):
    answer = [gcd(n, m), lcm(n, m)]
    return answer

print(gcd(12, 18)) # 6
print(lcm(12, 18)) # 36
print(solution(3, 12)) # [3, 12]
print(solution(2, 5)) # [1, 10]
print(solution(5, 10)) # [5, 10]
print(solution(6, 8)) # [2, 24]