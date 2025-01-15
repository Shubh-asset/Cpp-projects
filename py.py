'''print(list(enumerate(['a', 'b', 'd'])))'''

'''name = input("Your name?\n")
print("hello "+name+"!")'''

'''print("2+2=",2+2)'''

'''n = 300
print(n)'''

'''x,y='hi'
print(x," ")
print(y)'''

'''
import math
root = math.sqrt(25)
print(root)

from math import sqrt
x = sqrt(25)
print(x)

x=5
y=3
z=x==y
print(z)

x=12
x<<=1
print(x)

x=5
y=5
if not(x==y):
    print("x is not equal to y")
else:
    print("x is equal to y")
    
x=5
y=4
print((x<6 and y>5)or(x<10 and y<10))

print(bin(x|y))
print(bin(x))
x<<=1 #it multiplies the number with 2^n
print(bin(x))
print(x)
print("y=",bin(y))
y>>=1
print(bin(y))
print(y)
'''
'''
x=[1,2,3]
y=[4,5,6]
z=x
print(x is z)
print(x is not z)

x=[1,2,3]
y=[1,2,3]
print(x == y)
#it check for object identity not object equality i.e. values
print(x is y)'''
'''
i=0
while i<10:
    if i==5:
        break
    print(i)
    i+=1
    
print("\n")'''

# i = 0
# while True:
#     i+=1
#     if i%2==0:
#         continue
#     print(i)
#     if i==10:
#         break
    
# Initialize variables
# sum = 0
# number = 1
# # Ask the user to enter numbers
# while number != 0:
#     number = int(input("Enter a number (0 to quit): "))
#     sum = sum + number
# # Print the result
# print("The sum of the numbers is", sum)
'''
i = 0
while i<10:
    print(i)
    i+=1
    if i==5:
        break
else:
    print("done")'''
    
# for i in range(0,10,2):
#     print(i)
    
# for i in range(5):
#     print("hello")

import math
'''
x = math.radians(30)
y = math.floor(x)
print(y)

z = math.sin(x)
print("sin(30) = ",z)

my_list=[1,2,3,4,5]
for i in my_list:
    print(i)
    
i = 0
while i<len(my_list):
    print(my_list[i])
    i+=1'''
    
'''nested_list = [[1,2,3],[4,5,6],[7,8,9]]
for sublist in nested_list:
   # for item in sublist:
        print(sublist)'''
        
'''def traverse(list):
    for element in list:
        if type(element) == list:
            traverse(element)
        else:
            print(element)
nested_list = [[1,2,3],[4,5,6],[7,8,9]]

traverse(nested_list)'''
'''
my_list=[1,2,3,4,5,6]
my_list[2] = 67
my_list.append(22)
my_list.insert(2,111)
my_list.extend([9,7,6])
my_list = my_list+[44,55,66]
my_list.remove(111)
my_list.pop(2)
my_list.sort()
my_list.reverse()
my_list.copy()
min(my_list)
print(my_list)
print(len(my_list))
print(max(my_list))
print(min(my_list))
print(sum(my_list))
print(sorted(my_list))
print(enumerate(my_list))'''

'''my_tuple = ("apple")
print(my_tuple)
my_list = [1,2,3]
my_tuple2 = tuple(my_list)
print(my_tuple2)'''
# my_list2 = [4,5,6]
# my_tuple3 = *my_list2
# print(my_tuple3)

# unp_tuple = (1,2,3,4,5,6,7)

#a,b,c = (1,2,3)
#print(a)
# print(enumerate(unp_tuple))
'''
print("\n")
for i in unp_tuple:
    print(i)
    
print("\n")
for i in range(len(unp_tuple)):
    print(unp_tuple[i])
    
print("\n")
for i,j in enumerate(unp_tuple):
    print(i,j)
    
print("\n")
[print(i) for i in unp_tuple]
'''
# slice_tuple = unp_tuple[-6:-2]
# print(unp_tuple[-2:-6])
# print(slice_tuple)
'''
my_tuple = [1,2,3,4]

new_tuple = list(my_tuple)
new_tuple[1] = 10
new_tuple = tuple(new_tuple)

my_tuple = new_tuple
print(my_tuple)

del new_tuple
print(new_tuple)'''

'''
tuple_t = ((1,2,3),(4,5,6))
a = [1,2,3]
#b= [4,5,6]
b = tuple_t[1]

#tuple_t[1] = (3,4,5) #will not change cause its a tuple

print(b)
'''
'''
#set1 = {1,2,3}
# or
set1 = set([1,2,3])
set2 = {3,4,5}
# intersection | difference | union
print(set1.intersection(set2))
print(set1&(set2))

# add|update, remove|discard
'''
'''
    #function
numbers = {1,2,3,4,5,6}

if all(x>0 for x in numbers):
    print("all are positive")

if any(x>3 for x in numbers):
    print("numbers greater than 3 are here")

print("The elements are", len(numbers),"in numbers")'''

