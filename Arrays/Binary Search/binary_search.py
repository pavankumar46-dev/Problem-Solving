# time complexity of binary search (sorted array) O(log n)
def binary_search(nums, target):
    start_index = 0
    end_index = len(nums)-1
    mid_index = (start_index+end_index) // 2
    
    while start_index <= end_index:
        if nums[mid_index] == target:
            return True
        else:
            if nums[mid_index] > target:
                end_index = mid_index-1
                
            else:
                start_index = mid_index+1
                
        mid_index = (start_index+end_index) // 2
        print(start_index, mid_index, end_index)
            
    return False
                
                
lst = [4, 8, 15, 22, 27, 33]
result = binary_search(lst, 3)
print(result)
