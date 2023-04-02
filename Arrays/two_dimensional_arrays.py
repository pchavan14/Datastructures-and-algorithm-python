#numppy works perfectly with multidimensional arrays
import numpy as np

twoDArray = np.array([[11,15,10,6],[10,14,11,5],[12,17,12,8],[15,18,14,9]])
#O(1)
#Space - O(mn)

#prints like matrix
print(twoDArray)
# [[11 15 10  6]
#  [10 14 11  5]
#  [12 17 12  8]
#  [15 18 14  9]]

#Insert a new value (addtion of column or addition of row)
newtwoDArray = np.insert(twoDArray,1,[[1,2,3,4]],axis=1) # 1 as column , 0 as row
print(newtwoDArray)
#append method appends row or column at the end of an array

##Access elements of 2D array
print("no of Rows",len(twoDArray)) # just length of array prints the number of rows
print("no of Columns",len(twoDArray[0])) # with 0 index prints the column of 2 D array

#traverse the 2D array
for i in range(0,len(twoDArray)):
    for j in range(0,len(twoDArray[0])):
        print(twoDArray[i][j])
#O(mn)

#deletin two D array
deletedtwoDArray = np.delete(twoDArray,1,0)
print(deletedtwoDArray)









