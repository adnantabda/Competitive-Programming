def richest_customer_wealth(accounts ):
    for i in range(0, len(accounts)):
        accounts[i] = sum(accounts[i])
    return max(accounts)


accounts = [[2,4,6,91],[56,73,9,22]]
print(richest_customer_wealth(accounts))