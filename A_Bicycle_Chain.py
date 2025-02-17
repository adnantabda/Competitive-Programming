n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

hugeRation = 0
count = 0

for ai in a:
    for bj in b:
        if bj % ai == 0:
            ratio = bj // ai
            if ratio > hugeRation:
                hugeRation = ratio
                count = 1
            elif ratio == hugeRation:
                count += 1

print(count)