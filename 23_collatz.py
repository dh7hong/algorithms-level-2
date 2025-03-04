def solution(num):
    i = 0
    while num > 1:
        if (num % 2 == 0):
            print(f'num before num / 2 operation is: {num}')
            num = num / 2
            print(f'num after num / 2 operation is: {num}')
            i += 1
            print(f'i is incremented to: {i}')
        else:
            print(f'num before num * 3 + 1 operation is: {num}')
            num = num * 3 + 1
            print(f'num after num * 3 + 1 operation is: {num}')
            i += 1
            print(f'i is incremented to: {i}')
        if i == 500:
            return -1
    return i

print(solution(6)) # 8