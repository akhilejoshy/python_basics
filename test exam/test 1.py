##----> simple calculator
# print('1 addition')
# print('2 subtraction')
# print('3 multiplication')
# print('4 division')
# a=int(input('enter ur opetion:'))
# if(a==1 or a==2 or a==3 or a==4):
#     b = int(input('enter 1st number:'))
#     c = int(input('enter 2nd number:'))
#     if(a==1):
#         print(f'{b}+{c}={b+c}')
#     elif(a==2):
#         print(f'{b}-{c}={b-c}')
#     elif(a==3):
#         print(f'{b}*{c}={b*c}')
#     else:
#         print(f'{b}/{c}={b/c}')
# else:
#     print('enterd worng option')

##----> BMI calculator
# a=float(input('enter ur weight:'))
# b=float(input('enter ur height:'))
# c=b/100
# bmi=a/(c**2)
# if(bmi<18.5):
#     print('underweight')
# elif(18.5<=bmi<24.9):
#     print(' normal weight')
# elif(25<=bmi<29.9):
#     print('Overweight')
# else:
#     print('obese')

##----> ATM Withdrawal
# a=int(input('Enter your ammount:'))
# if(a%100==0):
#     print('Transaction  success')
# else:
#     print('Sorry , Transaction not complete , plz input an amount divisible by 100')

##----> sum of N natural number
# a=int(input('enter a number:'))
# sum=0
# for i in range(a+1):
#     sum+=i
#     i+=1
# print(sum)

##----> palindrome
# n=int(input('enter a number:'))
# a=n
# l=len(str(n))
# sum=0
# for i in range(l):
#     b=n%10
#     sum=sum*10+b
#     n//=10
#     i+=1
# if(sum==a):
#     print('it is palindrom')
# else:
#     print('it is not palindrom')

##----> Armstrong
# n=int(input('enter a number:'))
# a=n
# l=len(str(n))
# sum=0
# for i in range(n):
#     b=n%10
#     sum=sum+(b**l)
#     n//=10
# if(sum==a):
#     print('it is amstrong')
# else:
#     print('it is not armstrong')

##----> Disarium
# n=int(input("enter a number:"))
# l=len(str(n))
# a=n
# sum=0
# while(n>0):
#     b=n%10
#     sum=sum+(b**l)
#     n//=10
#     l-=1
# if(sum==a):
#     print('it is disariam')
# else:
#     print('it is not disariam')

##---> 	Sum of Even Numbers:
# n=int(input('enter a number:'))
# i=2
# sum=0
# while(i<n+1):
#     if(i%2==0):
#         sum=sum+i
#     i+=1
# print(sum)

##---> 	Factorial of a number
# n=int(input('enter a number:'))
# i=1
# sum=1
# while(i<n+1):
#     sum*=i
#     i+=1
# print(sum)

##---> Print Odd Numbers between 1 and 20
# for i in range(1,20):
#     if(i%2==0):
#         continue
#     else:
#         print(i,end=" ")

for i in range(6):
    for k in range(5-i):
        print(' ',end='')
    for j in range(i):
        print('*',end=' ')
    print()
for i in range(4,0,-1):
    for k in range(5-i):
        print(' ',end='')
    for j in range(i):
        print('*',end=' ')
    print()

for i in range(6):
    for k in range(5-i):
        print(' ',end='')
    for j in range(i):
        print(i,end=' ')
    print()
for i in range(4,0,-1):
    for j in range(5-i):
        print(' ',end='')
    for j in range(i):
        print(i,end=' ')
    print()

for i in range(6):
    for k in range(5-i):
        print(' ',end='')
    for j in range(i):
        print('*',end=' ')
    for p in range((5-i)*2):
        print(' ',end='')
    for j in range(i):
        print('*', end=' ')
    if(i==4 or i==5):
        for s in range(20):
            print('*',end=' ')
    print()
for i in range(4,0,-1):
    for k in range(5-i):
        print(' ',end='')
    for j in range(i):
        print('*',end=' ')
    for k in range((5-i)*2):
        print(' ',end='')
    for j in range(i):
        print('*',end=' ')
    if(i==4 or i==3):
        for s in range(20):
            print('*',end=' ')
    print()