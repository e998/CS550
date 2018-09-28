# 9/27/2018

"""

# lists used for large amounts of data or unknown amounts of data
# mixed data in lists possible, but can make it difficult for function calls

# IMPORTS
import random

# empty list
a = []

# 1. can use append function to add items to list
a.append(5)
a.append(6)
a.append(7)
a.append(8)

# print list (will print nothing for empty list, just brackets)
print(a)


# 2. can simply add items to list
a += [1,2,3,4,5]
print(a)


# specifying order of list
# adds the list itself as position 0 on the list
a.insert(0, [1,2,3,4,5])
print(a) 

# can specify order of list while inputting values from another list 
a = [1,2,3,4,5] + a
print (a)


# list index begins with 0
# len() gives you the length
print(len(a))


# removes from list, does not return (store) the value
del a[5]
print(a)


# a.pop() without an input deletes the last term of the list and returns it
# a.pop() with an input deletes the terms at the given positions

"""
# deletes everything starting from and including x to the end of the list
# a[x:]


# deletes everything just before x, not inclusive
# a[:x]


# deletes everything starting from and including y to the term just before x (not including x)
# a[y:x]

"""

x = random.randint(0,len(a)-1)
del a[x]
print (a)


# print last term
print(a[len(a)-1])
# OR
print(a[-1])


# swap
y,z = 5,10
y,z = z,y
print(y,z)



a[0],a[-1] = a[-1],a[0]



for i in range(2,10,-2):
	print(i)



# range(x) is [0,x)
# range(5,10) is [5,10)




# first 100 numbers
for i in range (1, 100):
	print(7*i)


sevens = []
for i in range(7,701,7):
	sevens.append(i)
print(sevens, len(sevens))
# print (*sevens, len(sevens)) # unpacks list

b = []
for i in range(1,5000):
	b.append(i)
print (b)


c = [x for x in range(2,5000,2)]

"""

for i in range(1,100):
	if ((i%2 == 0 or i%3 == 0) and i%6 != 0):
		print(i)








