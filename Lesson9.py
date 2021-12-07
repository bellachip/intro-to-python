#parameters are data that is passed into a function 

#funtion 

# def create_user():
#   print("Create User")
#   username = input("Enter username: ")
#   password = input("Create Password: ")

#   print("You have successfully created your username: " + username)
#   print("You have successfully created your password: " + password)

# def move_left():
#   print("The snake moved left")

# def create_username():
#   print("Create your username")
#   username = input("Enter username: ")
#   print("You have successfully created your username: " + username)


# def example_function(arg1):
#   return arg1

# def add_two(a, b):
#   answer =  a + b
#   print(answer)

# print(example_function("hello"))
  
#Homework 9 
# 1. Create a function that finds the index of a given item.

# Examples 
# search([1, 5, 3], 5) ➞ 1

# search([9, 8, 3], 3) ➞ 2

# search([1, 2, 3], 4) ➞ -1 

#Notes If the item is not present, return -1.

def search_one(nums_list, item): 
  index = 0
  for num in nums_list:   
    if num == item: 
      return index
    elif item not in nums_list: 
      return -1
    index = index+1 

  
# print(search([1, 5, 3], 5))
# print(search([9, 8, 3], 4))
# # print(search([1, 2, 3], 4))

# def search_two(nums_list, item): 
#   if item not in nums_list:
#     return -1
#   elif item in nums_list:
#     return nums_list.index(item)
#print(search([9, 8, 3], 3))
#print(search([1, 2, 3], 4))

def test_my_search_function(string_one, integer_one):
  list_of_lists = [[1,2,3], [2,3,4],[7,8,9],[10,11,12]]
  item = 3
  for list_element in list_of_lists:
    answer = search_one(list_element, item)
    print(answer)

  

test_my_search_function("string", "one")



#Homework 
print(5%2)