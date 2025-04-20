t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    count0 = a.count(0)
    count1 = a.count(1)

    if count0 <= (n + 1) // 2:
        print(0)
    else:
        if count1 == 0 or (count0 + count1) != n:
            print(1)
        else:
            print(2)