def scoreOfString(s: str) -> int:
    sum_ = 0
    for i in range(len(s) - 1):
        sum_ += abs(ord(s[i]) - ord(s[i+1]))

    print(sum_) 


scoreOfString("")