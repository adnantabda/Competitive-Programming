def swap_number(number):
    number_str = str(number)
    # print(len(number_str))

    for i in range(0 , len(number_str)):
        maximum = max(number_str)
        index_of_maximum = number_str.index(maximum)
        if index_of_maximum == i : 
            return number
        else:
            new_str = maximum + number_str[1:index_of_maximum] + number_str[0] + number_str[index_of_maximum + 1:]
            return int(new_str)



print(swap_number(43234))



# def fib2(n):
#     """
#     :type n: int
#     :rtype: int
#     """
#     if n == 0 :
#         return 0 
#     if n == 1:
#         return 1 
#     else: 
#         return fib2(n - 1 ) + fib2(n - 2)


# if index_of_maximum == 0:
#     return int(number_str)
# else :
#     new_str = maximum + number_str[1:index_of_maximum] + number_str[0] + number_str[index_of_maximum + 1:]
#     return int(new_str)
    
