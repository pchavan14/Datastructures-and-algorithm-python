def number_factor(n):
    if n in (0,1,2):
        return 1
    if n == 3:
        return 2
    else:
        return number_factor(n-1) + number_factor(n-3) + number_factor(n-4)
    

print(number_factor(5))