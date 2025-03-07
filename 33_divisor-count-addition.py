def divisor_count(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    return count


def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        if divisor_count(i) % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer

# example test
print(solution(13, 17)) # 43
print(solution(24, 27)) # 52

def solution2(left, right):
    answer = 0
    for i in range(left, right + 1):
        print(f'running the for loop where i = {i}')
        count = 0
        for j in range(1, i + 1):
            print("=========================================")
            print(f'when i = {i}, running the for loop where j = {j}')
            if i % j == 0:
                count += 1
                print(f'if i % j == 0, count += 1, count = {count}')
        if count % 2 == 0:
            print(f'if count % 2 == 0, answer before increment of i: {answer}')
            answer += i
            print(f'answer after increment, answer += {i}: answer = {answer}')
        else:
            print(f'if count % 2 != 0, answer before decrement of i: {answer}')
            answer -= i
            print(f'answer after decrement, answer -= {i}: answer = {answer}')
    return answer

# example test
print(solution2(13, 17)) # 43