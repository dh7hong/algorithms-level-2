def solution(arr1, arr2):
    answer = []  # Initialize an empty list

    for i in range(len(arr1)):  # Loop over each row
        row = [0] * len(arr1[0])  # Create a row of zeros
        answer.append(row)  # Add the row to the answer

    print(answer)
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            print(i, j, arr1[i][j], arr2[i][j])
            answer[i][j] = arr1[i][j] + arr2[i][j]
    
    return answer

print(solution([[1, 2], [2, 3]], [[3, 4], [5, 6]])) # [[4, 6], [7, 9]]

def solution2(arr1, arr2):
    answer = []  # Initialize an empty list

    for i in range(len(arr1)):  # Loop over each row
        row = []  # Create an empty row
        for j in range(len(arr1[i])):  # Loop over columns
            row.append(arr1[i][j] + arr2[i][j])  # Sum elements and append
        answer.append(row)  # Append the computed row to answer

    return answer

# Test case
print(solution2([[1, 2], [2, 3]], [[3, 4], [5, 6]]))  # Expected: [[4, 6], [7, 9]]
