length = int(input())
arr = input().split(" ")
arr = [int(num) for num in arr]
arr.sort()

if arr[length - 3] + arr[length - 2] <= arr[length - 1]:
    print("NO")
else:
    print("YES")
    print(arr[length - 1], end=" ")
    for i in range(length -  3, -1, -1):
        print(arr[i], end=" ")
    print(arr[length - 2])

