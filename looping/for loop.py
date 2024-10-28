##----->for loop
##----->    this are traditionly use when you have a block of code which you want to repeat to fixed number of times
##----->    for i in range(n):
##----->        body

# n=int(input('enter the number:'))
# for i in range(n):
#     print('hello')

##----->write a program to print 1st 10 natural number using for loop
# for i in range(1,11):
#     print(i)

# a=int(input('enter starting range:'))
# b=int(input('enter ending range:'))
# for i in range(a,b+1):
#     print(i)

##-----> write a program to print even numbers fall in the range input by the user
# for i in range(2,int(input('enter a number:'))+1,2):
#     print(i)
#
# for i in range(1,int(input('enter the number:'))+1,2):
#     print(i)

##-----> enter the number of odd values:5
##----->    printing 1st 5 odd numbers,
##-----> same for even number
# a=int(input('enter the number:'))
# i=1
# for i in range(1,(a*2)+1):
#     if(i%2==0):
#         print(i)
#     i=i+2


##----> Multiplication table
# n=int(input('enter the number:'))
# for i in range(1,11):
#     print(i,'*',n,'=',i*n)

##----> sum of first n natural numbers
# f=int(input('enter a number:'))
# e=0
# for i in range(1,f+1):
#     e+=i
# print(e)

##----> sum of first five odd number
# sum=0
# for i in range(1,10):
#     if(i%2==1):
#         sum=sum+i
# print(sum)

##----> product of even number
# sum=int(input('enter a number:'))
# s=1
# for i in range(1,sum):
#     if(i%2==0):
#         s*=i
# print(s)

##----> count
# count=0
# for i in range(1,101):
#     if(i%5==0):
#         count+=i
# print(count)

##----> sum of both even and odd
# even=0
# odd=0
# for i in range(1,6):
#     if(i%2==0):
#         even+=i
#     else:
#         odd+=i
# print('sum of even:',even)
# print('sum of odd:',odd)


##----> factorial
# n=int(input('enter the number:'))
# b=1
# for i in range(1,n+1):
#     b*=i
# print(b)

##----> sum of input numbers
# a=int(input("enter a number:"))
# l=len(str(a))
# sum=0
# for i in range(l):
#     b= a % 10
#     sum+=b
#     a=a/10
# print(int(sum))

##----> write a program to find the product of digit of thr number input by the user
# a=int(input('enter a number:'))
# l=len(str(a))
# sum=1
# for i in range(l):
#     b=a%10
#     sum*=b
#     a=a//10
# print(sum)

##----> write aprogram to find reverse of a number input by the user
# a=int(input('enter a number:'))
# len=len(str(a))
# mem=0
# for i in range(len):
#     sum=a%10
#     mem=mem*10+sum
#     a//=10
# print(mem)

##----> write a program to check a number is palindrome or not
# a=int(input('enter a number:'))
# b=a
# l=len(str(a))
# num=0
# for i in range(l):
#     rem=a%10
#     num=num*10+rem
#     a//=10
# if(num==b):
#     print('it is palindrome')
# else:
#     print('it is not palindrome')

 even=0
odd=0
for i in range(1,6):
    if(i%2==0):
        even+=i
    else:
        odd+=i
print('sum of even:',even)
print('sum of odd:',odd)

