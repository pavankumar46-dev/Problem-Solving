def left_angle_num_pattern(num):
    for i in range(1, num+1):
        for j in range(1, i):
            print(j, end=" ")
        print()
            
            
print_num_pattern(5)

# Sample Output
'''
1 
1 2 
1 2 3 
1 2 3 4
'''
