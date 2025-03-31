MOD = int(1e9 + 7)

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort()

    i = n - 1
    ans = 1

    for p in range(n - 1, -1, -1):
        while i >= 0 and a[i] > b[p]:
            i -= 1
        d = p - i
        if d <= 0:
            ans = 0
            break
        ans = (ans * d) % MOD

    print(ans)