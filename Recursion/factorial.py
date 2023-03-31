def factorial(n):
    #dying conditions or loopholes
    assert n>=0 and int(n)==n, 'The number must be positive'
    if n == 0:
        return 1
    else:
        return(n * factorial(n-1))
    
print(factorial(1))