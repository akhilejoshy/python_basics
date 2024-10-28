##---> 1,positional argument

def muk(a,b):
    print(a*b)
muk(1,5)


##---> 2,default argument

def add(a,b,c=0):
    print(a+b+c)
add(1,5)


#Q  create  function product using default argument

def product(a,b,c=1,d=1):
    print(a*b*c*d)
product(2,4)
product(2,4,2)
product(2,4,2,2)


##---> 3,arbitrary argument/ if u dont know how many argument that are passing into a function use arbitrary argument
#           denoted by * followed by arg name

def values(*a):
    print(a)

values(1,3,4,5,6,6,7,8)


#Q create fun to mult that pass any number of argument?

def prd(*ar):
    count=1
    for i in ar:
        count*=i
    print(count)
prd(1,2,3,4,5)


#Q create a function add that pass any number of argument

def addd(*ad):
    count=0
    for i in ad:
        count+=i
    print(count)
addd(1,2,3,34,4)


#Q create a function min value passing into a fun

def min(*m):
    c=m[0]
    for i in m:
        if c>i:
            c=i
    print(c)
min(1,2,3)


#Q create a fun to find max value passing in to fun

def max(*x):
    c=x[0]
    for i in x:
        if c<i:
            c=i
    print(c)
max(1,2,3)


##---> 4,keyword argument/: Arguments pass in to fun by specifying key name/ here thr order of args doesn't matter

def add(a,b):
    print(a+b)
add(b=3,a=3)

def person(name,email,phn,address):
    print(name,email,phn,address)
person(phn=90483,name='akhil',address='ak_home',email='ak@gmail')


##---> 5,arbitrary keyword argument:/if u dont know how many key value pairs passing in to a fun use arbitrary keyword argument denoted by ** followed by arg name

def values(**kwargs):
    print(kwargs)
values(name='akhil', id=122)


##---> passing list as argument
def list_sum(li):
    print(li)
list_sum([1,2,3,4,5,6])