
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