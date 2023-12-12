def Palindrome(x):
    if x < 0 :
        return False
    

    copy , reverse = x , 0

    while copy != 0:
        reverse = reverse*10 + copy % 10
        copy //= 10
    
    return x == reverse



print(Palindrome(121))