t = int(input())
for _ in range(t):
    n, m, l, r = map(int, input().split())

    length = m + 1
    l_prime = max(l, -m // 2)
    r_prime = l_prime + m
    if r_prime > r:
        r_prime = r
        l_prime = r_prime - m

    print(l_prime, r_prime)
