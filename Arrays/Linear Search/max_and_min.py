# Linear Search to find max and min values from the given list
# time complexity is O(n)

def max_and_min(nums):
    max_val = nums[0]
    min_val = nums[0]
    for val in nums:
        if val > max_val:
            max_val = val
        elif val < min_val:
            min_val = val
            
    return max_val, min_val
    
nums = [1, 3, 5, 7, 9, 10, -1]
max_val, min_val = max_and_min(nums)
print(max_val, min_val)
