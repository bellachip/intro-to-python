# # Data Structure
#   # List : elements inside the list
# 	# Dictionary 
# 	# Tuple 
#   # Sets
#   # Stack
#   # Queue
#   # Trees
#   # Linked Lists
#   # Graphs
#   # HashMaps

# #An else statement can be combined with an if statement. An else statement contains the block of code that executes if the conditional expression in the if statement resolves to 0 or a FALSE value.

# #The else statement is an optional statement and there could be at most only one else statement following if.

# #The elif statement allows you to check multiple expressions for TRUE and execute a block of code as soon as one of the conditions evaluates to TRUE.

# #Similar to the else, the elif statement is optional. However, unlike else, for which there can be at most one statement, there can be an arbitrary number of elif statements following an if.

# # Program checks if the number is positive or negative
# # And displays an appropriate message

# # num = 3

# # # Try these two variations as well. 
# # # num = -5
# # # num = 0

# # if num >= 0:
# #   #body of the if statement
# #     print("Positive or Zero")
# # else:
# #   # body of the else statement
# #     print("Negative number")

# # '''In this program, 
# # we check if the number is positive or
# # negative or zero and 
# # display an appropriate message'''

# # num = 3.4

# # # Try these two variations as well:
# # # num = 0
# # # num = -4.5

# # if num > 0:
# #     print("Positive number")
# # elif num == 0:
# #     print("Zero")
# # else:
# #     print("Negative number")

# # # check if the number is positive, negative, 0. 

# # #python Nessted if statements 
# # '''In this program, we input a number
# # check if the number is positive or
# # negative or zero and display
# # an appropriate message
# # This time we use nested if statement'''

# # num = float(input("Enter a number: "))
# # if num >= 0:
# #     if num == 0:
# #         print("Zero")
# #     else:
# #         print("Positive number")
# # else:
# #     print("Negative number")



# #input function allows the user to type and records the keyboard strokes. 
# #int() = covert string to an integer
# num = int(input("Please enter your number: "))


# # if num >= 0:
# #     if num == 0:
# #         print("you entered Zero")
# #     else:
# #         print("You entered a Positive number")
# # else:
# #     print("you entered Negative number")


# # Homework 7
# #Q1. Write a program to accept percentage from the user and display the grade according to the following criteria:

# #Marks           | Grade
# # >=90           |   A
# # >= 80 and <= 89|   B
# # >= 70 and <= 79|   C
# # >= 60 and <= 69|   D
# # below 60       |   F

# num = int(input("Please enter your number: "))
# if num >= 60:
#   if num >= 90:
#     print("You get an A.")
#   elif num <= 89 and num >= 80:
#     print("You get a B.")
#   elif num <= 79 and num >= 70:
#     print("You get a C.")
#   elif num <= 69 and num >= 60:
#     print("You get a D.")
# else:
#   print("You get a F.")


# if num >= 90:
#   print("You get an A.")
# elif num <= 89 and num >= 80:
#   print("You get a B.")
# elif num <= 79 and num >= 70:
#   print("You get a C.")
# elif num <= 69 and num >= 60:
#   print("You get a D.")
# else:
#   print("You get a F.")

# Q2. Write a program to accept a number from 1 to 7 and display the name of the day like 1 for Sunday , 2 for Monday and so on.

day_num = int(input("Please enter a number from 1 to 7: "))

while day_num != "quit":
  if day_num >= 1 and day_num <= 7:
    if day_num == 1:
      print("The number for Sunday.")
    if day_num == 2:
      print("The number for Monday.")
    if day_num == 3:
      print("The number for Tuesday.")
    if day_num == 4:
      print("The number for Wednesday.")
    if day_num == 5:
      print("The number for Thursday.")
    if day_num == 6:
      print("The number for Friday.")
    if day_num == 7:
      print("The number for Saturday.")
  else:
    input("Please enter a number from 1 to 7: ")