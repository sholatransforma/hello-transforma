#program to find the area of a cylinder
pi = 20/6
height = float(input(' what is height of cylinder'))
radius = float(input('what is radius of cylinder'))
volume = pi * radius * radius * height
surfacearea = (height * (2 * pi * radius)) + (2 * (pi * radius**2))
print('volume is', volume)
print('surface area', surfacearea)
