n = int(input())
a = list(map(int, input().split()))
asorted = sorted(a)
zsorted = [0] * n
left = 0
right = n - 1
for i in range(n):
    if i % 2 == 0:
        zsorted[i] = asorted[left]
        left += 1
    else:
        zsorted[i] = asorted[right]
        right -= 1
        
canbe = True
for i in range(1, n):
    if i % 2 == 0:
        if zsorted[i] > zsorted[i-1]:
            canbe = False
            break
    else:
        if zsorted[i] < zsorted[i-1]:
            canbe = False
            break
if canbe:
    print(*zsorted)
else:
    print("Impossible")