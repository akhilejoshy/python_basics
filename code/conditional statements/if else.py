##---> find the largest number
a=int(input('enter 1st number:'))
b=int(input('enter 2nd number:'))
if(a>b):
    print(a,'is bigger one')
else:
    print(b,'is bigger one')


##---> check char is vowel or not
char=input('enter a character:')
vowel='a,e,i,o,u'
if(char in vowel):
    print(f'{char} is vowel')
else:
    print(f'{char} is not vowel')


##---> find the smallest of two number
a=int(input('enter 1st number:'))
b=int(input('enter 2nd numner:'))
if(a>b):
    print(b,'is smallest')
else:
    print(a,'is smallest')


##---> check a number it even or odd
c=int(input('enter a number:'))
if(a%2==0):
    print(c,'is even')
else:
    print(c,'is odd')


##---> check a number input by user is +ve or -ve
d=int(input('enter a number:'))
if(d>0):
    print(d,'is +ve')
else:
    print(d,'is -ve')


##---> votting eligibelity
name=input('Enter the name of candidate:')
age=int(input(f'Enter the age of {name}:'))
if(age>=18):
    print(name,'is eligible for votting')
else:
    print(name,'is not eligible for voting')


##---> simple authenticaticaton user id: User,passwerd:Pass out:Succes
user=input('Enter the usser id:')
password=input('Enter the password:')
if(password=='Pass' and user=='User'):
    print("Authentication succes")
else:
    print('authenticaton decline')


##---> check a number div by 2 and 3
a=int(input('enter a number:'))
if(a%2==0 and a%3==0):
    print("the number is divisable by 3 and 2")
else:
    print('the number is not divisable by 2 and 3')


##---> check a number mull by 5
a=int(input("enter a numer:"))
if(a%5==0):
    print('this number is multiple by 5')
else:
    print('this number is not multiple by 5')


##---> check a day input by user is weekday or weekend
char=input('enter the day:')
weekday='mon,tue,wed,thu,fri'
weekend='sat,sun'
if(char in weekday):
    print(char,'is weekday')
else:
    print(char,'is weekend')