import math
#ex 1
deg = int(input('Input degree: '))
print('Output radian: ', format(math.radians(deg) , '.5f'))

#ex 2
height = int(input('Height: '))
base1 = int(input('Base, first value: '))
base2 = int(input('Base, second value: '))
area = ((base1 + base2)/2)*5
print('area of trapezoid is: ', area)

#ex 3
def calculate_area_polygon(n, l):
    area_of_polygon =(n*l**2)/(4*math.tan(math.pi/n))
    return area_of_polygon

num_of_sides = int(input('Input number of sides: '))
length_of_side = int(input('Input the length of a side: '))
print(format(calculate_area_polygon(num_of_sides, length_of_side), '.2f'))


#ex 4
length_p = int(input('Length of base: '))
height_p = int(input('Height of parallelogram: : '))
area_p = length_p*height_p
print('area of paralelogramm is: ', area_p)