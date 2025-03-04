def solve():
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort()
    ans = 0
    for i in range(n // 2):
        ans += a[-i-1] - a[i]
    print(ans)
    
    
t = int(input())
for _ in range(t):
    solve()