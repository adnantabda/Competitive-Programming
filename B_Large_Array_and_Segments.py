import sys

def main():
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    for _ in range(t):
        n, k, x = map(int, input[ptr:ptr+3])
        ptr +=3
        a = list(map(int, input[ptr:ptr+n]))
        ptr +=n
        
        dimir = sum(a)
        
        sPx = [0] * n
        sPx[-1] = a[-1]
        for i in range(n-2, -1, -1):
            sPx[i] = sPx[i+1] + a[i]
        
        sSx = 0
        max_prefix = 0
        for num in a:
            sSx += num
            if sSx > max_prefix:
                max_prefix = sSx
        
        deebisaa = 0
        
        for i in range(n):
            sPx_i = sPx[i]
            if dimir > 0:
                if max_prefix > dimir:
                    required = x - sPx_i - max_prefix
                    if required <= 0:
                        lakk1 = k - 1
                    else:
                        t_val = (required + dimir - 1) // dimir
                        valid_m = (k-2) - t_val + 1
                        if valid_m < 0:
                            valid_m = 0
                        lakk1 = valid_m
                    lakk2 = 1 if sPx_i >= x else 0
                    total = lakk1 + lakk2
                else:
                    required = x - sPx_i
                    if required <= 0:
                        total = k
                    else:
                        t_val = (required + dimir - 1) // dimir
                        total = max(0, k - t_val)
            else:
                idamaSx = sPx_i + max_prefix
                lakk1 = (k-1) if (idamaSx >= x) else 0
                lakk2 = 1 if (sPx_i >= x) else 0
                total = lakk1 + lakk2
            deebisaa += total
        
        print(deebisaa)

if __name__ == "__main__":
    main()