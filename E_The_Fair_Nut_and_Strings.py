def solve(n, k, s, t):
    total = 0  # total number of unique prefixes
    ways = 1   # how many new strings we can build at this level

    for i in range(n):
        # At this position i, we can add `ways` prefixes
        total += ways

        # Now update how many strings we can continue with at next level
        if s[i] == t[i]:
            pass  # still same, we just follow s[i]
        else:
            # The new number of strings doubles:
            # Any place after first difference can now choose 'a' or 'b'
            ways = min(2 * ways, k)

        # If we have already written k strings, stop
        if total >= k:
            print(k * (i + 1))  # all next levels would be full
            return

    # After full loop, total < k, just print the prefix count
    print(total)



n , k = map(int, input().split())
s = input()
t = input()

solve(n , k , s , t)