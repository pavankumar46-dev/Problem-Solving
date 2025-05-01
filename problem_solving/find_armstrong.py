import math

def find_armstrong(val):
    final_sum = 0
    for i in str(val):
        final_sum = final_sum+(round(math.pow(int(i), 3)))
        
    if final_sum == val:
        print(f"Given number {val} is armstrong number")
        
    else:
        print(f"Given number {val} is not an amstrong number")
        
        
find_armstrong(153)
        
