##divide and conquer create a smaller code and recursively call it
def fibonacci(n):
    if n < 0:
        return None
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)




n = 4
print(fibonacci(n))
