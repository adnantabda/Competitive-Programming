def incre(a):
    first = a[0]
    second = a[1]
    for i in range(2, len(a)):
        if i % 2 == 0:
            if a[i] % 2 != first % 2:
                return "NO"
        else:
            if a[i] % 2 != second % 2:
                return "NO"
            
    return "YES"


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(incre(a))
