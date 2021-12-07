# Q2. Write a program to accept a number from 1 to 7 and display the name of the day like 1 for Sunday , 2 for Monday and so on.

day_num = int(input("Please enter a number from 1 to 7: "))

while day_num:
  
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
      
    day_num = int(input("Please enter a number from 1 to 7: "))
  else:
    day_num = int(input("Please enter a number from 1 to 7: "))