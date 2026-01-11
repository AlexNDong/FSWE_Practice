first_var = 123123123
second_var = 1412424123
# print(first_var + second_var)

# To check if two variables are in the same memory space of RAM
a = 18
b = a
print(f"First value of variable a = {a}")
print(f"First value of variable b = {b}")
print(f"Location memory of a {id(a)}")
print(f"Location memory of b {id(b)}")
# The result shows that they are in the same location of the memory
c = 20
print(f"First value of variable c = {c}")
print(f"Location memory of c {id(c)}")
# The created c variable is in different location
d = 28
print(f"First value of variable d = {d}")
print(f"Location memory of d {id(d)}")
# As I created d with the same value of 18 -> variable d, b, and a will point to the same location
a += 10
print(f"New value of a + 10 = {a}")
print(f"Value of b = {b}")
# variable a has been updated to 10 + 18 = 28, while variable b is still 18
print(f"New location memory of a {id(a)}")
# What intesresting is that now the variable a = 28 = variable d = 28 (the two variables point to the same location)
print(f"Location memory of b {id(b)}")
# As b = 18 (still take the memory of previous one), while a takes the new location

print("THIS IS MUTABLE & IMMUTABLE variables of PYTHON")
print("Intergers, Tuples, Strings are IMMUTABLE")
print("if variable a = 18 created, it place in memmory @location X, then if a + 1 = 19, it place in memory @location Y")
print("if new variable is created b = 18, it plcae in the same memory @location X")

print("MUTABLE VARIABLES IN PYTHON")
list_a = [1,2,3,4,5]
print(f"List a = {list_a}")
print(f"ID of list_a = {id(list_a)}")
list_b = list_a
list_d = list_a.copy()
list_c = [1,2,3,4,5]
print(f"List b = {list_b}")
print(f"ID of list_b = {id(list_b)}")
print(f"List c = {list_c}")
print(f"ID of list_c = {id(list_c)}")
print(f"List d = {list_c}")
print(f"ID of list_d = {id(list_d)}")
# Eventhough list_c is the collection of the same number, but it points to diferent location memmory
# Update list a
list_a[0] = 10
print(f"List a = {list_a}")
print(f"ID of list_a = {id(list_a)}")
print(f"List b = {list_b}")
print(f"ID of list_b = {id(list_b)}")
print(f"List d = {list_d}")
print(f"ID of list_d = {id(list_d)}")
list_a.append(100)
print(f"List a = {list_a}")
print(f"ID of list_a = {id(list_a)}")
print(f"List b = {list_b}")
print(f"ID of list_b = {id(list_b)}")
# Update list b to see if list a will change
list_b[-1] = 200
print(f"List a = {list_a}")
print(f"ID of list_a = {id(list_a)}")
print(f"List b = {list_b}")
print(f"ID of list_b = {id(list_b)}")
# As list_a has been updated, it takes a new value of first index
# BUT, list_a still take the same memmory location
# list_b is updated accordingly, and still take the same location
# As we used copy() function for list_d, it takes the same value, but created a new memmory location,
# Then, once we updated list_a, list b = list a (so it will change value, but still keep location with list_a)
# but once we updated list_a, list_d = list_a.copy(), the value is not changed, 
# BEST PRACTICE: if we want to copy a mutable variable -> use .copy() method
print("In summary, IMMUTABLE refers values, variables are pointed to values, if value change, location will change")
print("Then, mutalbe refers variables, variables are pointed to values, if values change, location will not change")


### STRING ### - IMMUTABLE
str_a = "HELLO VIETNAM"
str_b = "HELLO FRANCE"
print(str_a + " " + str_b)
print(str_a * 3)
print("hello" in str_a.lower())
print(f"Hello {str_a}") # format string
str_fruits = "apple;banana;cherry"
print(str_fruits.split(";")) # string splitting
str_name = " DONG NHAT THIEN  "
str_list = [word.capitalize() for word in str_name.strip().lower().split()] # list comprehension [f(i) for i in list_i]
print(str_list)
print(" ".join(str_list)) # Joining a list of string together, each element is concatinated with " " (spacing)

### COLLECTION ### (IMMUTABLE AND MUTABLE)
# List, Set, Dict (mutable)
# Tuple (immutable)

# List []: remain order, can be added, removed (mutable), change item
list_a = [1,2,3,1,10,1,4,5,9,4]
print(list_a)
list_a.append("hello")
print(list_a)
list_a.remove("hello")
print(list_a)
list_a[0] = 100
print(list_a)

# Note: Shallow Copy and Deepcopy
print("Shallow copy")
list_a = [1,2,3,4]
list_b = list_a.copy() # SHALLOW COPY
print(list_a)
print(list_b)
list_a[0] = 100
print(list_a)
print(list_b)
list_b[0] = 200
print(list_a)
print(list_b)
#### The .copy() function works once in single list (shallow copy)
list_1 = [[1,2], [3,4]]
list_2 = list_1.copy()
print(id(list_1))
print(id(list_2))
list_1[0][0] = 100
print(list_1)
print(list_2)
print(id(list_1))
print(id(list_2))
#### The .copy() create another address, but did not work for nested list. Two list1 and list2 are in different location
#### shallow copy (.copy()) does not work with nested list (more dimension)
print("End Shallow Copy")
### DEEPCOPY
print("Deepcopy")
import copy
list_1 = [[1,2], [3,4]]
list_2 = copy.deepcopy(list_1)
list_1[0][0] = 100
print(list_1)
print(list_2)

