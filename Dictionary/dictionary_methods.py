#dictionary methods

my_dict = {"name":"Edy","age":29,"gender":"Female","education":"master","address":"Seattle"} 


#returns shallow copy of dictionary
copy_dict = my_dict.copy()

#fromkeys() method - create new dictionary with provided keys
new_dict = {}.fromkeys(["name","age","gender","education","address"])

#get() method - finds the keys in dictionary and return value , if the key is not found and value not specified it returns None
my_dict.get("street","Ave") #returns Ave
my_dict.get("street") #returns None

#items () - key ,value tuple pairs
my_dict.items()  #dict_items([('name', 'Edy'), ('age', 29), ('gender', 'Female'), ('education', 'master'), ('address', 'Seattle')])

#keys() - display keys (view object)
my_dict.keys() #dict_keys(['name', 'age', 'gender', 'education', 'address'])

#setdefault() - give the valaue of the key if its present else add the key to dict
my_dict.setdefault("salary",150000)

#values() - returns a view object with list of values in a dict
my_dict.values()

#update () - anaother dictionary values updates the current dictionary
my_dict.update({"name":"Teddy","status":"single"})

print(my_dict)









