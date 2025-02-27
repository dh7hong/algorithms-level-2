def solution(n):
    array = []
    for i in range(1, n+1):
        if n % i == 1:
            array.append(i)
    array = sorted(array)
    return array[0]

print(solution(10)) # 3
print(solution(12)) # 1

def solution2(n):
    array = []
    for i in range(1, n+1):
        print(f'i: {i}')
        if n % i == 1:
            print(f'n % i == 1 when i: {i}')
            array.append(i)
    print(f'array: {array}')
    return sorted(array)[0]

print(solution2(10)) # 3
print(solution2(12)) # 1