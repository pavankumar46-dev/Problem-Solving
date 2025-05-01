def string_slicing(string):
    print(string[::-1])

# In place replacement won't work in string, because strings are immutable
def reverse_string_two_pointer(string):
    start = 0
    end = len(string)-1
    string = list(string)
    while start < end:
        string[start], string[end] = string[end], string[start] 
        start += 1
        end -= 1
        
    print(''.join(string))
    
# String reversal with for loop
def reverse_string(string):
    temp_str = ""
    for i in range(1, len(string)+1):
        temp_str = temp_str+string[-i]
        
    print(temp_str)
            
    
string = "adasnanlanvca"
string_slicing(string)
reverse_string_two_pointer(string)
reverse_string(string)

        
