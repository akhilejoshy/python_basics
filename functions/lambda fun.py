# lambda() : it is unanimous fun which mean a fun without name/ it is a single line fun/
#       x=lambda args: expression

# #Q adding 2 numbers
# x=lambda a,b:a+b
# print(x(1,3))


# #Q find the square root of a number
# r=lambda a:a**0.5
# print(r(4))


# #Q find qube of a argument
# q=lambda a:a**3
# print(q(3))


# #Q find area of a circle
# c=lambda r: 3.14 * (r * 2)
# print(c(2))


# #Q find area of triangle
# t=lambda l,b:(b*l)/2
# print(t(2,3))


# #Q  find the largest of 2 number using lambda
# x=lambda a,b:f'{a} is greater' if (a>b) else f'{b} is greater'
# print(x(3,5))


#Q  using lambda find a number is odd or even
# oe=lambda a:f'{a} is odd' if (a%2==1) else f'{a} is even'
# print(oe(int(input('enter a number:' ))))


#Q check a char entered by user is vowel o not
# v=lambda a:f'{a} is vowel' if (a in 'aeiouAEIOU') else f'{a} is not vowel'
# print(v(input('enter a char:')))


#Q check a number is +ve or -ve
# p=lambda a:f'{a} is +ve' if a>0 else f'{a} is -ve'
# print(p(int(input('enter a number:'))))

# #Q  check a number is +ve or -ve or 0 using lambda
# n=lambda a:f'{a} is +ve' if a>0 else(f'{a} is zero' if a==0 else f'{a} is -ve')
# print(n(int(input(':'))))


# #Q   find thee largest 3 number
# l=lambda a,b,c:f'{a} is largest' if a>b and a>c else f'{b} is largest' if b>c else f'{c} is largest'
# print(l(int(input('1st num:')),int(input('2nd num:')),int(input('3rd num:'))))

#Q  find the min of 5 numbers using lambda
# n=lambda a,b,c,d,e:f'{a} is min' if(a<b and a<c and a<d and a<e) else (f'{b} is min' if(b<c and b<d and b<e) else(f'{c} is min' if(c<d and c<e) else(f'{d} is min' if(d<e) else f'{e} is min')))
# print(n(int(input('1st:')),int(input('2nd:')),int(input('3rd:')),int(input('4th:')),int(input('5th:'))))

##--> lambda filter(),map(),reduce()
##>1st: filter()
#       it that takes a sequence as argument and this will filter out all the element ina sequence
#           x=filter(lambda args:expression,sequence_element)
#Q filter even numbers from given list using lambda
# li=[1,2,3,4,5,6,7]
# x=filter(lambda i:i%2==0,li)
# print(list(x))

#Q  filter out alphabet
# l=[1,2,'a','b']
# a=filter(lambda i:i.isalpha(),str(l))
# print(list(a))


#Q  filter out which are dividable by both 2 and 3
# li=eval(input('enter a number:'))
# d=filter(lambda i:i%2==0 and i%3==0,li)
# print(list(d))


#Q  input a string and filter out vowels
# li=input('enter a string:')
# v=filter(lambda i:i in 'aeiouAEIOU',li)
# print(list(v))

##>2nd   map()
#       the map() in lambda that takes sequence as a argument and new sequence is return the expression in map that applies to all elements in sequence
#       x=map(lambda args:condition,list)

#Q  find the square of each number in a given list using lambda
# li=[1,2,3,4,5,6,7,8,9]
# s=map(lambda i: i**2,li)
# print(list(s))


#Q  convert only the first letter of each words to upper case
# li=['welcome','hello','python']
# u=map(lambda i:i.capitalize(),li)
# print(list(u))

#Q  print the reverse of each word in a list input by user using lambda
# l=eval(input('enter  strings:'))
# r=map(lambda i:i[::-1],l)
# print(list(r))

##--->  reduce
#       its use to reduce an iterable to a single value
#       :from functools import reduce
#           functools:package
#           reduce:module
#           x=reduce(lamda args:expr,seq)
from functools import reduce
li=[1,2,3,4]
x=reduce(lambda a,b:a+b,li)
print(x)


#Q  find the product of alist input by user

li=eval(input(':'))
print(reduce(lambda a,b:a*b,li))


#Q  find min value of a list input by user

l=eval(input(':'))
print(reduce(lambda a,b:a if a<b else b,l))

#Q  find max value of a list
print(reduce(lambda a,b:a if a>b else b,l))

##--->  n