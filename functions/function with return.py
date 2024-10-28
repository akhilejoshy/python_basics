# def add(a,b):
#     c=a*b
#     return c
#
# print(add(2,3))
from itertools import count


#Q find a unmerge is odd or even wit fun return type
# def oddoreven(a):
#     if a%2==0:
#         c='even'
#     else:
#         c='odd'
#     return c

# print(oddoreven(2))


#Q find the largest of three number
# def larg(a,b,c):
#     if a>b:
#         if a>c:
#             l=a
#     elif b>c:
#         l=b
#     else:
#         l=c
#     return l
# print(larg(9,5,2))


#Q check a number disarium
# def dis(n):
#     l=len(str(n))
#     sum=0
#     while n>0:
#         b=n%10
#         sum=sum+(b**l)
#         n//=10
#         l-=1
#     return sum
#
# n=175
# a=n
# if a==(dis(n)):
#     print('disarium')
# else:
#     print('not disarium')

#Q create a function list element square and pass list as a argument and return a list that contain square of each value
# def list_element_square(li):
#     a=[]
#     for i in li:
#        a+=[i**2]
#     return a
#
# print(list_element_square([1,2,3,4,5,6]))


#Q pass list into a fun and return a list that contain the reverse of each number
def rev(li):
    a=[]
    for i in li:
        b=0
        while i>0:
            c=i%10
            b=b*10+c
            i//=10
        a.append(b)
    return a

print(rev([12,24,53,84,95]))

#Q write a function uniqe char that return a list of uniq character i  a string
def unique_char(st):
    b=[]
    for i in st:
        if st.count(i)==1:
            b+=[i]
    return b
print(unique_char('hello'))

#Q pass number of string into a fun and return a dic that contain string and  reverse as value
def dic_reverse(str):
    d={}
    for i in str:
        d[i]=i[::-1]
    return d
print(dic_reverse(['hello','hii','bye']))

#Q write a python fun to pass list of number and return the even number from a given list
def even(li):
    a=[]
    for i in li:
        if i%2==0:
            a+=[i]
    return a
print(even([1,2,3,4,5]))

#q qudratic eqution 1 5 6
def q(a,b,c):

    x1=((-b)+(((b**2)-(4*a*c))**0.5))//(2*a)
    x2 = ((-b) - (((b**2) - (4 * a * c)) ** 0.5))//(2*a)
    return x1,x2
a=1
for i in q(1,5,6):
    print('x',a,'=',i,sep='')
    a+=1

