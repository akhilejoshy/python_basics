##---> a for loop inside another for loop
# for i in range(5):
#     for j in range(5):
#         print(i,j)

##---> using nested forlooop print multiplication table from number 1 to 10
# for i in range(1,11):
#     for j in range(1,11):
#         print(i,'*',j,'=',i*j)
#     print()

##---> pattern printing
# n=int(input('enter a number:'))
# for i in range(1,n+1):
#     for j in range(i):
#         print('*',end=' ')
#     print()

##---> square *
# n=int(input('enter a number:'))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print('*',end='  ')
#     print()

##---> reverse triangle
# n=int(input('enter a number:'))
# for i in range(n,0,-1):
#     for j in range(i):
#         print('*',end=" ")
#     print()


##---> combination of both triangle
# n=int(input('enter a number:'))
# t='*'
# x=t.ljust(5)
# for i in range(1,n+1):
#     for j in range(i):
#         print(x,end='')
#     print()
# for i in range(n-1,0,-1):
#     for j in range(i):
#         print(x,end='')
#     print()


# for i in range(6):
#     for j in range(i):
#         print(i,end=' ')
#     print()
# for i in range(4,0,-1):
#     for j in range(i):
#         print(i,end=' ')
#     print()


# 1
# 12
# 123
# 1234
# for i in range(1,5):
#     for j in range(i):
#         print(j+1,end=' ')
#     print()



# 1
# 21
# 321
# for i in range(4):
#     for j in range(i):
#         print(i-j,end=' ')
#     print()


# 1
# 12
# 123
# 1234
# 123
# 12
# 1
# for i in range(1,5):
#     for j in range(i):
#         print(j+1,end=' ')
#     print()
# for i in range(3,0,-1):
#     for j in range(i):
#         print(j+1,end=' ')
#     print()

# n=input("enter a string:")
# l=len(n)
# for i in range(l):
#     for k in range((l-1)-i):
#         print(" ",end='')
#     for j in range(i+1):
#         print(n[j],end=' ')
#     print()
# for i in range(l-1,0,-1):
#     for k in range((l-1)-i):
#         print(' ',end='')
#     for j in range(i):
#         print(n[j],end=' ')
#     print()

#
# c='*'
# for i in range(5):
#     print((c*i).rjust(4)+c+(c*i))
# for i in range(3,-1,-1):
#     print((c*i).rjust(4)+c+(c*i))

# for i in range(6):
#     for k in range(5-i):
#         print(' ',end='')
#     for j in range(i+1):
#         print('*',end=' ')
#     print()
# for i in range(5,0,-1):
#     for k in range(6-i):
#         print(' ',end='')
#     for j in range(i):
#         print('*',end=' ')
#     print()
# #
# for i in range(7):
#     for k in range(6-i):
#         print(' ',end='')
#     for j in range(i):
#         print(i,end=' ')
#     print()
# for i in range(5,0,-1):
#     for k in range(6-i):
#         print(' ',end='')
#     for j in range(i):
#         print(i,end=' ')
#     print()

##--->ASCII :american standerd code for information interchange
##--->A-z:65-90
##--->a-z:97-122
# for i in range(65,68):
#     for j in range(65,i+1):
#         print(chr(i),end=' ')
#     print()
#
# for i in range(97,103):
#     for j in range(97,i+1):
#         print(chr(i),end=' ')
#     print()