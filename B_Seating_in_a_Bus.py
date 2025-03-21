def seat(a):
    taken = {a[0]}
    for i in range(1, len(a)):
        if a[i] - 1 in taken or a[i] + 1 in taken:
            taken.add(a[i])
        else:
            return "NO"
    
    return "YES"

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(seat(a))
