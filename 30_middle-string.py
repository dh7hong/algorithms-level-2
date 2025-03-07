def solution(s):
    if len(s) % 2 == 0:
        # for qwer 
        # length is 4, 
        # int(4/2) - 1 = 1 (second position),
        # int(4/2) + 1 = 3 (fourth position)
        # s[1:3] = we
        return s[int(len(s)/2)-1:int(len(s)/2)+1]
    else:
        # for adcde
        # length is 5,
        # int(5/2) = 2 (third position)
        # s[2] = c
        return s[len(s)//2]
    
# Code test
print(solution("abcde")) # c
print(solution("qwer")) # we

def solution2(s):
    char_list = list(s)  # Convert string to a list
    print(f'initial char_list: {char_list}')
    
    while len(char_list) > 2:  # Continue until only 1 or 2 elements are left
        print(f'==========================================')
        print(f'Before removing digits: {char_list}')
        char_list.pop(0)  # Remove first element
        print(f'After removing first: {char_list}')
        char_list.pop(-1)  # Remove last element
        print(f'After removing last: {char_list}')
    
    return ''.join(char_list)  # Convert back to string

# Test case
print(solution2("abcde"))  # Output: 'c'

print(solution2("abcde")) # c
print(solution2("qwer")) # we

def solution3(s):
    char_list = list(s)  # Convert string to a list
    print(f'char_list: {char_list}')
    
    while len(char_list) > 2:  # Continue until only 1 or 2 elements are left
        print(f'Before removing: {char_list}')
 
        char_list.remove(char_list[0])  # Remove first occurrence of the first character
        print(f'After removing first: {char_list}')
        
        char_list.remove(char_list[-1])  # Remove first occurrence of the last character
        print(f'After removing last: {char_list}')
    
    print(f'char_list after processing: {char_list}')
    
    return ''.join(char_list)  # Convert back to string

# Test case
print(solution3("abcde"))  # Output: 'c'
print(solution3("qwer")) # we