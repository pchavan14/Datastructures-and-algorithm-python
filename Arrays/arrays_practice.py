from array import *

#1. Create an array and traverse
 
my_arr = array('i',[1,2,3,4,5])

print("Step 1")
for i in my_arr:
    print(i)
#O(n)

#2. Access individual elements through indexes
my_arr[0]
#O(1)

#3. Append any value to array using append()
print("Step 3")
my_arr.append(6)
print(my_arr)
#O(1)

#4. Insert value in an array using insert method
print("Step 4")
my_arr.insert(3,7)
print(my_arr)
#o(n)

#5.Extend the array , inplace
print("Step 5")
my_arr1 = array('i',[10,11,12])
my_arr.extend(my_arr1)
print(my_arr)

#6. Add items from list into array using fromlist() method
print("Step 6")
my_list = [20,21,22]
my_arr.fromlist(my_list)
print(my_arr)

#7. Remove last element using pop() method
print("Step 7")
my_arr.pop()
print(my_arr)

#8. Fetch any element through its index using index() method
print("Step 8")
my_arr.index(21)

#9. Reverse the array , it is inplace
print("Step 9")
my_arr.reverse()
print(my_arr)

#10. Get array buffer through buffer_info() method
print("Step 10")
print(my_arr.buffer_info())

#11. Check for number of occurence of an element using count() method
print("Step 11")
print(my_arr.count(21))

#12. Covert array to python using tolist()
print("Step 12")
my_list = my_arr.tolist()
print(type(my_list))

#13. Slice elements from an array
print("Step 13")
print(my_arr[1:3])





