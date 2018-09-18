# 9/14/2018

import sys
import math as m

P = float(sys.argv[1])
r = float(sys.argv[2])
t = float(sys.argv[3])

P1 = float(P * (m.e ** (r*t)))

print("You have: $" + str(P1) + " after " + str(t) + " years.")