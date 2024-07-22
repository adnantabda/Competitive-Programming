number = int(input())

def luckNumber(n):
    count = 0
    string_number = str(n)
    for i in string_number:
        if int(i) == 7 or int(i) == 4:
            count +=1

    count = str(count)
    for i in count:
        if int(i) == 7 or int(i) ==4:
            pass
        else:
            return "NO"
             
        
    return "YES"


print(luckNumber(number))

