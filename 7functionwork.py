# 9/25/2018
# 7functionwork.py


# Imports
import sys


def fibonacci(sys.argv[n+1]):
	s1 = 1
	s2 = 1
	if (n>2):
		for i in range(n-2):
			s = s1 + s2
			s1 = s2
			s2 = s
		return s
	elif (n>=1):
		return 1
	else:
		print "This term does not exist."
	
print(fibonacci(1))
