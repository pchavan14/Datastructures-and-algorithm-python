fruit_list1 = ['Apple', 'Berry', 'Cherry', 'Papaya']
fruit_list2 = fruit_list1 # the address of both the lists are same as we assign the address of list 1 to list 2
fruit_list3 = fruit_list1[:] # we assign only the values of list 1 into list 3
 
fruit_list2[0] = 'Guava'
fruit_list3[1] = 'Kiwi'
 
print(fruit_list1)
print(fruit_list2)
print(fruit_list3)


sum = 0
for ls in (fruit_list1, fruit_list2, fruit_list3):
    if ls[0] == 'Guava':
        sum += 1
    if ls[1] == 'Kiwi':
        sum += 20
 
print(sum)