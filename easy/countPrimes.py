def countPrime(n):
    if n <=2 : 
        return 0 
    
    is_prime = [True]
    num = num / 2 

    for i in range(3 , n , 2 ):
        if i * i >= n :
            break

        if not is_prime[i]:
            continue

        for j in range(i * i , n , 2 * i ):
            if not is_prime[j]:
                continue

            num -= 1
            is_prime[j] = False

    return int(num)