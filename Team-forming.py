length = int(input())
arr = input()
arr =  arr.split(" ")
arr = [int(num) for num in arr ]
arr.sort()
i = 1
difference = 0
while i < length:
    difference += abs(arr[i - 1 ] - arr[i])
    i += 2
    
print(difference)