def minimum_operations( nums ):
    operation = 0
    for i in nums:
        if i % 3 != 0:
            j = 1
            while j < 10:
                if (i + j) % 3 == 0:
                    operation += 1
                    break
                else:
                    j += 1


    return operation

nums=[3,6,9]
print(minimum_operations(nums))

