##---> break
for i in range(1,10):
    if(i==5):
        break
    else:
        print(i)

##---> continue
for i in range(1,10):
    if(i==5):
        continue
    else:
     print(i)

##---> write a prgm to skip the number which are div by 2 and not by 3 fall in range 1 to 100\
for i in range(1,101):
    if(i%2==0 and i%3!=0):
        continue
    else:
        print(i)

##---> write a prgm to skip mthe number which are div by 3
for i in range(1,101):
    if(i%3==0):
        continue
    else:
        print(i)

##---> for loop with else
for i in range (1,10):
    print(i)
else:
    print('complited')


###---> check a number input by user is prime or not
n=int(input('enter a number:'))
if(n<=1):
    print('itys not prime number')

else:
    for i in range(2,n):
        if(n%i==0):
            print('it is not prime number')
            break
    else:
        print('it is prime number')

##---> write a prgm to print the given series
for i in range(5,31,5):
    print(i,end=' ')
print()

##---> print a progrm the given series
for i in range(1000,5001,1000):
    print(i,end=' ')
print()

##---> print the first 10 natural numbers in revers order
for i in range(10,0,-1):
    print(i,end=',')