def valid_subsequent(arr1, arr2):
    ptr = 0
    for i in range(len(arr2)):
        if arr2[i] == arr1[ptr]:
            ptr +=1

        if ptr == len(arr1):
            return True
    
    return False

arr1 = [5,1,22,25,6,-1,8]
arr2 = [5,1,22,25,6,-1,8,10]
print(valid_subsequent(arr1, arr2))