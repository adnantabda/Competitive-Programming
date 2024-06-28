def position(nums, target):
    if target in nums:
        return nums.index(target)
    else:
        for i in nums:
            if i > target:
                return nums.index(i)

    return len(nums)


list_number = [1, 3, 5, 6]
value = 2
print(position(list_number, value))
