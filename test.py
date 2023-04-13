def minSwaps(arr):
    '''Function that returns
       the minimum swaps'''
     
    n = len(arr)
    minn, maxx, l, r = -1, arr[0], 0, 0
 
    for i in range(n):
         
        # Index of leftmost
        # largest element
        if arr[i] > minn:
            minn = arr[i]
            l = i
             
        # Index of rightmost
        # smallest element
        if arr[i] <= maxx:
            maxx = arr[i]
            r = i
             
    if r < l:
        print(l + (n - r - 2))
    else:
        print(l + (n - r - 1))
         
# Driver code
arr = [2,4,3,1,6]
 
minSwaps(arr)