# 9/11/2018 - Greetings

# CA: Command Line Greeting Solution

import sys

# sys.argv is a list that starts with term 0 and contains the terms listed in the command line after python3
# second term, listed as term 1, would be username listed on command line after name of the file 
# file name (cs550_2greetings.py) is term 0 (first term) in sys.argv
print("Hello " + sys.argv[1] + "!")