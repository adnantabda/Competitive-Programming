t = int(input())

letters  = []
for i in range(t):
    letter = input()
    if letter in 'codeforces':
        letters.append("YES")
    else:
        letters.append("NO")

for j in letters:
    print(j)
    
