##----> While loop
##---->     it is used to execute a block of statemets repeatedly until a given condition is satisfied
##---->     while(condition)
##---->         body
##----> write a prgm to print first 10 natural numbers using while loop
# i=1
# while(i<=10):
#     print(i)
#     i=i+1

##---->  write a prgm print 0 to 50 using while loop
# i=0
# while(i<=51):
#     print(i)
#     i=i+1
##----> print first 10 even number using while loop
# i=2
# count=0
# while(count<=10):
#     if(i%2==0):
#         print(i)
#         count=count+1
#     i=i+1

##----> print 1st 5 odd numbers
# i=1
# while(i<=9):
#     if(i%2==1):
#         print(i)
#     i=i+1

##----> write a prgm to print the sum of a number fall in range 1,10
# i=1
# sum=0
# while(i<=10):
#     sum=sum+i
#     i=i+1
# print(sum)

##----> write the progrm find the prodect of both even and odd numbers fall in range 1 to 10
#
# i=1
# sum1=1
# sum2=1
# while(i<=10):
#     if(i%2==0):
#         sum1*=i
#     else:
#         sum2*=i
#     i=i+1
# print(sum2)
# print(sum1)

##----> write the progrm find the prodect of both even and odd numbers fall in range by user
# i=int(input('enter initial:'))
# b=int(input('enter the final:'))
# count1=0
# count2=0
# while(i<=b):
#     if (i % 2 == 0):
#         count1=count1+1
#     else:
#         count2=count2+1
#     i = i + 1
# print('count of even:',count1)
# print('count of odd:',count2)

##---> print first 10 natural number in reverse order
# i=10
# while(i>=1):
#     print(i)
#     i-=1

##--->  multiplication table of a number input by user
# a=int(input('enter a number:'))
# i=1
# sum=0
# while(i<=10):
#     sum=a*i
#     print(i,'*',a,'=',sum)
#     i+=1

##----> print first 5 even number
# i=10
# while(i>=2):
#     if(i%2==0):
#         print(i,end=" ")
#     i-=1

# print()
##----> write a prgrm to print the 1st 10 intiger and square
###--->     1:1
##---->     2:4
##---->     3:9
# i=1
# while(i<=10):
#     print(i,':',i**2)
#     i+=1


##---->  find the factorial of a number input by the user
# a=int(input('enter a number:'))
# fact=1
# while(a>1):
#     fact=fact*a
#     a=a-1
# print(fact)


##---->  skip the number that a divisible by 11 fall in range 1,100
# i=0
# while(i<100):
#     i+=1
#     if(i%11==0):
#         continue
#     else:
#         print(i)


##----> write a prgm that sums all the multiples of 3 up to given number N using loop
# n=int(input('enter the number;'))
# i=1
# sum=0
# while(i<=n):
#     i+=1
#     if(i%3==0):
#         sum=sum+i
# print(sum)


##----> count the total even number fall in the range input by user
# n=int(input('enter the number:'))
# i=1
# count=0
# while(i<=n):
#     i+=1
#     if(i%2==0):
#         count+=1
# print(count)


##----> find the sum of digit of number inputs by user
# i=0
# n=int(input('enter a number:'))
# sum=0
# while(n!=0):
#     b=n%10
#     sum=sum+b
#     n=n//10
# print(sum)


##----> reverse of a number
# n=int(input('enter a number:'))
# leng=len(str(n))
# mem=0
# sum=0
# while(n>0):
#     sum=n%10
#     mem=mem*10+sum
#     n//=10
# print(mem)

##---->  palindrome checking oof a number
# a=int(input('enter a number:'))
# b=a
# l=len(str(a))
# i=0
# num=0
# while(i<l):
#     rem=a%10
#     num=num*10+rem
#     a//=10
#     i+=1
# if(num==b):
#     print('it is palindrome')
# else:
#     print('it is not palindrome')


##--->harshad number
# n=int(input('enter a number:'))
# a=n
# sum=0
# while(n!=0):
#     b=n%10
#     sum=sum+b
#     n//=10
# if(a%sum==0):
#     print('it is harshad')
# else:
#     print('it is not harshad')


##----> disariam number
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


##----> armstrong number
# n=int(input('enter a number:'))
# a=n
# sum=0
# while(n>0):
#     b=n%10
#     sum=sum+(b**3)
#     n//=10
# if(a==sum):
#     print('it is armstrong')
# else:
#     print('it is not armstrong')

##----> task
# n=int(input('enter a number:'))
# l=len(str(n))
# a=n
# sum=0
# while(n!=0):
#     b=n%10
#     sum=sum+(b**l)
#     n//=10
# if(sum==a):
#     print('it is amstrong')
# else:
#     print('it is not amstrong')



##----> input numbers from the user  till user input 0 and at the end it should display
#          the total number of even and odd numners

# n=int(input('enter the number:'))
# count_of_odd=0
# count_of_even=0
# while(n!=0):
#     n=int(input('enter the number:'))
#     if(n%2==0):
#         count_of_even+=1
#     else:
#         count_of_odd+=1
# print('count of odd number:',count_of_odd)
# print('count of even number:',count_of_even)
