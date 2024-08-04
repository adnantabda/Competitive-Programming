def squared_sorted_arr(nums):
    left = 0
    right = len(nums) - 1
    squared_ = [0] * len(nums)
    i = len(nums) - 1
    while left <= right:
        if abs(nums[left]) > abs(nums[right]):
            squared_[i] = nums[left] ** 2
            left +=1

        elif abs(nums[left]) < abs(nums[right]):
             squared_[i] = nums[right] ** 2
             right -=1
    
        else:
            squared_[i] = nums[right] ** 2
            right -=1
        
        i -=1

    return squared_

nums = [-7,-2,-1,0,3,4,6,7]
print(squared_sorted_numsay(nums)) 