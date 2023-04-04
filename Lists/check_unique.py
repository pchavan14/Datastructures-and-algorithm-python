
def check_unique(mylist):
    # s = set()
    # for i in mylist:
    #     if i not in s:
    #         s.add(i)
    #     else:
    #         return False
    # return True






    return len(mylist) == len(set(mylist))



mylist = [1,20,30,44,5,56,57,8,19,10,31,12,13,14,35,16,27,58,19,21]
print(check_unique(mylist))