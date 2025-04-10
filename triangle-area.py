#Python program to find area of triangle
a=float(input('Enter the First Side:'))
b=float(input('Enter the Second Side:'))
c=float(input('Enter the Third Side:'))

#Semi-Perimeter of triangle
S= (a+b+c)/2

#Now for area of triangle
area = (S*(S-a)*(S-b)*(S-c))**0.5

print('The area of traingle is %f'%area)
