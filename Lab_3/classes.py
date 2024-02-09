#ex 1
class Firstclass():
    def getString(self):
        return str(input())
        
    def printString(self, string):
        print(string.upper())

s = Firstclass()
input_string = s.getString()
s.printString(input_string)

#ex 2
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length
    
    def area(self):
        return self.length ** 2
f = Shape()
print(f.area())
g = Square(int(input()))
print(g.area())

#ex 3
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
d = Rectangle(int(input()), int(input()))
print(d.area())

#ex 4
import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print('coordinates of point ({},{})' .format(self.x, self.y))

    def move(self, newx, newy):
        self.x = newx
        self.y = newy

    def dist(self, sheesh_another_point):
        dis = self.x - sheesh_another_point.x
        dis2 = self.y - sheesh_another_point.y
        print(math.sqrt(dis**2 + dis2**2))

point1 = Point(int(input()), int(input()))
point2 = Point(int(input()), int(input()))
point1.show()
point1.move(int(input()), int(input()))
point1.dist(point2)


#ex 5
class Accaunt():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        print(self.owner, self.balance)

    def deposit(self, insum):
        self.balance += insum
        print('{} your balance now is: '.format(self.owner), self.balance)

    def withdraw(self, summ):
        if self.balance - summ < 0:
            print('{}: insufficient funds'.format(self.owner))
        else:
            self.balance -= summ
            print(f'{self.owner} your balance now is: {self.balance}')

first_account = Accaunt(str(input('Enter your name: ')), int(input('Enter your balance: ')))
quest = str(input('Deposit - \'D\' \ Withdraw - \'W\': ')).upper()

p = 'Y'
while p == 'Y':
    if quest == 'D':
        first_account.deposit(int(input()))
    elif quest == 'W':
        first_account.withdraw(int(input()))
    else:
        print('No such operation')
    p = str(input('Do you whant to continue? Y/N: ')).upper()
    if p == 'Y':
        quest =  str(input('Deposit - \'D\' \ Withdraw - \'W\': ')).upper()
else:
    print('Thank you for using of our program!')

#ex 6
def filt(num):
    if num <= 1:
        return False
    sheesh = 1
    for i in range(2, num):
        
        if num % i == 0:
            sheesh = 0
            break
    if sheesh == 1:
        return num
            
numbers = [int(x) for x in input().split()]
prime_list = list(filter(lambda s: filt(s), numbers))
print(prime_list)