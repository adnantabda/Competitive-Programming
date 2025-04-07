# - every castle is a castle is a part of exactly one block 
# - each block is sorted independetly 

def sortBlockAdnan(arr):
    n = len(arr)
    preMax = [0] * n
    sufMax = [0] * n

    preMax[0] = arr[0]
    for i in range(1, n):
        preMax[i] = max(preMax[i - 1], arr[i])

    sufMax[n - 1] = arr[n - 1]
    for i in range(n - 2, -1, -1):
        sufMax[i] = min(sufMax[i + 1], arr[i])

    blocks = 0
    for i in range(n - 1):
        if preMax[i] <= sufMax[i + 1]:
            blocks += 1

    return blocks + 1 
n = int(input())
castles = list(map(int, input().split()))
print(sortBlockAdnan(castles))
