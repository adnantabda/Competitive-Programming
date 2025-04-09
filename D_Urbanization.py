n, n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse=True)

little = min(n1, n2)
many = max(n1, n2)

sg = a[:little]
lg = a[little:little + many]

avergS = sum(sg) / little
avergL = sum(lg) / many

ans = avergL + avergS
print("{0:.8f}".format(ans))