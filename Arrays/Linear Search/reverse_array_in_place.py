# Using two pointer technique as start and end index
# time complexity is O(n)
# Not creating new variables, doing inplace replacement
# Slightly slower than slicing
def reverse_array_in_place(nums):
    start_index = 0
    end_index = len(nums)-1
    while start_index < end_index:
        nums[start_index], nums[end_index] = nums[end_index], nums[start_index]
        
        start_index += 1
        end_index -= 1
    return nums

nums = [1, 3, 5, 7, 9, 10, -1, 4]
nums = reverse_array_in_place(nums)
print(nums)
