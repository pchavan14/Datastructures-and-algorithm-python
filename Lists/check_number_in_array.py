import numpy as np



#questions
#1. Are all the numbers distinct ?
#2. If no do we need to find just one occurence of the element

def find_number(myarray,target):
    for i in range(len(myarray)):
        if myarray[i] == target:
            return f"Found the number at index {i}"
    return "Did not find the number"


myarray = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13])
target = 1
print(find_number(myarray,target))
