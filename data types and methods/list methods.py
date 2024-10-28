# li=[1,2,3,'a','b','c']
# print(li)


##---> element access
# print(li[4])
# print(li[2:4])
# print(li[2:])
# print(li[:3])
# print(li[1:5:2])
# print(li[::-1])


##---> list iteration
# for i in li:
#     print(i,end=' ')
# print()


##---> find the length of a list input bu the user without using len()
##--->      eval():its a bult un funtion that takes a string and evaluvates it as valid python expression and return the result
# data=eval(input('enter a data:'))
# count=0
# for i in data:
#     count+=1
# print('length is:',count)


##---> input intiger list frome user and dislay the sum of element
# a=eval(input('enter a input:'))
# sum=0
# for i in a:
#     sum+=i
# print(sum)


##---> remove duplicate element input by user
# a=eval(input('enter a input:'))
# b=[]
# for i in a:
#     if (i not in b):
#         b+=[i]
# print(b)


##---> find the reverse of the input by the user with out sl
# a=eval(input('enter a input:'))
# reslult=[]
# for i in a:
#     reslult=[i]+reslult
# print(reslult)


# a=eval(input('enter a input:'))
# l=len(a)
# r=[]
# for i in range(l-1,-1,-1):
#     r+=[a[i]]
# print(r)


##---> input alist of word and print a list that contain reverse of each words without slice
# a=eval(input('enter a input:'))
# res=''
# res2=[]
# for i in a:
#     for j in range(len(i)-1,-1,-1):
#         res+=i[j]
#     res2=res2+[res]
#     res=''
# print(res2)


##---> find the max value in a list
# a=eval(input('enter a input:'))
# l=len(a)
# temp=a[0]
# for i in range(l):
#     if(a[i]>temp):
#         temp=a[i]
# print([temp])


##---> find the min value in a list
# a=eval(input('enter a input:'))
# temp=a[0]
# for i in a:
#     if(i<temp):
#         temp=i
# print([temp])


##---> input a list of numbers from users and return a list with factorial of each numbers
# a=eval(input('enter a input:'))
# list=[]
# for i in a:
#     fact = 1
#     for j in range(1,i+1):
#         fact*=j
#     list+=[fact]
# print(list)


##---> fimd the revers of each number in list input by number
# a=eval(input('enter a list of numbers:'))
# rev=[]
# for i in a:
#     rev2=0
#     for j in range(len(str(i))):
#         b=i%10
#         rev2=rev2*10+b
#         i//=10
#     rev+=[rev2]
# print(rev)

##---> assignment:
##--->     1, list comprehension:
##--->          what is list compri
##--->          syntax of list compri
##--->          three diff problms

# list methods

# li=['a','b','c']
# li.append('d')
# print(li)
# li.insert(0,'hello')
# print(li)
# li.extend([1,2,3])
# print(li)
# print(li.index('hello'))
# li.pop()
# print(li)
# li.pop(3)
# print(li)
# li.remove('d')
# print(li)
# li1=['a','A','b','B']
# li1.sort()
# print(li1)
# li.reverse()
# print(li)
# li.clear()
# print(li)
# li1=[9,6,4,7,3,2,1,8]
# li1.sort(reverse=True)
# print(li1)































