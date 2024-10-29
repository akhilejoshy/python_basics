#Q find the largest number
a=int(input('enter 1st number:'))
b=int(input('enter 2nd number:'))
if(a>b):
    print(a,'is bigger one')
else:
    print(b,'is bigger one')


#Q1 check char is vowel or not
char=input('enter a character:')
vowel='a,e,i,o,u'
if(char in vowel):
    print(f'{char} is vowel')
else:
    print(f'{char} is not vowel')


#Q2 find the smallest of two number
a=int(input('enter 1st number:'))
b=int(input('enter 2nd number:'))
if(a>b):
    print(b,'is smallest')
else:
    print(a,'is smallest')


#Q3 check a number it even or odd
c=int(input('enter a number:'))
if(a%2==0):
    print(c,'is even')
else:
    print(c,'is odd')


#Q4 check a number input by user is +ve or -ve
d=int(input('enter a number:'))
if(d>0):
    print(d,'is +ve')
else:
    print(d,'is -ve')


#Q eligibility
name=input('Enter the name of candidate:')
age=int(input(f'Enter the age of {name}:'))
if(age>=18):
    print(name,' eligible for voting')
else:
    print(name,'is not eligible for voting')


#Q1 simple authentication user id: User,password:Pass out:Success
user=input('Enter the user id:')
password=input('Enter the password:')
if(password=='Pass' and user=='User'):
    print("Authentication success")
else:
    print('authentication decline')


#Q2 check a number div by 2 and 3
a=int(input('enter a number:'))
if(a%2==0 and a%3==0):
    print("the number is dividable by 3 and 2")
else:
    print('the number is not dividable by 2 and 3')


#Q check a number mull by 5
a=int(input("enter a numer:"))
if(a%5==0):
    print('this number is multiple by 5')
else:
    print('this number is not multiple by 5')


#Q check a day input by user is weekday or weekend
char=input('enter the day:')
weekday='mon,tue,wed,thu,fri'
weekend='sat,sun'
if(char in weekday):
    print(char,'is weekday')
else:
    print(char,'is weekend')
