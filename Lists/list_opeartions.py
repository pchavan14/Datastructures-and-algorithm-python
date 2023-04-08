#accessin / traversing a list
shopping_list = ['Milk','Cheese','Butter']

shopping_list[0]
#each index maps to one of element in list

#print('Milk' in shopping_list)

#accessing elements from backwards
shopping_list[-3]

#traverse through list
for i in shopping_list:
   i

#using range and len function
for i in range(0,len(shopping_list)):
    shopping_list[i]+"+"

#Update/Insert - List
shopping_list[2] = 'Bread' #O(1)
shopping_list.append('Butter') #O(1)
#print(shopping_list)

my_list = [1,2,3,4,5]

#inserting elements in a list
my_list.insert(0,11)
#Time complexity - O(n)

my_list.append(12)
#O(1)

my_list_2 = [23,24,25]
my_list.extend(my_list_2)
#O(n) - adds element in the ordered way we declare

print(my_list)

#Slice / Delete from the list
my_list[-3:]

#Delete and element from list
#pop() - it removes the last element by default , we have to provide the index of element to delete and it returns the element
my_list.pop(0)

#del - if we dont need the value and works on index
del my_list[0]

#remove - delete the value , we just provide the value
my_list.remove(25)









