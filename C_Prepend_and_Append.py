def lastString(s):
    left = 0
    right = len(s) - 1
    while left < right :
        if s[left] == "0" and s[right] == "1":
            left += 1
            right -= 1
        elif s[left] == "1" and s[right] == "0":
            left += 1
            right -= 1    
        else:
            return right - left + 1


    return right - left + 1

t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    print(lastString(s))