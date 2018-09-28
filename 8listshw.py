# 9/27/2018
# Esther Sojung An
# Challenge Questions! :)

"""
Sources:
- Oleh! Fibonacci Code
- Random sample from list - https://stackoverflow.com/questions/15511349/select-50-items-from-list-at-random-to-write-to-file/39585770
- Sort in descending order - https://medium.com/@chuck.m.park/how-to-sort-integer-list-in-python-descending-order-ae4456c9d362
"""

# Imports
import random as r


# 1. Generate list of 10 random numbers between 0 and 100. Get them in order from largest to smallest, removing numbers divisible by 3.
a = [x for x in range(0,100,1)]
b = []
for x in a:
	if x % 3 != 0:
		b.append(x)
b = r.sample(b, 10)
b.sort(reverse=True)
print(b)



# 2. Print list of the first 50 odd Fibonacci numbers.
c = []
f = [1,1]
i=0
while len(c) <= 50:
	f.append(f[i] + f[i+1])
	if f[i] % 2 != 0:
		c.append(f[i])
	i+=1
print(c)
print(f)



# 3. Print list that contains a number of terms between 0 and 100. Each of the terms must be divisable by two and less than 1000.
a = []
for i in range(r.randrange(100)):
	a += [r.randrange(0,1000,2)]
print(a)


