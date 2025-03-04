def solution(numbers):
    num_set = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
    missing = list(num_set - set(numbers))
    
    return sum(missing)

print(solution([1, 2, 3, 4, 6, 7, 8, 0]))

def solution2(numbers):
    y = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
    for i in range(len(numbers)):
        print(f'i: {i}')
        if numbers[i] in y:
            print(f'numbers[{i}]: {numbers[i]}')
            print(f'before removal, y: {y}')
            y.remove(numbers[i])
            print(f'after removal, y: {y}')
    return sum(y)

print(solution2([1, 2, 3, 4, 6, 7, 8, 0]))
