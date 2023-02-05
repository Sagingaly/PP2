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
2)
from math import *
class Shape:
  def init(self):
    pass
  def area(self):
    return 0
class Square(Shape):
  def init(self):
    n = int(input())
    Shape.init(self)
    self.length = n
  def area(self):
    return self.length * self.length
aSquare = Square()
print(aSquare.area())

3)
class Rectangle():
  def init(self):
    length = float(input())
    width = float(input())
    self.length = length
    self.width = width
  def area(self):
    print(self.length * self.width)
nRectangle = Rectangle()
nRectangle.area()

4)
from math import *
class Point():
  def init(self):
    a = float(input())
    b = float(input())
    pta = int(input())
    ptb = int(input())
    self.pta = pta
    self.ptb = ptb
    self.a = a
    self.b = b
  def show(self):
    print(self.a, self.b)
  def move(self):
    self.a += self.a
    self.b += self.b
    print(self.a, self.b)
  def dist(self):
    da = self.pta - self.a
    db = self.ptb - self.b
    print(sqrt(da  2 + db  2))
nPoi = Point()
nPoi.show()
nPoi.move()
nPoi.dist()

5)
class Account:
  def init(self):
    self.balance = 0
  def deposit(self):
    deposit = float(input())
    self.balance += deposit
    print(deposit)
  def withdraw(self):
    summa = float(input())
    if self.balance >= summa:
      self.balance -= summa
      print(summa)
    else:
      print("Insufficient balance")
  def display(self):
    print("\n Net Available Balance=", self.balance)
a = Account()
a.deposit()
a.withdraw()
a.display()


6)numbers = list(map(int, input("Enter a list of numbers, separated by space: ").split()))

result = list(filter(lambda x: all(x % i != 0 for i in range(2, x)), numbers))

print("Prime numbers in the list: ", result)
"""





