def single_number(arr):
    for i in range(0, len(arr)):
        if arr.count(i) == 1:
            return i


arr = [2,1,5,5,2,2]
print(single_number(arr))
