def GoodPairs(array):
    pair = 0
    for i in range(0 , len(array) - 1):
        for j in range(i + 1 , len(array)):
            if array[i] == array[j]:
                pair = pair + 1
    
    return pair

print(GoodPairs([1,2,3]))
