#List operations / functions

#concatenations of two lists
a = [1,2,3]
b = [4,5,6]

c = a + b

#star operator ( all values of list are repititive with the values)
a = [1,2,3]
b = a * 4
#[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]

#number of elements in list
len(a)

#returns max element in a list
max(a)

#returns min element in a list
min(a)

#returns sum of element in a list
sum(a) 

#convert string to list
a = 'spam'
b = list(a)

#convert a sentence to list with a delimiter
a = 'spam spam spam'
b  = a.split()

#convert list to string 
' , '.join(b)

#Pitfalls and ways to avoid them
#Most list methods modify the argument and return None (inplace changes)
c = [2,1,3,5,6]
c.sort()
#sorted function do not change original list

#Array vs list
import numpy as np
my_arr = np.array([1,2,3,4,5])
my_list = [1,2,3,4,5]

# my_arr / 2 #supported
# my_list / 2 #not supported

my_arr_2 = np.append(my_arr,'a')
print(my_arr_2)





