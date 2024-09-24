a=''
b=str()
#the both use for emppty string

##---> string formation
# name='akhil'
# designation='python django trainer'
# company='luminar'
# #im... i iam working as a... at ...
# print('I am {0} i am working as a {1} at {2}'.format(name,designation,company))
#
# name='Akhil Joshy'
# age=22
# course='Python'
# place='Thrissur'
# qulification='B.Tech'
# print('My name is {0:s} ,Iam from {1:s} ,my age is {2:d} ,and I complited {3:s} and im studing {4:s}'.format(name,place,age,qulification,course))
# print('my name is %s ,I am from %s my age is %d ,and I complited %s and Im studing %s'%(name,place,age,qulification,course))

# a=input('enter a strint:').upper()
# print(a)
# print(a.lower())

# b='john doe'
# print(b[0].upper()+b[1:])

c='abcdefghij'
l=len(c)
a=''
for i in range(l):
    if(i%2!=0):
        a=a+c[i].upper()
    else:
        a=a+c[i].lower()
print(a)