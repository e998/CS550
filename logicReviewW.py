# Logic Review

# Partner 1: Eyad
# Partner 2: Esther
''' Instructions:
   Work with a partner to complete these tasks. Assume that all variables are declared; you need only write the if-statement using the variables indicated in the description. Write your solution below the commented description.
'''

''' 1.
   Variable grade is a character. If it is an A, print good work. 
'''
   if grade == 'A' :
      print("good work")
 
 
''' 2.
   Variable yards is an int. If it is less than 17, multiply yards by 2.
'''
   if yards < 17
      yards = yards * 2


''' 3.
   Variable success is a boolean. If something is a success, print congratulations. 
'''
   if success:
      print("congratulations")


''' 4.
   Variable word is a String. If the string's second letter is 'f', print fun.
'''
   if word[1] == 'f':
      print("fun")


''' 5.
   Variable temp is a float. Variable celsius is a boolean. If celsius is true, convert to fahrenheit, storing the result in temp. F = 1.8C + 32.
'''
   if celsius:
      temp = (temp * 1.8) + 32
      celsius = False


''' 6.
   Variable numItems is an int. Variable averageCost and totalCost are floats. If there are items, calculate the average cost. If there are no items, print no items.
'''
   if numItems > 0:
      averageCost = totalCost/numItems
      print(averageCost)
   else:
      print("no items")


''' 7.
   Variable pollution is a float. Variable cutoff is a float. If pollution is less than the cutoff, print safe condition. If pollution is greater than or equal to cutoff, print unsafe condition. 
'''
   if pollution < cutoff:
      print("safe condition")
   else:
      print("unsafe condition")


''' 8.
   Variable score is a float, and grade is a char. Store the appropriate letter grade in the grade variable according to this chart.
   F: <60; B: 80-89; D: 60-69; A: 90-100; C: 70-79.
'''
   score = score // 10
   list = [1, 2, 3, 4, 5, 6, 7, 8 , 9, 10, 'F', 'F', 'F', 'F', 'F', 'D', 'C', 'B', 'A', 'A']
   grade = list[list.index(score) + 10]


''' 9.
   Variable letter is a char. If it is a lowercase letter, print lowercase. If it is an uppercase, print uppercase. If it is 0-9, print digit. If it is none of these, print symbol.
'''
   if letter.islower():
      print("lowercase")
   elif letter.isupper():
      print("uppercase")
   elif letter.isdigit():
      print("digit")
   else:
      print("symbol")


''' 10.
   Variable neighbors is an int. Determine where you live based on your neighbors.
   50+: city; 25+: suburbia; 1+: rural; 0: middle of nowhere. 
'''
   if neighbors >= 50:
      print("city")
   elif neighbors >= 25:
      print("suburbia")
   elif neighbor >= 1:
      print("rural")
   else:
      print("middle of nowhere")


''' 11.
   Variables doesSignificantWork, makesBreakthrough, and nobelPrizeCandidate are booleans. A nobel prize winner does significant work and makes a break through. Store true in nobelPrizeCandidate if they merit the award and false if they don't. 
'''
   if doesSignificantWork and makesBreakthrough:
      nobelPrizeCandidate = True
   else:
      nobelPrizeCandidate = False


''' 12.
   Variable tax is a boolean, price and taxRate are floats. If there is tax, update price to reflect the tax you must pay.
'''
   if tax:
      price = price + price * taxRate


''' 13.
   Variable word and type are Strings. Determine (not super accurately) what kind of word it is by looking at how it ends. 
   -ly: adverb; -ing; gerund; -s: plural; something else: error   
'''
   if word.endswith("ly") == True :
      type = "adverb"
   elif word.endswith("ing") == True :
      type = "gerund"
   elif word.endswith("s") == True :
      type = "plural"
   else:
      type = "error"


''' 14.
   If integer variable currentNumber is odd, change its value so that it is now 3 times currentNumber plus 1, otherwise change its value so that it is now half of currentNumber (rounded down when currentNumber is odd).
'''
   if currentNumber%2 == 1:
      currentNumber = currentNumber * 3 + 1
   else:
      currentNumber /= 2


''' 15.
   Assign true to the boolean variable leapYear if the integer variable year is a leap year. (A leap year is a multiple of 4, and if it is a multiple of 100, it must also be a multiple of 400.) 
'''
   if year % 4 == 0:
      if year % 100 == 0:
         if year % 400 == 0:
            leapYear = True
      else:
         leapYear = True


''' 16.
   Determine the smallest of three ints, a, b and c. Store the smallest one of the three in int result. 
'''
result = min(a, b, c)


''' 17.
   If an int, number, is even, a muliple of 5, and in the range of -100 to 100, then it is a special number. Store whether a number is special or not in the boolean variable special. 
'''
if number%10==0 and number>=-100 and number<=100:
   special = True
