# Esther An
# 9/13/2018
# HW CS550_3
# 01_math_examples.docx
# Sources: Found sys.stdout.write (https://www.programcreek.com/python/example/52597/sys.stdout.write)

import sys

# 1. Program that takes two floats t & v from command-line and writes wind chill.  
t = float(sys.argv[1])
v = float(sys.argv[2])
if (t<=50 and t>=-50 and v<=120 and v>=3):
	w = 35.74 + 0.6125*t + (0.4275*t - 35.75)*(v**0.16)
	print("Wind chill is", w)
else:
	print("Formula is not valid for given temperature and/or wind speed.")



# 2. Program that takes three floats x, y, and z in command-line and writes 'True' if values are strictly ascending or descending and 'False' if not. 
x = float(sys.argv[1])
y = float(sys.argv[2])
z = float(sys.argv[3])
check = bool(x < y < z or x > y > z)
print("This is " + str(check))



# 3. Program that accepts a date as input and writes the day of the week on which that date falls. 
m = int(sys.argv[1])
d = int(sys.argv[2])
y = int(sys.argv[3])

y1 = int(y - int((14-m)/12))
x = int(y1 + int(y1/4) - int(y1/100) + int(y1/400))
m1 = int(m + 12*int((14-m)/12) - 2)
d1 = int(int(d + x + int((31*m1)/12)) % 7)

sys.stdout.write(str(d1))

if(d1==0):
	print(", The day was a Sunday.")
elif(d1==1):
	print(", The day was a Monday.")
elif(d1==2):
	print(", The day was a Tuesday.")
elif(d1==3):
	print(", The day was a Wednesday.")
elif(d1==4):
	print(", The day was a Thursday.")
elif(d1==5):
	print(", The day was a Friday.")
else:
	print(", The day was a Saturday.")


