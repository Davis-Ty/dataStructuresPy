#Flexable
#can change size
#easy to use

#a list is a buildt in (data type) 
# can hold elements of differnt data types
# is made with [] and are dynamic-(size cand be changed)


#number list
the_list=[1,2,3,4,5,6]
print(the_list)

#adding the string hello to the list
the_list.append("hello")
print(the_list)

# removing int 4 from list
the_list.remove(4)
print(the_list)

#printing out 2 selected element
print(the_list[0])
print(the_list[4])


#changing the output of an selected element
the_list[2]=2.34
print(the_list)


#adding an element to a list with a given location
the_list.insert(1,78)
print(the_list)

#put the list in order
#only usable with list with numbers
the_list.remove("hello")
the_list.sort()
print(the_list)

#you can pop an selected element 
the_list.pop(1)

print(the_list)

# you can use pop to drop the last element 
the_list.pop()

print(the_list)

#getting the length of the list
print(len(the_list))


#printing list out ne element at a time
#adding string back to list
the_list.append("hello")
for element in the_list:
    print(element)



#End of List



#more memory efficient
#Fast
#multi-dim
#Array is a data structure
#only holds elements of the same data type
#fixed size

#creating a array
import numpy as np


the_array = np.array([4,3,2,5,6,9])
print(the_array)

#print out a selected element in the array
print(the_array[4])
print(the_array[0])

#change the value of a selected element
the_array[2]=7
print(the_array)

#arithmetic operation
#+,-, /, and * all elements in the array
the_array = the_array+2
print (the_array)

the_array = the_array*2
print (the_array)

the_array = the_array-2
print (the_array)


#arrays are only one data type so all elements will just return all int or all float
the_array = the_array/2
print (the_array)

# you can reshape an array making it an 2D array

the_array=the_array.reshape(2,3)
print (the_array)


# you filp the array from a 2 by 3 to a 3 by 2
the_array=the_array.transpose()
print(the_array)

#End of Array



#tuples
# are immutable meaning once created it cant be changed
# represent fixed structured data (ex) coordinates or data time

# can create a tuple and set its values to variables to print out when needed
tuple=(2,3)

x=tuple[0]
y=tuple[1]

print(x,y)

#if we want to add more elements we have to recreate the tuple
# we can assign multi elements to one variable 
tuple=(2,3,4,5,6,7)
give_me_2_nums= tuple[2:4]
print(give_me_2_nums)

#add two tuples 
tuple=(2,3,4,5,6,7)
tuple1=('a','b','c',5,6,7)
put_as_one=tuple+tuple1
print(put_as_one)

#unpack tuple
name, age, city = ('Ace', 24, 'Blue sea')
print(name)  # Output: 'Alice'
print(age)  # Output: 30
print(city)  # Output: 'New York'


#grab key data from tuple
numbers = (1, 2, 3, 4, 5)
count = len(numbers)
minimum = min(numbers)
maximum = max(numbers)
total = sum(numbers)
print(count)  # Output: 5
print(minimum)  # Output: 1
print(maximum)  # Output: 5
print(total)  # Output: 15

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
