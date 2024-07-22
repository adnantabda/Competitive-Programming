n = int(input())
sum_ = 0 
for question in range(n):
    sure_status = input()
    i_sure = [ int(i) for i in sure_status.split(" ")]
    if sum(i_sure) >= 2:
        sum_ +=1
        
        
print(sum_)



