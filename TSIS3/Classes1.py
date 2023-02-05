"""
1)class InputOutString(object):
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input()

    def printString(self):
        print(self.s.upper())


stObj = InputOutString()
stObj.getString()
stObj.printString()

2)a = int(input())

class Shape():
    def __init__(self):
        pass
    def area(self):
        return 0
class Square(Shape):
    def __init__(self, lenght):

        self.lenght = lenght
    def area(self):
        return self.lenght * self.lenght

sq = Square(a)
sh = Shape()
print( "Area of square:", sq.area())
print( "Area of shape:", sh.area())

3)a = int(input())
b = int(input())

class Shape():
    def __init__(self):
        pass
    def area(self):
        return 0

class Rectangle(Shape):

    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width
    def area(self):
        return self.lenght * self.width

rec = Rectangle(a,b)

print("Area of rectangle:", rec.area())

4)import math


a, b = int(input()), int(input())

c, d = int(input()), int(input())

class Point():
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def show(self):
        print("Point({}, {})".format(self.x, self.y))
    def move(self, x, y):
        self.x += x
        self.y += y

    def distt(self, x1, y1):
        return math.sqrt((self.x - x1) ** 2 + (self.y - y1) ** 2)

cl = Point(a,b)

cl.show()



print("Distance between the two points", cl.distt(c,d))

5)a = input()
b = int(input())

class Account:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance
    def deposite(self, sum):
        self.balance += sum
        print( "Balance", self.balance)
    def withdraw(self, sum):
        if sum > self.balance:
            print("Withdrawal declined, insufficient funds")
        else:
            self.balance -= sum
            print( "New balance", self.balance)

acc = Account(a,b)

acc.deposite(500)
acc.withdraw(2000)
acc.withdraw(300)


6)numbers = list(map(int, input("Enter a list of numbers, separated by space: ").split()))

result = list(filter(lambda x: all(x % i != 0 for i in range(2, x)), numbers))

print("Prime numbers in the list: ", result)
"""


