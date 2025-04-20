t = int(input())
for _ in range(t):
    words = input()
    wl = words.split()
    result = []
    for w in wl:
        result.append(w[0])

    print(''.join(result))

