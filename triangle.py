'''program to find the area of a triangle
calculate the perimeter
calculate the semi perimeter
calculate the area'''

a = float(input('what is the side a of the triangle'))
b = float(input('what is side b of the triangle'))
c = float(input('what is side c of the triangle'))
perimeter = a + b + c
s = (a + b + c) / 2
area = (s*(s - a) * (s - b) * (s - c))** 0.5
print(' the semi perimeter of the triangle is %0.2f' %s)
print('the area of the triangle is %0.2f' %area)
print('the perimeter of the triangle is %0.2f' %perimeter)
