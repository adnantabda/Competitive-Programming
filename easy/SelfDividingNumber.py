def selfDividingNumbers(left , right):
    result = []
    for i in range(left , right + 1):
        num_str = str(i)
        if '0'  not in num_str:
            length = len(num_str)
            for j in range(length):
                if i % int(num_str[j]) != 0 :
                    break
                elif j == length - 1: 
                    result.append(i)

    return result



print( selfDividingNumbers(1,22))