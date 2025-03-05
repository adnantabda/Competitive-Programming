t = int(input())

def seat(a):
    if len(a) == 1:
        print("YES")
    hash_ = set()
    hash_.add(a[0])
    correct = True
    for i in range(1,len(a)):
        left = a[i] - 1
        right = a[i] + 1
        found = False
        if left in hash_ and right in hash_:
            found = True
        if not found:
            correct = False
            break
        hash_.add(a[i])

    print("YES" if correct else "NO")


def seat2(a):
    hash_ = set()
    hash_.add(a[0])
    correct = True
    for i in range(1, n):
        if (a[i] - 1) not in hash_ and (a[i] + 1 ) not in hash_:
            correct = False
        hash_.add(a[i])
    print("YES" if correct else "NO")


for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    seat2(a)

