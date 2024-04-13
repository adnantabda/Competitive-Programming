def insertion_sort(arr):

    for i in range(len(arr)):
        j = i 
        while arr[j-1] > arr[j] and j > 0 : 
            arr[j - 1] , arr[j] = arr[j], arr[j - 1]
            j-=1

    return arr


print(insertion_sort([1,4,5,6,8,10,14,3,2 ]))