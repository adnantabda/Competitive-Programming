def increasing(nums):
    def is_increasing(nums):
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                return False

        return True

    i = 0
    while i < len(nums) - 2:
        nums2 = [i for i in nums]
        nums2.remove(nums[i])

        if is_increasing(nums2):
            return True
        else:
            i += 1

    return False


nums = [1, 2, 10, 5, 7]
print(is_increasing(nums))