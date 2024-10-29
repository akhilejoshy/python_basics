##--->elif statement
##    if():
##        body
##    elif():
##        body
##    else
##        body


#Q  4,check a day input by user is weekday or weekend
char=input('enter the day:')
weekday='mon,tue,wed,thu,fri'
weekend='sat,sun'
if(char in weekday):
    print(char,'is weekday')
elif(char in weekend):
    print(char,'is weekend')


#Q  check a number is +ve,-ve,0
a=int(input('enter a number:'))
if(a>0):
    print('it is 3+ve')
elif(a<0):
    print('it is -ve')
else:
    print('it is zero')


#Q the largest three number
a=int(input('enter 1st number:'))
b=int(input('enter 2nd number:'))
c=int(input('enter 3rd number:'))
if(a>b and a>c):
    print('1st is greater')
elif(b>c):
    print("2nd is greater")
else:
    print('3rd is greater')


#Q find the largest of 4 number
a=int(input('enter 1st number:'))
b=int(input('enter 2nd number:'))
c=int(input('enter 3rd number:'))
d=int(input('enter 4th number'))
if(a>b and a>c and a>d):
    print('1st is greater')
elif(b>c and b>d):
    print("2nd is greater")
elif(c>d):
    print('3rd is greater')
else:
    print('4th is greater')


#Q  find the min of 5 number
a=int(input('enter 1st number:'))
b=int(input('enter 2nd number:'))
c=int(input('enter 3rd number:'))
d=int(input('enter 4th number:'))
e=int(input('enter 5th number:'))
if(a<b and a<c and a<d and a<e):
    print('1st is min')
elif(b<c and b<d and b<e):
    print("2nd is min")
elif(c<d and c<e):
    print('3rd is min')
elif(d<e):
    print('4th is min')
else:
    print('5th is min')


#Q  check grade
a=int(input('enter the mark:'))
if(a<=100 and a>90):
    print("you got A+")
elif(80<a<=90):
    print('u got A')
elif(70<a<=80):
    print('u got B+')
elif(60<a<=70):
    print('u got B')
elif(50<a<=60):
    print('u got C+')
elif(40<a<=50):
    print('u got C')
else:
    print('u got fail')


#Q road tax of bike
a=int(input('enter the price:'))
if(a>100000):
    print((a*15)/100)
elif(50000<a<=100000):
    print((a*10)/100)
else:
    print((a*5)/100)


#Q company bonus
salary=int(input('enter the salary:'))
pird=int(input('enter the service period:'))
if(pird>10):
    print(salary+((salary*10)/100))
elif(6<=salary<=10):
    print(salary+((salary*8)/100))
else:
    print(salary+((salary*5)/100))
    