t = int(input())
for _ in range(t):
    n , k , q = map(int, input().split())
    a = list(map(int, input().split()))

    c = 0
    l = 0
    for i in a:
        if i <= q:
            l += 1
        else:
            if l >= k:
                correct = l - k + 1
                c += correct * ( correct + 1)// 2
            l = 0

    if l >= k :
        correct = l - k + 1
        c += correct * ( correct + 1)// 2
    print(c)
