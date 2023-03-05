#  1a - Given a list of the numbers between 1 and 10 (but excluding one number) find the missing number
x = set([1, 2, 3, 4, 5, 6, 7, 8, 10])
y = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

z = y.difference(x)
print (z)

#  1b - Modify your program to remove a random number
b = [1, 2, 3, 4, 5, 6, 7, 8, 10]
import random
b.pop(random.randrange(len(b)))
print(b)

#  1c - Update the program to have all numbers from 1 to 100 and remove a random number of elements. Find how many numbers were removed and what they were
lst = list(range(1,101))
print(lst)
a = random.randint(0,101)
print(a)
(lst.pop(random.randrange(len(lst))))*a #how to pass 'a' into this line?
print(lst)

#  1d - Create a new program that duplicates one element in the list at random and then find which number has been duplicated

# 2a - Given the following tuple of numbers, what is the difference between the biggest and smallest number? 2, 5, 12, 7, 9

tup = (2, 5, 12, 7, 9)
tup_diff = (max(tup))-(min(tup))
print(tup_diff)

#  2b - Find the product of the elements of the tuple (product is each item multiplied together)
#print(zip(tup))

from math import prod
print(prod(tup))

#  2c - Modify your program to generate a tuple of random numbers of a random length and still show what the difference and product is

#  3a - Create a dictionary to store the favourite colours of the following individuals
fave_colours = {'Becci' : 'green', 'Steve' : 'orange', 'Melinda' : 'purple', 'Ryan' : 'orange', 'Nate' : 'green' , 'Anna' : 'green'}
#  3b - Add your own favourite colours. Update Melinda’s preference to green and remove Becci’s preference from the dictionary
fave_colours['Lonie']='black'
fave_colours.pop('Becci')
fave_colours.get('Melinda')
fave_colours['Melinda']='green'
print(fave_colours)

#  3c - Write code to create a new dictionary that has the key as each colour’s name and the value being how many people have that colour as their favourite
print(len(fave_colours))


# from collections import counter
# counter(fave_colours))

#  3d - Write code to create another dictionary that has the colour name as the key and a list of all the people that don’t have that colour as their favourite as the value