# Set {}: unique elements, is ordered in ascending, can be added, removed (mutable)
list_a = [1,2,3,1,10,1,4,5,9,4]
print(list_a)
print(set(list_a)) # the set will remove duplicates, and sort it in ascending order

# Tuple (): cannot be changed, can be not unique elements, keep order, can only be indexed
print(tuple(list_a))
# The size of tuple is fixed, then once it is created, python will assiged a fixed amount of memory for that tuple
# In performance memmory, tuple is more optimized than list or set (mutable)

# DICTIONARY {key:value} - mutable - dict is HASH TABLE (with key must be hasable)
# Note: distingush set and dict
dict_1 = {1,2}
print(type(dict_1))

students = {"name": "Alex", "age":18, "school":"IFP"}
# dict.keys()/print all keys, dict.values()/print all values, dict.items()/print all items, dict/print keys
for key in students.keys():
    print(key)

# keys named cannot be mutable value (code below does not work as key is mutable [1,2,3])
# mutable_dict1 = {[1,2,3]:"ddf", "dfd":[1,2,3], 1:2, True:False}
# print(mutable_dict1)
# Note in dict: immutalbe = hasable, mutable = unhasable <HASH FUNCTION>
# To check if it is hasable
list1 = [1,2,3]
var_a = 10
tuple1= (1,2,3)
#print(f"List is {hash(list1)}") -> this is unhasable -> ERROR
print(f"Interger is {hash(var_a)}") 
print(hash(tuple1))

def process_command_ifelse(command):
    if command == "start":
        return "Starting the system ---"
    # ...
    else:
        return "Unknow commands"
# The if-else statement is not optimized, as they need to go through all conditions
# it can be improved by using dict as below
def process_command_dict(command):
    commads ={
        "start": "Starting the system ---",
        "stop": "Stopping the system ---",
        "restart": "Restarting the system ---",
        "status": "System is running",
        "help": "Available commands: start, stop, restart, status, help"
    }
    return commads.get(command, "Unknown command") 
"""
The get() method of dictionary .get(key, alternative). It will return the value of the specify "key", 
then if the "key" does not exist in dict, it will return the alternative value
"""
print(process_command_dict(command="fsfsdf"))
# Hash table of dictionary is generally fast -> more computational optimized
# KEY note: Perfer HASH TABLE (DICT) over CONDITIONAL (If, elif, else)


### LOOPING ### FOR / WHILE
for i in range(10): # [0:5] -> [0:5) from 0 (inclusive) to 5 (exclusive)
    print(i)

students = ["Alice", "Thien", "Aka"]
for index, value in enumerate(students):
    print(f"Student {index+1}: {value}")

# Break & Continue

# for num in range(1,11):
#     if num == 5:
#         break # Go out of the looping if condition met
#     print(num)

# for num in range(1,11):
#     if num %2 == 0:
#         continue # Go the next iterable value if condition met (ignore the below)
#     print(num)

## WHILE - how to check active error during while, using pdb, pdb.set_trace(), exit: Ctrl + D
count = 0
while count <= 10:
    print(count)
    count += 1
    # import pdb; pdb.set_trace()

## More performance with list comprehension in for loop
# Way 1. Append
squares = []
for i in range(1000):
    squares.append(i**2)
# Way 2. List comprehension
squares = [i**2 for i in range(1000)]
# Why way2 is faster ?
# In way 1, when we create a list, Python Inpreter does not know "length of your list", then it may overuse the space of memmory for your list
# In way 2, when we create the list (with specify of range(1000)), Python will know the length {1000} of your list, then it uses an exact space in memory
# List comprehension is written with Cpython's c code -> low language level (faster)

### ITERABLE ITERATOR VS GENERATOR ###
# 1. Collection is iterable object: list, array, dict, set, tuple (store all elements in RAM) -> process is limited
# 2. INterator (having only one element at a time in RAM) more efficient -> can process unlimited 
## When working with data -> (generally large dataset) -> INterator is perfered
# Way 1. Looping over a list (already created)
lst1 = [i for i in range(10)]
for i in lst1: # List is interable collection
    print(i)
# Way 2. Looping over range (Q? Is range(10) a list already created with 10 elements like way 1)
for i in range(10): # Here is generator
    print(i)
# Answer: way 2 is faster as it is not looping over a list of 10 elements. It create one element, process, execute, and then the next element
# While way 1 using list will need to put the whole 10 element in RAM, looping through each element, process and execute

# # Example
# from random import normalvariate, randint
# from itertools import count
# from datetime import datetime

