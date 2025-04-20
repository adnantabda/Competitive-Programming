n, k = map(int, input().split())
a = input().strip()
b = input().strip()

ans = 0
cur = 0
while cur < n and a[cur] == b[cur]:
    cur += 1
    ans += 1

sum_ = -1
for i in range(cur, n):
    sum_ = sum_ * 2 + ord('b') - ord(a[i]) + ord(b[i]) - ord('a')
    if sum_ + 2 >= k:
        ans += (n - i) * k
        break
    else:
        ans += sum_ + 2

print(ans)