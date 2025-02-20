def soln(s):
    left = 0
    ans = []
    right = 1
    # for right in range(1,len(s)):
    #     if s[left] == s[right]:
    #         ans.append(s[left])
    #         left = right + 1

    while right < len(s):
        if s[left] == s[right]:
            ans.append(s[left])
            left = right + 1
            right += 1
        right +=1 

    print(''.join(ans))



t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    soln(s)