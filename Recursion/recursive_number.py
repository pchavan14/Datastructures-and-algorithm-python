def recursive_number(n):
    #constraint or the condition which might break our code
    assert n>=0 and int(n) == n , "The number must be positive"
    if n < 1:
        print("n is less than 1")
    else:
        recursive_number(n-1)
        print(n)

recursive_number(-1)