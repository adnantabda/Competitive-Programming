def contain_duplicates(nums, k):
    for i in range(0, len(nums)- 1):
        for j in range(1, len(nums)):
            print(i, j)
            if nums[i] == nums[j] and abs(i - j) <= k:
                return True

    return False


nums = [1,2,3,1,2,3]
k = 2
print(contain_duplicates(nums, k))