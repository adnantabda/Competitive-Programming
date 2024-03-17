arr = [1, 4,3,5,6,8,10,7,2,9]


def cyclicSort(arr):
    i = 0
    while i < len(arr):
        correct_position = arr[i] - 1
        if arr[i] != i +1 :
    
            arr[i], arr[correct_position] = arr[correct_position] , arr[i]
        else: 
            i+=1
    return arr


print(cyclicSort(arr))
