n = int(input())
a = list(map(int, input().split()))
o = sum(1 for x in a if x % 2 != 0)
e = sum(1 for x in a if x % 2 == 0)
if o > 0 and e > 0:
    a.sort()
print(*a)    