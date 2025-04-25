def find_first_duplicate(nums, target):
    low = 0
    high = len(nums) - 1
    
    while low <= high:
        mid = (low + high) // 2
        # If mid is a duplicate, check if it's the first occurrence
        if nums[mid] == target:
            index = mid
            for i in range(mid, low-1, -1):
                if nums[i] == target:
                    index = i
            return index
        
        # Move the search range to the left half
        else:
            if nums[mid] > target:
                high = mid-1
                
            else:
                low = mid+1
                
    # If no duplicates are found
    return None


nums=[1, 1, 1, 6, 6, 11, 11, 16, 16, 16, 16, 16]
val = find_first_duplicate(nums, 16)
print(val)
