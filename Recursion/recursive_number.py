def recursive_number(n):
    if n < 1:
        print("n is less than 1")
    else:
        recursive_number(n-1)
        print(n)

recursive_number(4)