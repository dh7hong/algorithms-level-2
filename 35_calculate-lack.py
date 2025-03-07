def solution(price, money, count):
    
    total_price = 0
    for i in range(1, count+1):
        total_price += price * i
    
    return total_price - money if total_price > money else 0

print(solution(3, 20, 4)) # 10

def solution2(price, money, count):
    answer = -1
    total = 0  # Don't reset count to 0
    for i in range(1, count + 1):  # Start from 1 instead of 0
        total += price * i  # Use price correctly
        answer = total - money
    if answer <= 0:
        return 0
    else:
        return answer

print(solution2(3, 20, 4))  # Expected output: 10
print(solution2(3, 20, 4))  # Expected output: 10