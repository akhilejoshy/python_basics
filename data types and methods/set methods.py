##--->  collction of elements
##--->  unorded
##--->  {}
##--->  unindexed
##--->  no duplication
##--->  mutable


##--->  set methods
# add()
# pop()
# remove(element)
# union: its combine two or more sets
# intersection:pick come elements
# symmetric difference:
# clear()

a={'a','b','c'}
b={'f','a','g'}
print(a)

a.add('e')
print(a)

a.pop()
print(a)

a.remove('b')
print(a)

a={'a','b','c'}
b={'f','a','g'}

c=a.union(b)
print(c)

c=a.intersection(b)
print(c)

c=a.symmetric_difference(b)
print(c)

a.clear()
print(a)

b={'q','w','r'}
for i in b:
    print(i)

##--->