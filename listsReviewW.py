# Lists Practice
# Partner 1: Esther
# Partner 2: Sasha

''' Instructions:
   Work with a partner to complete these tasks. You may assume that all variables/lists are declared and initialized (unless you are specifically asked to create/initialize a list); you need only write the code using the variables/lists indicated in the description. Write your solution below the commented description.
'''

### SOURCES
"""
- Decimal number to a fraction - https://stackoverflow.com/questions/23344185/how-to-convert-a-decimal-number-into-fraction
"""

### IMPORTS
import random


''' 1.
   Create a list of ints, faveNums, that holds 3 integers.
'''
faveNums = [1,2,3]


''' 2.
   Create a list of Strings, holidays, that holds 14 holidays.
'''
holidays = "New Year, Chinese New Year, Valentines Day, St. Patricks Day, Easter, Mother's Day, 4th of July, Father's day, Memorial Day, Veteran's Day, Oktobrfest, Thanksgiving, Hannukah, Christmas".split(",")


''' 3.
   Create a list of characters, grades, that holds 5 letter grades.
'''
grades = ['A', 'B', 'C', 'D', 'F']
 
 
''' 4.
   Create a list of booleans, funny, the can keep track of whether 18 things are funny or not. 
'''
funny = [True]*18


''' 5.
   Create a list of floats, salaries, that holds the salaries of all the employees at a university. The number of employees is stored in the int numEmployees.
'''
salaries = [0.00] * numEmployees


''' 6.
   A picture's dimensions are stored in integer variables x and y. Create a single list of integers that can store the grayscale value for each pixel in the list.
'''
picture = [255]*x*y


''' 7.
   In a class, each student has 0, 1, 2 or 3 siblings. The numbers of students with no siblings is stored in the variable noSiblings, the number of students with one sibling is stored in the variable oneSibling, the number of students with two siblings is stored in the variable twoSiblings, and the number of students with three siblings is stored in the variable threeSiblings. Create a list that holds all the names of the students in the class, as well as the names of all their siblings.
'''
names = ["Bob"] * noSiblings + ["Bobby"] * oneSibling + ["Bobster"] * twoSiblings + ["Bobber"] * threeSiblings


''' 8.
   Create a list that holds all the months in the year. (No loop.)
'''
 months = "January February March April May June July August September October November December".split(" ")


''' 9.
   Create a list that holds all the days of the week. (No loop.)
'''
 daysofweek = "Monday, Tuesday Wednesday, Thursday, Friday, Saturday, Sunday".split(" ")


''' 10.
   Create a list that holds all the possible values for boolean variables. (No loop.)
'''
boolean = [True, False]


''' 11.
   Create a list that holds the names of all the 3rd form dorms on campus. (No loop.)
'''
dorms = "Memorial Nichols Pitman Squire".split(" ")


''' 12.
   Create a list that holds 3 random numbers with values between 0 and 1. (Loop optional.)
'''
randlist = []
for i in range(3):
   randlist.append(random.random())


''' 13.
   Create a list that will represent a deck of cards. Some example data for cards would be AS (ace of spaces), 5H (5 of hearts), JC (jack of clubs), 9D (9 diamonds). (Loop required.) 
'''
deck = []
rank = "2 3 4 5 6 7 8 9 10 J Q K A".split(" ")
suit = "H D S C".split(" ")
for i in range(13):
   for j in range(4):
      deck.append(rank[i]+suit[j])


''' 14.
   Write a Yahtzee program that simulates the rolling of five dice and prints "Yahtzee" if all five dice are the same; otherwise it should print "Try again."
'''
yahtzee = []
for i in range(5):
   yahtzee.append(random.randint(1,6))

if yahtzee[0] == yahtzee[1] == yahtzee[2] == yahtzee[3] == yahtzee[4]:
   print("Yahtzee")
else:
   print("Try again.")


''' 15.
   In a list, specials are numbers in a list that have an even number before them, an odd number behind them, and they themselves are divisible by 3. Given a list of ints called numbers, print out the location in the list of the specials, as well as the value in front of them, their value, and the value behind them. For example:
   position 4: 14, 9, 25
'''
numbers = [1,8,3,5,6,12,7]
for i in range(1,len(numbers)):
    if numbers[i]%3==0 and numbers[i-1]%2==0 and numbers[i+1]%2==1:
        print("position " + str(i) + ": " + str(numbers[i-1]) + ", " + str(numbers[i]) + ", " + str(numbers[i+1]))


''' 16.
   Write a program to search for the "saddle points" in a 5 by 5 list of integers. A saddle point is a cell whose value is greater than or equal to any in its row, and less than or equal to any in its column. There may be more than one saddle point in the list. Print out the coordinates of any saddle points your program finds. Print out "No saddle points" if there are none.
'''
saddlenum = 0
for j in range(len(l)):
    for i in range(len(l)):
        saddle = True
        for a in range(len(l)):
            if l[i][a] > l[i][j]:
                saddle = False
            if l[a][j] < l[i][j]:
                saddle = False
        if saddle:
            print(str(i) + "," + str(j))
            saddlenum += 1
if saddlenum == 0:
   print("No saddle points.")


