def evenarray(array):
    even = 0
    odd = 0

    for i in range(len(array)):
        if array[i] % 2 != i % 2:
            if i % 2 == 0:
                even += 1
            else:
                odd += 1

    if even != odd:
        return -1
    return even

t = int(input())
for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    print(evenarray(array))
