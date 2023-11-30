import array #in built python array method
import numpy as np #need to install

my_array = array.array('i',[1,2,3])
my_array[0] = 9 #replace , we do have insert method when needed 

print(my_array[0])
np_array = np.array([],dtype=int)

my_array.insert(2,5) #insert an element which leads other elements to move 
print(my_array)

#using index
for i in range(0,len(my_array)):
    print(my_array[i])

#traversing through array
for i in my_array:
    print(i)


my_array.remove(2)

print(my_array)
