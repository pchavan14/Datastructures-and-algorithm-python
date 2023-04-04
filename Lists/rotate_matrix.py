#rotate the matrix 90 degrees

import numpy as np

myarray = [[1,2,3],[4,5,6],[7,8,9]]

#transpose the matrix
for i in range(len(myarray)):
    for j in range(i,len(myarray[0])):
        myarray[i][j], myarray[j][i] = myarray[j][i],  myarray[i][j]
print("Transpose",myarray)

#reverse the rows
for i in range(len(myarray)):
    left = 0
    right = len(myarray[i]) - 1
    while(left < right):
        myarray[i][left] , myarray[i][right] = myarray[i][right],myarray[i][left]
        left += 1
        right -= 1

print(myarray)




