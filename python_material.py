import math
import time
import random

'''
long comment
'''
# comment 54

#strings
strd = ("hello"*3)
print(strd)
print(type(strd))

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

dish = str(input("what is your fav food? "))
print ("I like " + dish + " too")
print(dish[2])
print(dish[0::1])
sli = slice(2, 4)
print(dish[sli])
a = len(dish)
cou = dish.count('z')
o = dish.find('o')
t = dish.capitalize()
dish.upper()
dish.lower()

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

age = 36
txt = "My name is John, and I am {}" #вставит число на место {} но только один раз, если будет несколько скобок то выдаст ошибку
print(txt.format(age))
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price)) 


print(dish.isdigit())
print(dish.isalpha())
dish.replace('z', 's') #replace all 'z' to 's'
for x in "banana":
  print(x)
txt = "The best things in life are free!"
print("free" in txt)
txt = "The best things in life are free!"
print("expensive" not in txt)

number = int(input())
x, y, z = 1, 2, 3
fl = 2.03
r = pow(number, 3)
d = math.sqrt(number)
b = abs(number)
f = max(x, y, z)
v = min(x, y, z)
w = round.fl
e = math.ceil.fl
r = math.floor.fl




print('lol' + 5)


sd = int(input())
if sd >= 2:
    print('lol')
elif sd == 1 and sd >0 or sd == -1:
    print('nah')
else:
    print('sheesh')

while sd <=0:
    print('nope')
    time.sleep(1)
    sd = sd + 1

for i in range(3, 7 + 1):
    print(i, 'cook')
for i in range(dish):
    print(i)


x = "awesome"
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)


def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)

"""
Text Type:	str

Numeric Types:	int, float, complex(example x = 1j)

Sequence Types:	list, tuple, range(example x = range(6))

Mapping Type:	dict(example x = {"name" : "John", "age" : 36})

Set Types:	set(example x = {"apple", "banana", "cherry"}), frozenset(example x = frozenset({"apple", "banana", "cherry"}))

Boolean Type:	bool

Binary Types:	bytes(example x = b"Hello"), bytearray(example x = bytearray(5)), memoryview(example x = memoryview(bytes(5)))

None Type:	NoneType
"""
spisoc = ['food', 'car', 'phone'] #list
soc = ('food', 'car', 'phone') #tuple

#Setting the Specific Data Type
'''
x = str("Hello World")	str	
x = int(20)	int	
x = float(20.5)	float	
x = complex(1j)	complex	-always with j, no other letters-
x = list(("apple", "banana", "cherry"))	list	
x = tuple(("apple", "banana", "cherry"))	tuple	
x = range(6)	range	
x = dict(name="John", age=36)	dict	
x = set(("apple", "banana", "cherry"))	set	
x = frozenset(("apple", "banana", "cherry"))	frozenset	
x = bool(5)	bool	
x = bytes(5)	bytes	
x = bytearray(5)	bytearray	
x = memoryview(bytes(5))	memoryview
'''

#смена типа данных
t = 5
t = float(t)

print(random.randrange(1, 10 + 1))

#Escape Characters
'''
\'	Single Quote	
\\	Backslash	
\n	New Line	
\r	Carriage Return	
\t	Tab	
\b	Backspace	
\f	Form Feed	
\ooo	Octal value	
\xhh	Hex value
'''