#frozen sets
'''
fruits = frozenset(['apple', 'banana'])
print(fruits)

fruits.add('yellow')'''
'''
dict = {"name":"john", "age":20, "city": "pkl"}

#person = dict("name":"john", "age":20, "city": "pkl")

#myvalue = dict["name"]
myvalue = dict.get["name"]
print(myvalue

del dict["name"]
print(dict)
'''

'''
x= 1.2
y = 34

s1 = str(x)
s2 = str(y)

print(s1)

s3 = """this is a multiline 
string"""

print(s3)
# string interpolation
name = "shubh"
age = 21

s4 = f"my name is {name} and age is {age}"
print(s4)

# using bytes and bytearray

s5 = b'hello'
s6 = bytearray(b'hello')
print(s5)
print(s6)

s7 = "hello here you are"
for i in s7:
    print(i)
'''


#string functions
'''
s = "hello, world"
new_s = s.replace("world", "python")
print(new_s)
'''

#concatenation
'''
s1 = "here"
s2 = "you here"

print(s1+" "+s2+"!")

s3 = "Python"
s4 = "python"

print(s3 == s4)
print(s3 != s4)
print(s3 >= s4)
print(s3 <= s4)
print(s3 > s4)
print(s3 < s4)
'''

#functions
'''
def add_no(a,b):
    return a+b

result = add_no(3,4)
print(result)'''

#with no argument
'''
def greet():
    print("hello")

greet()'''

#with argument
'''
def greet(name):
    print(f"hello {name}!")
    
greet("Shubh")
'''

#arbitrary length arguments
'''
def add_no(*no):
    result = 0
    for i in no:
        result += i
    return result

numbers = add_no(1,2,3,4,5)
print(numbers)
'''

#default arguments
'''
def info_m(name, age=20):
    print(f"name is {name} and age is {age}")   
    
info_m("Shubh")
'''

#Lambda functions
'''
addition = lambda x,y,z:x+y+z
print(addition(2,3,4))
'''

#recursive function
'''
def recursive(n):
    if n== 0:
        return 1
    else:
        return n*recursive(n-1)

print(recursive(1))
'''

#modules
'''
import sqrt
print(sqrt.sqqrt(25))
'''

'''
def validate_age(age):
    if age < 0:
        raise InvalidAgeError("Age cannot be negative.")
    elif age > 150:
        raise InvalidAgeError("Age cannot be greater than 150.")
    else:
        print("Age is valid.")
    try:
        validate_age(-5)
    except InvalidAgeError as e:
        print(e)
'''

#File handling
'''
file_object = open("hello.txt", "r")
print(file_object.read())
#file_object.close()
'''

#renaming a file
# '''
# import os
# '''os.rename("hello.txt", "newone.txt")'''
# #working directory
# '''crt_dir = os.getcwd()
# print(crt_dir)
# os.rmdir("F:\Course\dummydir")'''
# #listing dir
# '''list_dir = os.listdir("F:\Course")
# print(list_dir)'''
# #classes

# class Car:
#     def _init_(self,make,model,year):
#         self.make = make
#         self.model = model
#         self.year = year
#     def honk(self):
#         print("beep beep")
# my_car = Car("toyota","corolla",2019)   #object of class Car

# print(my_car.make)
# print(my_car.model)
# print(my_car.year)

# my_car.honk()

# '''

#docstring
# '''
# def add(a,b):
#     '''
#     this function adds two numbers
#     parameters:
#     a(int) = first number
#     b(int) = second number
    
#     returns:
#     int: the sum of a and b
#     '''
#     help(add)
#     return a+b'''

#variable

# var = 21.09
# print(var)
# var = "hello"
# print(var)

#loops
'''
sum = 0
number = 1

while number !=0:
    number = int(input("Enter a number(0 to quit): "))
    sum = sum+number
    
print(sum)
'''
'''
def largest_num(numbers):
    if not numbers:
        return None
    largest = numbers[0]
    for num in numbers:
        if num>largest:
            largest = num
    return largest

numbers = [1,2,3,4,5]
largest_nmm = largest_num(numbers)

if largest_num is not None:
    print("The largest number is", largest_num)
else:
    print("The list is empty")  
    '''
'''
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def honk(self):
        print("Beep beep!")
        
# Create an object of the Car class
my_car = Car("Toyota", "Camry", 2020)

# Access attributes of the object
print(my_car.make)
print(my_car.model)
print(my_car.year)
# Call a method
'''
'''
def rec_func(n):
    if n == 0 or n==1:
        return 1
    else:
        return n*rec_func(n-1)
    
number = 5
result = rec_func(number)
if number<0:
    Print("enter valid integer")
else:
    print("The factorial of {number} is {rec_func(result)}")
    '''
# for i in range(10):
#     pass

# i = 0 
# while i<10:
#     i+=1
#     pass

# s = 'hello, world'
# for i in s:
    
#     print(i)
    
# i = 0
# while i < len(s):
#     print(s[i])
#     i+=1
'''
f1 = float(input("Enter the first number: "))
f2 = float(input("Enter the second number: "))

summ = f1+f2

int_result = int(summ)

print(f"sum of {f1} and {f2} is {summ}")
print(f"result in integer is {int_result}")'''

import sys
print(sys.path)