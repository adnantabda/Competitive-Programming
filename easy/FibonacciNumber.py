# Fibonacci Number


'''
is defined as each number in the sequence is the sum of 
the two previous numbers
Example : 
0 , 1 , 1 , 2 , 3 , 5 , 8 , 13 , 21


in this example the each number in the sequence is the sum of two previous 
numbers example for the first term 

'''
while True:
                n = int(input("Enter the number"))            
                def Fibonacci(n):
                    count = 0
                    if n == 0 :
                        return count
                    if n == 1:
                        return 1
                    else :
                        count+=1
                        return Fibonacci(n-1)  + Fibonacci(n-2)
                    

                print(Fibonacci(n))