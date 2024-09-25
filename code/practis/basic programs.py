##---> take 2 int input from user and disp the sum and product of thr two value
a=int(input('Enter first nymber : '))
b=int(input('Enter second number :'))
print(f'sum of {a} and {b} is',a+b,'prodect is',a*b)


##---> take anumber frm user and display the sqr of the numbers
a=int(input('enter the number :'))
print(f'square of {a} is {a**2}')


##--->  the cube of input numbers
a=int(input("enter a number : "))
print(f"cube of {a} is {a**3}")


##---> find area of circle
b=float(input('enter the radius'))
print(f'radiyus of circle is {3.14*b**2}')


##---> find the area of triangle
c=int(input('enter the breath :'))
d=int(input('enter the height :'))
print(f'area of tringle is : {0.5*c*d}')


##---> find the square root of a number
e=int(input('enthe the number ;'))
print(f'the root is {e**0.5}')


##---> find the last digit of a number  input by the user
f=int(input(' enter a number :'))
print(f'the last digit is {f%10}')


##---> create a qudratic equation solver?
a=int(input('enter a value: '))
b=int(input('entrer a second value: ' ))
c=int(input('enter thred number: '))
d=(b**2-4*a*c)**0.5
x1=(-b+d)/(2*a)
x2=(-b-d)/(2*a)
print('x1=',x1,'x2=',x2)