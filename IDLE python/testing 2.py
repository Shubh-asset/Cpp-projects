Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
python
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    python
NameError: name 'python' is not defined
n = 300
n
300
x,y,z=10,20,30
x,y,z=z,y,x
printf(x,y,z)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    printf(x,y,z)
NameError: name 'printf' is not defined. Did you mean: 'print'?
print(x,y,z)
30 20 10
x=int("123")
y=int(-456.6)
z=int(7.9)
print(x,y,z)
123 -456 7
print(x,\n,y,\n,z)
SyntaxError: unexpected character after line continuation character
x=complex(2,4)
print(x)
(2+4j)
y=complex(7,2)
print(y)
(7+2j)
print(x+y)
(9+6j)
m1='hello'
m2='shubh'
msg = m1+","+m2+","
print(msg)
hello,shubh,
msg = m1+","+m2+"!"
print(msg)
hello,shubh!

repeat = "*"*10
print(repeat)
**********
string="hello, World"
print(string[0])
h
print(string[-1])
d
print(string[2:5])
llo
print(string[:5])
hello
print(string[6:])
 World
print(string[0:-1])
hello, Worl
print(string[0:-2])
hello, Wor
print(string[0:0])

2>3
False
4<7
True
'hello'=='goodbye'
False
true and false
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    true and false
NameError: name 'true' is not defined. Did you mean: 'True'?
True and False
False
True or False
True
x=20
if(x>5)
SyntaxError: expected ':'
if x>5:
    print("it is greater than 5")
print("not greater")
SyntaxError: invalid syntax
if x>5:
    print("it is greater than 5")

    
it is greater than 5
a=[1,2,3,4]
print(a[1:2])
[2]
print(a[1:3])
[2, 3]
print(a[1:5])
[2, 3, 4]
a=[1,2,3,4,5,6]
print(a[1:6])
[2, 3, 4, 5, 6]
t=(1,'a',3.14)
print(t)
(1, 'a', 3.14)
print(t[1:])
('a', 3.14)
t*2
(1, 'a', 3.14, 1, 'a', 3.14)
t+[7,8]
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    t+[7,8]
TypeError: can only concatenate tuple (not "list") to tuple
>>> t+(6,7)
(1, 'a', 3.14, 6, 7)
>>> fruit=('apple','banana')
>>> print(type(fruit))
<class 'tuple'>
>>> fruit={'apple','banana'}
>>> print(type(fruit))
<class 'set'>
>>> fruit.add('oil')
>>> print(fruit)
{'apple', 'banana', 'oil'}
>>> fruit.remove('banana')
>>> print(fruit)
{'apple', 'oil'}
>>> 
>>> a1={1,2,3,4}
>>> a2={5,3,4,7,8}
>>> intersection = a1&a2
>>> print(intersection)
{3, 4}
>>> union = a1 | a2
>>> print(union)
{1, 2, 3, 4, 5, 7, 8}
>>> 
>>> my_dict = {'a':1,'b':3,'c':67}
>>> print(my_dict)
{'a': 1, 'b': 3, 'c': 67}
>>> print(my_dict['a'])
1
>>> print(my_dict['c'])
67
>>> print(my_dict['v'])
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    print(my_dict['v'])
KeyError: 'v'
