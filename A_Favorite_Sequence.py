def reset(arr):
    left = 0
    right = len(arr) - 1
    result = []
    while left < right:
        result.append(arr[left])
        result.append(arr[right])
        left += 1
        right -=1
        
    if len(arr) % 2 != 0:
        result.append(arr[left])
        
    return result 
    
    

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(*reset(arr))