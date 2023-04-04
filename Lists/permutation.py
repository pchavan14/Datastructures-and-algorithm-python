#always check on boundary cases

def permutation(list1,list2):
    if len(list1) != len(list2):
        return False
    list1.sort()
    list2.sort()
    if list1 == list2:
        return True
    else:
        return False

list1 = [1,2,3,4]
list2 = [4,2,3]
print(permutation(list1,list2))