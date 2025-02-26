n = int(input())
apples = list(map(int, input().split()))

c100 = apples.count(100)
c200 = apples.count(200)
total = sum(apples)

if total % 200 != 0 and total % 100 != 0:
    print("NO")
elif total % 2 != 0:
    print("NO")
else:
    half = total // 2

    for i in range(0, min(c200, half // 200) + 1):
        remaining = half - i * 200
        if remaining <= c100 * 100 and remaining % 100 == 0:
            print("YES")
            break
    else:
        print("NO")
