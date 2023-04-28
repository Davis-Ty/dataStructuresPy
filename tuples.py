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
# end of tuple
