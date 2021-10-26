# This is the first Lession. 
# My code prints Hello World 
# String: 'Hello World'
# Funtion: print()
#Snakecase : Words that are delimited by an underscore 
	# example: variable_x
#Pascalcase: Words that are delimited by capital letters
	# example VarableX
#Camelcase: Words that are delimited by capital letters, excep the initial word
	# example: VariableOneAndTwo

# Types
	# String +
	# Integer +
	# Double 
	# Float +
  # Boolean True/False +
	

# Data Structure
  # List : elements inside the list
	# Dictionary 
	# Tuple 
  # Sets
  # Stack
  # Queue
  # Trees
  # Linked Lists
  # Graphs
  # HashMaps 

# a = "hello"
# print(type(a))

#List
string_list = ["hello", "hi", "world"]
nums_list = [1,34,7,17]
boolean_list = [True,False,True,True]
float_list = [2.23,3.33,4.43]
# print(float_list)

string_list.append("RAY")
string_list.clear()
print(string_list)


print(nums_list[0]+nums_list[1] +nums_list[2] + nums_list[3])

num = 0
for item in nums_list:
  num = item + num
  
print(num)

# 1. print all the elements in side string_list
print(string_list)

for item in string_list:
  print(item)
# 2. using for loop, add all the elements in float_list 
for item in float_list:
  print(item)
# 3. create a list of 10 elements consiting of both floats and strings. Then using for loop add all the elements in side the list you created. 
sample_list = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5]
# print('\n Final Question: \n')
# number = 0
# for item in sample_list:
#   number = item + number
#   print(number)

# print('\n Range Section: \n')
# print(list(range(10)))

#x < 10



# for item in range(1 , 20 , 5): 
#   print(item) 

# for item in range(int(3.3), 1, -2):
#   print(item)

# for item in range(1, 10):
  


# for item in sample_list:
#   for i in range(10):
#     print(item)

# dict = {"Ate breakfast":True, "Ate Dinner": False}

# i = 0
# for key, value in dict.items():

#   print("For user: " + str(i) + " "+ str(key) +  " is " + str(value))
#   i+=1


