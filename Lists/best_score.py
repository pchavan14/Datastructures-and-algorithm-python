# Best Score

# Given a list, write a function to get first, second best scores from the list.

# List may contain duplicates.

# Example

#     
#     firstSecond(myList) # 90 87

def firstSecond(givenList):
    # TODO
    givenList.sort(reverse= True)
    first_best = givenList[0]

    for i in range(1,len(givenList)):
        if givenList[i]!= first_best:
            return first_best, givenList[i]



myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]
print(firstSecond(myList))