def fib_memo(memo,n):
    if n == 0:
        return 0
    if n in (1,2):
        return 1
    if n not in memo:
        memo[n] = fib_memo(memo,n-1) + fib_memo(memo,n-2)

    return memo[n]







myDict = {}
n = 5
print(fib_memo(myDict,n))
