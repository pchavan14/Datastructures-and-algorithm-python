def fib_memo(memo,n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n not in memo:
        memo[n] = fib_memo(memo,n-1) + fib_memo(memo,n-2)

    return memo[n]







myDict = {}
n = 6
print(fib_memo(myDict,n))
