#dictionaries are keys and values
#like a object stored in a object

my_dict = {'apple': 1, 'banana': 2, 'orange': 3}
apple_value = my_dict['apple']
orange_value = my_dict.get('orange')
print(apple_value)  
print(orange_value)  

#changing the value of the key
my_dict['pear'] = 4
my_dict['banana'] = 5
print(my_dict) 

# to remove values we can use del and pop

del my_dict['banana']
orange_value = my_dict.pop('orange')
print(my_dict)  
print(orange_value)


#printing out each element
for key in my_dict.keys():
    print(key)

for value in my_dict.values():
    print(value)

for key, value in my_dict.items():
    print(key, value)