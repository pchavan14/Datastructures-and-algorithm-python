
def coinChange(amount,coins):
    
    coins_list = sorted(coins,reverse=True)


    coins_change = []
    while amount > 0:
        print(amount,coins_list)
        if amount >= coins_list[0]:
            coins_change.append(coins_list[0])
            amount = amount - coins_list[0]
        else:
            coins_list.pop(0)    
            if len(coins_list) == 0 and amount != 0:
                return -1    

    if len(coins_change) == 0:
        return -1
    return len(coins_change)















total_number = 6249
coins_list = [186,419,83,408]
print(coinChange(total_number,coins_list))