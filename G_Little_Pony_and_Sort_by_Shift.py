n = int(input())
a = list(map(int, input().split()))

rot = -1
for i in range(n - 1):
    if a[i] > a[i + 1]:
        if rot != -1:
            print(-1)
            exit()
        rot = i

if rot == -1:
    print(0)
elif a[-1] <= a[0]:
    print(n - rot - 1)
else:
    print(-1)
