dollar = int(input())
bills = 0
while dollar > 0:
    if dollar >= 100:
        bills += dollar // 100
        dollar %= 100
    elif dollar >= 20:
        bills += dollar // 20
        dollar %= 20
    elif dollar >= 10:
        bills += dollar // 10
        dollar %= 10
    elif dollar >= 5:
        bills += dollar // 5
        dollar %= 5
    else:
        bills += dollar 
        dollar = 0
    # print(dollar)
    
print(bills)