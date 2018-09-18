# Esther An
# 9/15/2018
# Grade Calculator w/ Command Line
# Source(s): N/A

"""
A+ = 4.85+
A = 4.7+
A- = 4.5+
B+ = 4.2+
B = 3.85+
B- = 3.5+
C+ = 3.2+
C = 2.85+
C- = 2.5+
D+ = 2+
D = 1.5+
D- = 1.0+
F = 0+
"""

import sys

g = float(sys.argv[1])
if g>5 or g<0:
	print("This grade is not in range of [0,5].")
else:
	if g >= 4.85:
		print("A+")
	elif g >= 4.7:
		print("A")
	elif g >= 4.5:
		print("A-")
	elif g >= 4.2:
		print("B+")
	elif g >= 3.85:
		print("B")
	elif g >= 3.5:
		print("B-")
	elif g >= 3.2:
		print("C+")
	elif g >= 2.85:
		print("C")
	elif g >= 2.5:
		print("C-")
	elif g >= 2:
		print("D+")
	elif g >= 1.5:
		print("D")
	elif g >= 1:
		print("D-")
	else:
		print("F")


