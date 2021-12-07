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

#Homework 10 
given_list = [1,2,3,4,5,6,7,8]
# 1. Write a Python function to sum all the numbers in a list.

def sum(number_list):

# 2. Write a Python program to print the even numbers from a givenlist

def even_num(number_list):
