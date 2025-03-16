# This is a single line comment in Python, we use # symbol
# Welcome to Financial Software Engineering

'''
This is a multi-line comment in Python using triple-quoted strings.
A multi-line comment is also known as a docstrings and  used in Python to provide 
documentation for modules, functions, classes, and methods i.e. describe the purpose, behavior, 
and usage of the code element they are attached to. 
Docstrings can be accessed at runtime using the built-in Python __doc__ attribute.
'''

'''
The purpose of commenting out multiple lines in Python 
is to disable or exclude a block of code from execution.
'''

print("Hello, World!")

student_name = "John Doe"
print(type(student_name))
print("*****")


STUDENT_NUMBER = "DEJ001" # STUDENT_NUMBER is a constant, a constant is a value that is not supposed to change
print(type(STUDENT_NUMBER))
print("*****")
student_age = 21
print(type(student_age))
print("*****")
student_height_cms = 165.5
print(type(student_height_cms))
print("*****")
student_registered = False
print(type(student_registered))
print("*****")
student_modules = ["Fintech and Cryptocurrencies", "Financial Software Engineering", "Supervised Learning"]
print(type(student_modules))
print("*****")

# type casting
student_age = str(21)
print(type(student_age)) # student_age will now be '21' i.e. a string instead of 21 (an int)
print("*****")

# tuple having only integer type of data.
student_ages = (21,22,23,24)
print(student_ages) #prints the whole tuple

# example dict - A Python dictionary is a data structure that stores the value in key: value pairs. 
# Values in a dictionary can be of any data type and can be duplicated, whereas keys can’t be repeated 
# and must be immutable.
student_name = "first name"
student_surname = "last name"
student_age = 33

student_record = {"student_name": student_name, "student_surname": student_surname, "student_age": student_age}
print(student_record) #prints the whole dictionary
print(student_record["student_name"]) 

# alternatively create dictionary using dict() constructor
student_record2 = dict(student_name = "first name", student_surname = "last name", student_age = 33)
print(student_record2) #prints the whole dictionary

# example set - an unordered collection with no duplicated elements
my_set = {10, 50, 20, 20}
print(my_set)
print(type(my_set))

# Arithmetic Operators
input_one = 4
input_two = 2

add = input_one + input_two 

sub = input_one - input_two 

mul = input_one * input_two 

mod = input_one % input_two # modulo

exp = input_one ** input_two # In Python, the double-star operator (**) is used for exponentiation

print(add) 
print(sub) 
print(mul) 
print(mod) 
print(exp) 

#Logical Operators
bool_input_one = True
bool_input_two = False
print(bool_input_one and bool_input_two) 
print(bool_input_one or bool_input_two) 
print(not bool_input_one) 

# Conditional statements
a = 7
b = 5
c = 10

# Equals 
print(a == b)

# Not Equals
print(a != b)

# Less Than
print(a < b)

# Less than or equal to
print(a <= b)

# Greater than: 
print(a > b)

# Greater than or equal to
print(a >= b)

if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

# and
if a > b and c > a:
  print("Both conditions are True")

# or 
if a > b or a > c:
  print("At least one of the conditions is True")

# and plus or
if (a > b and c > a) or ( a > b or a > c):
  print("Both conditions are True or At least one of the conditions is True")



# not
if not a > b:
  print("a is NOT greater than b")

i = 20
if (i < 15): 
    print("i is smaller than 15") 
    print("i'm in if Block") 
else: 
    print("i is greater than 15") 
    print("i'm in else Block") 
print("i'm not in if and not in else Block") 

i = 20
if (i == 10): 
    print("i is 10") 
elif (i == 15): 
    print("i is 15") 
elif (i == 20): 
    print("i is 20") 
else: 
    print("i is not present") 

# user input as string
username = input("Enter username:")
print("Username is: " + username)

# Taking input as string
course_code = input("What is the course code for FSE?: ")
print(course_code)

# Taking input as int and typecasting to int
n = int(input("How many classes?: "))
print(n)

# Taking input as float typecasting to float
price = float(input("Price of each pen?: "))
print(price)

# For Loop
for i in range(0, 10, 2): 
    print(i) 

currencies = ["USD", "ZAR", "ZWM"]
for x in currencies:
  print(x)

# While Loop
count = 0
while (count < 3): 
    count = count + 1
    print("Hello FSE")

#infinite loop
count = 0
while (count == 0):
    print("Hello FSE infinite")

# For Loop with a break
for i in range(5):
    if i == 3:
        break  # Exit the loop when i is 3
    print(i)
    
# While Loop with a break
i = 0
while i < 5:
    if i == 3:
        break  # Exit the loop when i is 3
    print(i)
    i += 1

# continue in for loop
for i in range(5):
    if i == 3:
        continue  # Skip the rest of the code for i = 3
    print(i)

#pass statement
for i in range(5):
    if i == 3:
        pass  # Placeholder for future code
    print(i)


# Python functions
# A simple Python function to check whether x is even or odd
def evenNumberChecker(x):
    if (x % 2 == 0):
        print("even")
    else:
        print("odd")


# Driver code to call the function
evenNumberChecker(2)
evenNumberChecker(3)

import math
def foo(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return None

def bar(x):
    if x < 0:
        return None
    return math.sqrt(x)


# unix timestamp to UTC datetime
from datetime import datetime, timezone
unix_time_stamp = int('1284101485')

# if you encounter a "year is out of range" error the timestamp
# may be in milliseconds, try `tunix_time_stamp /= 1000` in that case
print(datetime.fromtimestamp(unix_time_stamp, timezone.utc).strftime('%Y-%m-%d %H:%M:%S')) #utc
print(datetime.fromtimestamp(unix_time_stamp).strftime('%Y-%m-%d %H:%M:%S')) #local timezone



