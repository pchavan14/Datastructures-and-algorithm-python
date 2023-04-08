my_dict = dict()
second_dict = {}

my_dict = {"name":"Edy","age":29}
my_dict["name"] = "Teddy"

#Time complexity O(1)
#Space complexity O(1)

my_dict["gender"] = "Female"

#Time complexity O(1)
#Space complexity amortized O(1)

#Traverse through a dictionary

def traverse_dict(my_dict):
    for key in my_dict:
       return(key,my_dict[key])

traverse_dict(my_dict)
#Time complexiy O(n)

#Search for an element in a dictionary
def search_dict(my_dict,value):
    for key in my_dict:
        if my_dict[key] == value:
            return key,value
    return "Did not find it"

search_dict(my_dict,29)
#Time complexity O(n)

#delete from dictionary
my_dict.pop("age") 
#returns the value

#popitem
my_dict.popitem()

#emptied out the whole dictionary
my_dict.clear()

my_dict = {"name":"Edy","age":29,"gender":"Female"}

#delete any key or entire dictionary
del my_dict["gender"]

#Time complexity for deleting is O(1)
#amortized O(n) when huge elements are there










