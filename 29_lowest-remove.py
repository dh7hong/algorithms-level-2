def solution(arr):
    # If the array has only one element, return [-1]
    if len(arr) == 1:
        return [-1]
    
    # Find the minimum value in the array
    min_value = min(arr)
    
    # Create a new list excluding the minimum value
    arr.remove(min_value)
    
    return arr

print(solution([4, 3, 2, 1])) # [4, 3, 2]
print(solution([10])) # [-1]
print(solution([1, 2, 3, 4])) # [4, 3, 2]
print(solution([1, 2, 3, 4, 5])) # [5, 4, 3, 2]