# def read_fake_data(filename):
#     """Generator create fake data"""
#     for timestamp in count():
#         if randint(0, 7*60*60*24-1) == 1:
#             value = normalvariate(0,1)
#         else:
#             value = 100
#         yield datetime.fromtimestamp(timestamp), value

### FUNCTION ###
## Local and Global: inside function, first, it looks for local, if not exist, it uses global

# Local and global variable - for Immutable variable
x = 10 # gobal variable, can be accessed inside another function
def demo(x):
    y = 5 # local variable, cannot be access outside the function, if it is local, must be assigned a value
    x +=100 # x takes value of 10, then plus 100 = 110
    return x + y, x # x now = 110 + (y=5) = 115, x = 110

print(demo(x)) # x takes 10 (global)
print(x) # x still be 10 (inside function cannot change global variable) - X is immutable

x = 10
def demo():
    y = 5
    return x+10, y
print(demo())

# Local and global variable - for Mutable variable
list_x = [1,2,3]
def demo_mutable():
    list_x.append(100) # list_x = [1,2,3], then append(100) = [1,2,3,100]
    # Note: list.append(x) is in-place mutation
    list_y = list_x.append(1000)
    # Note: list.append(X) return in None
    return list_x, list_y # return [1,2,3,100,1000] for list_x, list_y = NONe

print(demo_mutable())
print(list_x) # the outside global variable also being changed to [1,2,3,100,1000] - list is mutable
## Immutable Variable: only changed inside the function
## Mutable Variables: after being changed inside, it also affects the outside global variables

## Scope: global local 
# x = 10 # global
# def demo():
#     x = x+10 # this is assigned statement -> treat as local (must be assiged a value before it is called)
#     return x
# print(demo())
## This code does not work
x = 10
def demo(x): # x is now a parameter
    x = x+ 10 # parameter assinged it to be 10
    return x
print(demo(x))
print(x)

x = 10
def demo():
    global x # Now we force x to be global (then it will be assgined 10)
    x += 10 # x = 10 + 10 = 20
    return x
print(demo()) # return x = 20
print(x) # x = 20 (as we force it inside the function), now it is 20

## PARAMETERS AND ARGUMENTS
def add(a,b): # a,b are parameters (variable in function deffinition)
    return a+b
print(add(2,10)) # 5, 10 are arguments (actual value passed when calling)
## DEFAULT VS REQUIRED PARAMETERS
def multiply(a,b): # a,b are required parameters (positional)
    return a*b 
print(multiply(10,20)) # must be specified when calling (positional argument)
print(multiply(b=10, a=100)) # keyword argument

def devide(a,b=10): # a is required parameter, b is default parameter
    return a/b
print(devide(100)) # only specify one as position argument, b is default (don't need to specify)

## *args / **kwargs
# *args: collect extra positional arguments (as tuple)
# **kwargs: collect extra keyword arguments (as dictionary)
def show_info(*args, **kwargs):
    print("Positional: ", args)
    print("Keyword:", kwargs)
print(show_info("Python", "3.10", author="Guide", year=1991))
# Required parameter (normally specified as positional arguments)
# Default parameter (normally specified as keyword arguments)

def demo_kw(a, *args, **kwargs): 
    print(a) # required parameter
    print(args) # positional args
    print(kwargs) # keyword args

demo_kw(1,2,3,4,5,x=10,y=100) # a takes 1, *args takes (1,2,3,4,5) as tuple, **kwargs takes {"x":10, "y":100} as dict

# Orders: required params (keyword or position), default params, *args, **kwargs

### FILE HANDLING IN PYTHON ###
# W1:
try: 
    file = open(file="temp.txt", mode="r")
    content = file.read()
    print(content)
    file.close() # we need to say close() so the file can close 
except:
    print("No such file end with .txt")
# W2:
try:
    with open(file="temp.txt", mode="r") as f:
        content = f.read() # we don't need to say close()
        print(content) 
except:
    print("No such file end .txt")
# Read each line
try:
    with open(file="temp.txt", mode="r") as f:
        lines = f.readlines()
        for line in lines:
            print(line)
except:
    print("No such file end .txt")
# Application: Having a folder of file involve: temp1.txt, temp2.txt, temp3.txt, tempn.txt
# Write a python to change the extension to .md
# Similar to using command "ls" to ls all files in current directory, we need "os" <operating system>
import os
folder_path = "." # "." is current folder where the python file is in.
# If all the files for example in another folder -> folder_path = "./text_files"
try:
    for filename in os.listdir(folder_path): # list all directory in the current folder
        if filename.endswith(".txt"):
            new_filename = filename.replace(".txt", ".md") # replace the string
            # Above is just get the name of the file, then change the name
            # To change name of the file, we need to interact with os
            old_file = os.path.join(folder_path, filename) 
            # folder path = ".", filename = "temp1.txt" -> "./temp.txt", join will provide you "/"
            new_file = os.path.join(folder_path, new_filename)
            # Still not change the file in the system yet
            os.rename(old_file, new_file)
except:
    print("No such file .txt")


### HANDLE ERROR ### TRY - EXCEPT
input = 0
try:
    result = 10/input
except:
    print("Not devide by 0")