else:
   special = False


''' 18.
   Variable letter is a char. Determine if the character is a vowel or not by storing a letter code in the int variable code.
   a/e/o/u/i: 1; y: -1; everything else: 0
'''
   bool = letter == 'a' or letter == 'e' or letter = 'i' or letter = 'o' or letter = 'u' 
   if bool == True :
      code = 1
   elif letter == 'y' :
      code = -1
   else :
      code = 0


''' 19.
   Given a string dayOfWeek, determine if it is the weekend. Store the result in boolean isWeekend.
'''
   day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"] 
   if dayOfWeek == day[5] or dayOfWeek == day[6]:
      isWeekend = True
   else:
      isWeekend = False
   print(isWeekend)
 

''' 20.
   Given a String variable month, store the number of days in the given month in integer variable numDays. 
'''
   lis = ["jan", "mar", "may", "jul", "aug", "oct", "dec", "apr", "jun", "sep", "nov", "feb"]
   if lis.index(month) > 10 :
      numDays = 28
   elif lis.index(month) > 6 :
      numDays = 30
   else:
      numDays = 31


''' 21. 
   Three integers, angle1, angle2, and angle3, supposedly made a triangle. Store whether the three given angles make a valid triangle in boolean variable validTriangle.
'''
   if angle1 + angle2 + angle3 == 180 :
      validTriangle = True


''' 22.
   Given an integer, electricity, determine someone's monthly electric bill, float payment, following the rubric below. 
   First 50 units: 50 cents/unit
   Next 100 units: 75 cents/unit
   Next 100 units: 1.20/unit
   For units above 250: 1.50/unit, plus an additional 20% surcharge.
'''
   if electricity > 250 :
      payment = 220 + 1.5 * (electricity - 250) * 1.2
   elif electricity > 150 :
      payment = 100 + 1.2 * (electricity - 150)
   elif electricity > 50 :
      payment = 25 + 0.75 * (electricity - 50)
   else:
      payment = 0.5 * electricity


''' 23.
   String, greeting, stores a greeting. String language stores the language. If the language is English, greeting is Hello. If the language is French, the greeting is Bonjour. If the language is Spanish, the greeting is Hola. If the language is something else, the greeting is something of your choice.
'''
   if language == "English":
      greeting = "Hello"
   elif language == "French":
      greeting = "Bonjour"
   elif language == "Spanish":
      greeting = "Hola"
   else:
      greeting = "YAY"


''' 24. 
   Generate a phrase and store it in String phrase, given an int number and a String noun. Here are some sample phrases:
   number: 5; noun: dog; phrase: 5 dogs
   number: 1; noun: cat; phrase: 1 cat
   number: 0; noun: elephant; phrase: 0 elephants
   number: 3; noun: human; phrase: 3 humans
   number: 1; noun: home; phrase: 3 homes
'''
   number = 20
   noun = "whales"
   phrase = str(number) + " " + noun


''' 25. 
   If a string, userInput, is bacon, print out, "Why did you type bacon?". If it is not bacon, print out, "I like bacon."
'''
   if userInput == "bacon"
      print("Why did you type bacon?")
   else:
      print("I like bacon.")


''' 26.
   Come up with your own creative tasks someone could complete to practice if-statements. Also provide solutions.
'''

''' Task 1:
   The area of a trapezoid can be found with the formula A = (1/2) * (b1 + b2)/h. Store whether the given values of floats b1, b2, and h form a trapezoid with an area greater than 25 in boolean bigTrap.
'''
   # solution
   if A > 25:
      bigTrapezoid = True
   else:
      bigTrapezoid = False


''' Task 2:
   A triangle with sides a, b, and c is a right triangle if a^2 + b^2 = c^2, an obtuse triangle is a^2 + b^2 > c^2, and an acute triangle if a^2 + b^2 < c^2. Store what kind of triangle is given in a String, angle, by printing "right", "obtuse" or "acute".
'''
   # solution
   if a ** 2 + b ** 2 = c ** 2:
      print("right")
   elif a ** 2 + b ** 2 > c ** 2:
      print("obtuse")
   else:
      print("acute")


''' Task 3:
   Assign true to a boolean, divide, if an integer, number, is divisible by 2, 3, 4, 5, or 6, but not 7, 8, 9, or 10.
'''
   # solution
   if number%2==0 or number%3==0 or number%5==0:
      if number%7!=0 and number%8!=0 and number%9!=0 and number%10!=0:
         divide = True
      else:
         divide = False
   divide = False


''' Sources
 http://www.bowdoin.edu/~ltoma/teaching/cs107/spring05/Lectures/allif.pdf
 http://www.codeforwin.in/2015/05/if-else-programming-practice.html
 Ben Dreier for pointing out some creative boolean solutions.
'''