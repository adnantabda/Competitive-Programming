def wiggleSort(nums):
    for i in range(len(nums)-1):
        if i % 2 == 0:
            if nums[i] < nums[i + 1]:
                nums[i] , nums[i + 1] = nums[i + 1] , nums[i]
        else:
            if nums[i] > nums[i + 1]:
                nums[i], nums[ i + 1] = nums[i + 1], nums[i]
        
    return arr


arr = [1,10,100,1000]
print(wiggleSort(arr))
                 
