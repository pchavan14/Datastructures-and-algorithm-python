
def check_unique(mylist):
    #lookup in a set is O(1)
    s = set()
    for i in mylist:
        if i not in s:
            s.add(i)
        else:
            return False
    return True


mylist = [1,20,30,44,5,56,57,8,19,10,31,12,13,14,35,16,27,58,19,21]
print(check_unique(mylist))

#set is implemented as hash table so insert/update/delete is O(1)
#set is unordered
#use set as a data structure where we don't need ordered data