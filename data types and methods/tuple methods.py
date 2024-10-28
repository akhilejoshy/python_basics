##--->  len()
##--->  count()
##--->  index()
##--->  iteration
##--->  sliceing
##--->  element accessing
from itertools import count

a=(1,2,4,'a','b','c')
print(a)

print(len(a))

print(a.count('a'))

print(a.index(4))

for i in a:
    print(i)

print(a[::-1])

print(a[4])

