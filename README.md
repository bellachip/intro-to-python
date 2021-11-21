# intro-to-python
Hello Everyone! I teach python for beginner high schoolers. All the python code from my tutoring session is uploaded in this repo. This repo will have beginner conecepts of python and fundametals of programming. 

## Updates
The Lesson plan and code for my lesson will be updated every week on Monday nights EST. Please check back on Monday nights for updates!

## Technology Requirements and Setup 
### Replit.com
We use replit.com for our IDE. Replit.com is an online IDE that allows to work and view coding projects in real time. Students are explected to do their homework on the workspace that the teacher created for them. 
link: https://replit.com/

### Python
Please install python from 


## Contents 
+ [Lesson1](https://github.com/bellachip/intro-to-python#lesson-1-9272021) 
  + [Lesson1.py](https://github.com/bellachip/intro-to-python/blob/main/Lesson%201.py)
+ [Lesson2](https://github.com/bellachip/intro-to-python#lesson-2-10042021)
  + [Lesson2.py](https://github.com/bellachip/intro-to-python/blob/main/Lesson2.py)
+ [Lesson3](https://github.com/bellachip/intro-to-python#lesson-3-10112021)
  + [Lesson3.py](https://github.com/bellachip/intro-to-python/blob/main/Lesson3.py)
+ [Lesson4](https://github.com/bellachip/intro-to-python#lesson-4-10112021)
  + [Lesson4.py](https://github.com/bellachip/intro-to-python/blob/main/Lesson4.py)
+ [Lesson5](https://github.com/bellachip/intro-to-python#lesson-5-10252021)
  + [Lesson5.py](https://github.com/bellachip/intro-to-python/blob/main/Lesson5.py)

## Lesson 1 9/27/2021
+ print statements 
+ What is a function?
+ Parameters
+ Strings
+ Variable naming conventions

## Lesson 2 10/04/2021
+ Filename: Lesson2.py 
+ Integers 
+ Floats 
+ Operations 
  + Addition 
  + Subtraction
  + Multiplication
  + Division

### Homework 1
 1. add two numbers 

 2. minus two numbers 

 3. divide two numbers

 4. multiply two numbers 

 5. add up all the results from questions 1~4 and print out the result.

## Lesson 3 10/11/2021
+ shortcuts and different syntax for math expressions
+ boolean operators and statements

### Homework 2
##### Asume a = 3, b = 8

 1. use another expression for a = a + 1 
 2. use another expression for b = b - 2
 3. use another expression for b = b/2
 4. use another expression for a = a*2
 5. print the boolean value of "is 'a' equal to 'b'?"
 6. print the boolean value of "is 'a' not equal to 'b'?"

## Lesson 4 10/11/2021
#### Introduction to 'Lists' and 'For Loops'
One of the most used data structure is a List. Lists allows to store an object (any data types ex. strings, integers, lists, etc). There are many ways to manipulate lists, an example is for loops. Learn how to store elements in lists and utilize for loops to manipulate lists. 

### Homework 4
 1. print all the elements in side string_list
 2. add all the elements in float_list 
 3. create a list of 10 elements consiting of both floats and strings. Then using for loop add all the elements.

## Lesson 5 10/25/2021
+ Lists and For Loops in depth
+ What kind of objects can we store in lists? How to do append a list?
  + Add 
  + Update
  + Remove
  + Clear all elements in list 
+ For loop ranges

### Homework 5
##### nums_list = [1,34,7,17]
##### Animal_list=["koala", "cat", "fox", "panda", "chipmunk", "sloth", "penguin", "dolphin"]
1. Using for loops and range count down numbers from 10 ~ 2 
2. Using for loops and range print numbers from 0~ 9
3. Using for loops and range print out numbers from 1-20 but add 3 to every iteration. 
4. Using for loops add all the numbers in the nums_list
5. Write a for loop print all the elements in the list.
6. Using a for loop and .append() method append 2 more animals in the list. print the appended list 
7. Clear all the elements in the list and print the cleared list

## Lesson 6 11/1/2021
In Lesson 6 we learn about if statements. If statenments are used to check a condition or compare values. 


### Homework 6 
a = 2
b = 3
c = 5
d = 6; 
Animal_list=["koala", "fox", "panda", "chipmunk", "sloth", "penguin", "dolphin"]

1. check if 'a' is equal to 'b'
2. Check if the value of 'd/a' is greater than 2 if not print false 
3. check if sloth and penguin exists in the Animal_list.

## Lesson 7 11/8/2021

### If statement
<img src="https://cdn.programiz.com/sites/tutorial2program/files/Python_if_statement.jpg"
     alt="Markdown Monster icon"
     style="float: left; margin-right: 10px;" />


# If the number is positive, we print an appropriate message
In Python, the body of the if statement is indicated by the indentation. The body starts with an indentation and the first unindented line marks the end.
```ruby
num = 3
if num > 0:
    print(num, "is a positive number.")
print("This is always printed.")

num = -1
if num > 0:
    print(num, "is a positive number.")
print("This is also always printed.")
```
```
3 is a positive number
This is always printed
This is also always printed.
```

### If else statement


Python Conditions and If statements
Python supports the usual logical conditions from mathematics:

+ Equals: a == b
+ Not Equals: a != b
+ Less than: a < b
+ Less than or equal to: a <= b
+ Greater than: a > b
+ Greater than or equal to: a >= b


<img src="https://cdn.programiz.com/sites/tutorial2program/files/Python_if_else_statement.jpg"
     alt="Markdown Monster icon"
     style="float: left; margin-right: 10px;" />

### If... elif... else statement
<img src="https://cdn.programiz.com/sites/tutorial2program/files/Python_if_elif_else_statement.jpg"
     alt="Markdown Monster icon"
     style="float: left; margin-right: 10px;" />

## Lesson 8 11/21/2021
### Python Casting
There may be times when you want to specify a type on to a variable. This can be done with casting. Python is an object-orientated language, and as such it uses classes to define data types, including its primitive types.

Casting in python is therefore done using constructor functions:

+ int() - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)
+ float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
+ str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals

+ x = int(1)   # x will be 1
+ y = int(2.8) # y will be 2
+ z = int("3") # z will be 3
+ x = float(1)     # x will be 1.0
+ y = float(2.8)   # y will be 2.8
+ z = float("3")   # z will be 3.0
+ w = float("4.2") # w will be 4.2
+ x = str("s1") # x will be 's1'
+ y = str(2)    # y will be '2'
+ z = str(3.0)  # z will be '3.0'


### Slicing Strings
You can return a range of characters by using the slice syntax.

Specify the start index and the end index, separated by a colon, to return a part of the string.

Get the characters from position 2 to position 5 (not included):

+ b = "Hello, World!"
print(b[2:5])

Get the characters from the start to position 5 (not included):

+ b = "Hello, World!"
print(b[:5])

Get the characters from position 2, and all the way to the end:

+ b = "Hello, World!"
print(b[2:])

#### Negative Indexing
Use negative indexes to start the slice from the end of the string:


Get the characters:

From: "o" in "World!" (position -5)

To, but not included: "d" in "World!" (position -2):

+ b = "Hello, World!"
print(b[-5:-2])


### Modify Strings
Python has a set of built-in methods that you can use on strings.
#### Upper Case 
The upper() method returns the string in upper case:

a = "Hello, World!"
print(a.upper())
#### Lower Case
The lower() method returns the string in lower case:

a = "Hello, World!"
print(a.lower())
#### Remove Whitespace
The strip() method removes any whitespace from the beginning or the end:

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!
#### Replace String
The replace() method replaces a string with 
another string:
a = "Hello, World!"
print(a.replace("H", "J")) 
#### Split String
The split() method splits the string into substrings if it finds instances of the separator:

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']


### While Loops 
With the while loop we can execute a set of statements as long as a condition is true.

Example
Print i as long as i is less than 6:

i = 1
while i < 6:
  print(i)
  i += 1



The while loop requires relevant variables to be ready, in this example we need to define an indexing variable, i, which we set to 1.


The break Statement
With the break statement we can stop the loop even if the while condition is true:

Example
Exit the loop when i is 3:

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1


### Homework 8
a = "4.2"

b = "Modyfing strings is very easy and fun."

1. Convert 'a' to a float
2. Slice the string 'a' from 0 to 1 
3. Using string slicing, print out only the word 'strings' in 'b'
4. Split string where the "." is in 'a'. 
5. Split string where all the 'i' is in 'b'. 
6. split string where all the ' ' space is in 'b'.
7. Example Print i as long as i is less than 6 using while loop


### Contacts
Email hwy4012@gmail.com for personal zoom session python lessons. Private lessons are held through zoom. Private lessons are $40 per hour.