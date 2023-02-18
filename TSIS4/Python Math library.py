"""
1)import math
degree=int(input())
x=(math.pi*degree)/180
print(x)


def radian(degree):
    radian=(math.pi*degree)/180
    print(radian)
radian(degree=int(input()))


2)import math
a=int(input('Height: '))
b=int(input('Base,first value: '))
c=int(input('Base,second value: '))
Area_t=((b+c)/2*a)
print(Area_t)

def Area_T(a,b,c):
    Area_T=((b+c)/2)*a
    print(Area_T)
a=int(input('Height:'))
b=int(input('Base,first value:'))
c=int(input('Base,second value:'))
Area_T(a,b,c)

3)import math
a=int(input('Input number of sides: '))
b=int(input('Input the length of a side: '))
A_p = (a * pow(b,2)) / (4 * (math.tan(math.pi/a)))
print('The area of the polygon is: ',math.floor(A_p))

4)import math
a=int(input('Length of base: '))
b=int(input('Height of parallelogram: '))
Area_Par=a*b
print('Expected Output: ',Area_Par)

def calculate_parallelogram_area(base, height):
    area = base * height
    return area

base = float(input('Length of base: '))
height = float(input('Height of parallelogram: '))

Area_Par = calculate_parallelogram_area(base, height)
print('The area of the parallelogram is:', Area_Par)
"""