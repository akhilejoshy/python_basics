di={'name':'amal','age':23}
print(di.keys())
print(di.values())
print(di.items())
print(di.get('name'))
print(di.pop('name'))
print(di.popitem())
di.update({'phone no':6997969769})
print(di)
di.update({'phone no':68743543543})
print(di)
di['address']='jhk'
print(di)
# change the key name
# di.pop('phone no') it return the value of phone no
di['mobile']=di.pop('phone no')
print(di)
di.clear()
print(di)



from itertools import count

# dictionary iteration
d={'a':1,'b':2,'c':3}
for i in d:
    print(i)

for i in d.values():
    print(i)

for i in d.items():
    print(i)

for i,j in d.items():
    print(i,j)


##---> input a sting from user and return a dictionary where keys are character and values as the number of occurrence
a=input('enter a string:')
c={}
for i in a:
    # c[i]=a.count(i)
    if i in c:
        c[i]=c[i]+1
    else:
        c[i]=1
print(c)


##--->  input a list strings from user print that with leng
a=eval(input('enter a string:'))
c={}
for i in a:
    count=0
    for j in i:
        count+=1
    c[i]=count
print(c)

##--->
a=eval(input('enter a integer list:'))
c={}
for i in a:
    if i%2==0:
        c[i]='even'
    else:
        c[i]='odd'
print(c)


