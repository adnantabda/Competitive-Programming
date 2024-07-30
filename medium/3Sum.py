# Function Definition 

# [12,3,1,2,-6,5,-8,6]
# sorted [-8,-6,1,2,3,5,6,12]
def threeSum(nums):
    nums.sort()
    result = []

    for i , current in enumerate(nums):
        if i > 0 and current == nums[i - 1]:
            continue

        left = i + 1
        right = len(nums) - 1
        while left < right:
            sum_ = current + nums[left] + nums[right]
            if sum_ == 0:
                result.append([current,nums[left], nums[right]])
                left +=1
                while nums[left] == nums[left - 1] and left < right: 
                    left +=1
                    
            elif sum_ < 0:
                left +=1
            else:
                right -=1


    return result


# time limit exceeded



# Driver code 
nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))