import numpy as np

def max_product(myarray):
    product = 0
    for i in range(len(myarray)):
        for j in range(i+1,len(myarray)):
            product = max(product,(myarray[i]*myarray[j]))
    return product

#time complexity - O(n^2)






myarray = np.array([1,20,30,44,5,56,57,8,9,10,31,12,13,14,35,16,27,58,19,21])
print(max_product(myarray))
