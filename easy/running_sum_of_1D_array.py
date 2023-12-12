array = [1,2,3,4]
array2 = [1,1,1,1,1]

def runningSum(array):
    sum = 0 
    new_array = []
    for i in range(0 , len(array)):
        sum = sum + array[i]
        new_array.append(sum)

    return new_array

print(runningSum(array2))