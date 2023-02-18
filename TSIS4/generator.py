"""
def square(N):
    for i in range(0,N):
        yield i**2
for g in square(int(input())):
 print(g)


def even_numbers(n):
    for i in range(0, n+1, 2):
        yield str(i)

n = int(input())
even_number = even_numbers(n)
result = ','.join(even_number)
print(result)


def divisible(n):
    for i in range(0,n+1):
        if i%3==0 and i%4==0:
            yield i
n=int(input())
for a in divisible(n):
 print(a)

def f():
    return range(a,b)

def square():
    for i in range(a,b+1):
        yield i**2
a=int(input())
b=int(input())
for g in square():
 print(g)
#print(next(g))
#print(next(g))

def decreasing(c):
    for i in range(c,0,-1):
        yield i
c=int(input())
for a in decreasing(c):
 print(a)
"""

