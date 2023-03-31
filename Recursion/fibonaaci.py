def fibonacci(n):
    assert n>=0 and int(n)==n, "The number should be positive"
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return(fibonacci(n-1)+fibonacci(n-2))
    
print(fibonacci(-1))