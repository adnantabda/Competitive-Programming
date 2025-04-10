MOD = 998244353
limitFac = 500000

fact = [1] * (limitFac + 1)
for i in range(1, limitFac + 1):
    fact[i] = fact[i-1] * i % MOD

pFac = [1] * (limitFac + 1)
pFac[limitFac] = pow(fact[limitFac], MOD - 2, MOD)
for i in range(limitFac - 1, -1, -1):
    pFac[i] = pFac[i + 1] * (i + 1) % MOD

def main():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    for _ in range(t):
        c = list(map(int, input[ptr:ptr+26]))
        ptr += 26
        
        N = sum(c)
        if N == 0:
            print(0)
            continue
        
        even_pos = N // 2
        odd_pos = (N + 1) // 2
        
        dirqSum = 0
        for num in c:
            if num > even_pos:
                dirqSum += num
        
        if dirqSum > odd_pos:
            print(0)
            continue
        
        S = []
        for num in c:
            if 0 < num <= even_pos:
                S.append(num)
        
        sum_S = sum(S)
        if sum_S < even_pos:
            print(0)
            continue
        
        target = even_pos
        dp = [0] * (target + 1)
        dp[0] = 1
        for num in S:
            for s in range(target, num - 1, -1):
                dp[s] = (dp[s] + dp[s - num]) % MOD
        
        K = dp[target]
        if K == 0:
            print(0)
            continue
        
        even_fact = fact[even_pos]
        odd_fact = fact[odd_pos]
        
        notAcceptable = 1
        for num in c:
            if num > 0:
                notAcceptable = notAcceptable * pFac[num] % MOD
        
        ans = even_fact * odd_fact % MOD
        ans = ans * notAcceptable % MOD
        ans = ans * K % MOD
        print(ans)

if __name__ == '__main__':
    main()