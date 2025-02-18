t = int(input())
total = 0
for i in range(t):
    stat = input()
    if "+" in stat:
        total += 1
    elif "-" in stat:
        total -= 1


print(total)