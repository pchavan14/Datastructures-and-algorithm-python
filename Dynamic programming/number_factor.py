def number_factor_top_down(memo,n):
    if n in (0,1,2):
        return 1
    elif n == 3:
        return 2
    elif n in memo:
        return memo[n]
    else:
        if n not in memo:
            memo[n] = number_factor_top_down(memo,n-1) +  number_factor_top_down(memo,n-3) +  number_factor_top_down(memo,n-4)
    
    return memo[n]
    
#bottom up tabulation
def number_factor_bottom_up(n):
    tb = [1,1,1,2]
    for i in range(4,n+1):
        tb.append(tb[i-1] + tb[i-3] + tb[i-4])
    return tb[n]







n = 5
memo = {}
number_factor_top_down(memo,n)
print(number_factor_bottom_up(n))