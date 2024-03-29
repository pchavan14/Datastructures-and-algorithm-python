# if we just reserve the space for array and do not insert elements into it might cause memory leaks

from array import *

#array creation

arr1 =array('i',[1,2,3,4,5,6])
#Time complexity - O(1) when we create an array and initiallize it with values
#Time complexity - O(n) when we create an empty array and later insert values in it

#insert values in array (inplace)
arr1.insert(0,7)
#Time complexity - O(n) at the beginning of array
#Time complexity - O(1) at the end of array


#arrays and mutable and we can replace a value
arr1[0] = 10
#Time complexity - o(1)

#Array traversal
def traverseArray(arr1):
    for i in arr1:
        print(i)
traverseArray(arr1)
#Time complexity - O(n)
#Space complexity - O(1)

#Access array element
print("Fourth element in an array",arr1[3])

#search a value within an array
def findingElement(arr1,element):
    for i in arr1:
        if i == element:
            return arr1.index(i) #Array mmethod with time complexity O(n)
    return 'Element not found'

print(findingElement(arr1,5))
#Time complexity - O(n) - worst case

#delete an element from array
#remove element only removes one occurence of element in case of duplicates
arr1.remove(10)
print(arr1)
#Time complexity - O(n) - Worst case
#Space complexity - O(1)

def palindromic_string(sample_str):
    i = 0
    j = len(sample_str) - 1

    while (i < j):
        if sample_str[i] == sample_str[j]:
            i += 1
            j -= 1
            continue
        else:
            return False       
    return True

print(palindromic_string('abab'))