''' 17.
   In the game of chess, a queen can attack pieces which are on the same row, column, or diagonal. A chessboard can be represented by an 8 by 8 list. A 1 in the list represents a queen on the corresponding square, and a O in the list represents an unoccupied square. Given the two locations for queens (row1, col1, row2, col2), place the queens in the 2D list, chessboard. Then process the board and indicate whether or not the two queens are positioned so that they attack each other. 
'''
chessboard[a1][b1] = 1
chessboard[a2][b2] = 1
if a1 == a2 or b1 == b2 or (a1-a2)/(b1-b2) == 0:
    print("Can attack!")
else:
    print("Cannot attack!")


''' 18.
   Given a list, write code that will reverse the order of the elements in the list. For example, dog, cat, bunny should become bunny, cat, dog.
'''
listA.reverse()


''' 19. 
   Given a list, doorknobs, that holds strings, swap the elements at positions 1 and 3, if possible.
'''
if len(doorknobs) >=3:
   a = doorknobs[1]
   b = doorknobs[3]
   doorknobs.remove(a)
   doorknobs.remove(b)
   doorknobs.insert(1, b)
   doorknobs.insert(3, a)


''' 20.
   In a list of ints called numbers, find the largest number in the list and place it at the end of the list.
'''
maxnum = max(numbers)
numbers.remove(maxnum)
numbers.append(maxnum)


''' 21.
   In a 2D list with dimensions w by h, filled with random numbers from from 1 to 100, replace every odd number with either 2 or 22; 2 if the number was a single digit number, 22 if the number was a 2-digit number. 
'''
for i in range(h):
   for j in range(w):
      if listA[i][j]%2==1:
         if listA[i][j] > 10:
            listA[i][j] = 22
         else:
            listA[i][j] = 2


''' 22.
   In a 2D list with dimensions w by h, holding grayscale values for an image, adjust the colors so the image is inverted. All light portions should be dark, all dark portions should be light. A value of 200 should be 55, a value of 100 should be 155, etc. Remember, there are 256 levels for color, including 0.
'''
for i in range(h):
   for j in range(w):
      graylist[i][j] = 255 - graylist[i][j]


''' 23.
   In a list, shifters, holding ints, shift all elements forward 1 position. For example, position 2 should move to position 1, position 1 to position 0, and position 0 to the end of the list (etc.)
'''
a = shifters[0]
shifters.remove(a)
shifters.append(a)
print(shifters)


''' 24.
   Given an N-by-N grid of elevation values (in meters), a peak is a grid point for which all four neighboring cells are strictly lower. Write a code fragment that counts the number of peaks in a given N-by-N grid.
'''
peaks = 0
for i in range(1,N-1):
   for j in range(1,N-1):
      point = elevation[i][j]
         a = elevation[i][j-1]
         b = elevation[i][j+1]
         c = elevation[i+1][j]
         d = elevation[i-1][j]
         if point > a and point > b and point > c and point > d:
            peaks += 1


''' 25.
   90% of incoming college students rate themselves as above average. Write some code that, given a list of student rankings (stored in integer list rankings), prints the fraction of values that are strictly above the average value.
'''
sumrank = sum(rankings)
average = sumrank / len(rankings)
aboveAvg = 0
for i in range(len(rankings)):
   if rankings[i] > average:
      aboveAvg += 1
fractAbove = aboveAvg/len(rankings)
print(Fraction(fractAbove).limit_denominator())


''' 26. *****
   Given a 9-by-9 list of integers between 1 and 9, check if it is a valid solution to a Sudoku puzzle: each row, column, and block should contain the 9 integers exactly once.
'''
l = [[random.randint(1,9) for j in range(9)] for i in range(9)]
print(l)
for a in range(9):
   if l[a][0] != l[a][1] != l[a][2] != l[a][3] != l[a][4] != l[a][5] != l[a][6] != l[a][7] != l[a][8]:
      row = True
for b in range(9):
   if l[0][b] != l[1][b] != l[2][b] != l[3][b] != l[4][b] != l[5][b] != l[6][b] != l[7][b] != l[8][b]:
      column = True
if row and column:
   valid = True
print(valid)


'''
    27. Create a list of 100 numbers between 1 and 10 (inclusive), create a new list whose first value is the number of 1s in the original list, whose 2nd value is the number of 2s in the original list, and so on. Average the number of occurences of each number in the list over 100 repetitions. Average the averages. Print the result to the screen.
'''
oneSum = 0
twoSum = 0
hundred = []
for i in range(100): # 100 repetitions
   for j in range(100): # 100 numbers in list
      hundred.append(random.randint(1,10))
      # hundred = [random.randint(1,10)]
   occurrences = [hundred.count(1), hundred.count(2)]
   oneSum += occurrences[0]
   twoSum += occurrences[1]
   print(hundred)
   print(oneSum)
   print(twoSum)
oneAvg = oneSum/100
twoAvg = twoSum/100
finalAvg = (oneAvg + twoAvg) / 2
print(finalAvg)


''' Sources
   http://users.csc.calpoly.edu/~jdalbey/103/Projects/ProgrammingPractice.html
   http://introcs.cs.princeton.edu/java/14array/
'''