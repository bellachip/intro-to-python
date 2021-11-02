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

nums_list = [1,34,7,17]
Animal_list=["koala", "cat", "fox", "panda", "chipmunk", "sloth", "penguin", "dolphin"]
# 1. Using for loops count down numbers from 10 ~ 2
# for item in range(10, 1, -1):
  # print(item)
# 2. Using for loops print numbers from 0~ 9
# for item in range(0, 10, 1):
  # print(item)
# 3. Using for loops and range print out numbers from 1-20 but add 3 to every iteration. 
# for item in range(1, 21, 3):
  # print(item)
# 4. Using for loops add all the numbers in the nums_list
print('\nNUMBER 4: \n')
sum_value = 0
for number in nums_list:
  sum_value = number + sum_value
  print(sum_value)
print(sum_value)
# 5. Write a for loop print all the elements in the list.
for item in nums_list:
  print(item)
# 6. .append() method append 2 more animals in the list. print the appended list 
Animal_list.append("cardinal")
Animal_list.append("Lion")
print(Animal_list)
# 7. Clear all the elements in the list and print the cleared list
Animal_list.clear()
print(Animal_list)