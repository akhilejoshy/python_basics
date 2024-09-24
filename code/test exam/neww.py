for i in range(4):
    for k in range(3,i,-1):
        print(' ',end=' ')
    for j in range(i):
        print('*',end=' ')
    print()
for i in range(2):
    for j in range(3):
        print('*',end=' ')
    print()
for i in range(4):
    for k in range(i):
        print(' ',end=' ')
    for j in range(3,i,-1):
        print('*',end=' ')
    print()

print()

for i in range(4):
    for k in range(i):
        print(' ',end='')
    for j in range(4,i,-1):
        print('*',end=' ')
    print()
for i in range(2,5):
    for k in range(4-i):
        print(' ',end='')
    for j in range(i):
        print('*',end=' ')
    print()

print()

for i in range(5):
    for j in range(5-i):
        print('*',end=' ')
    print()
for i in range(2,5):
    for j in range(i):
        print('*',end=' ')
    print()

print()

for i in range(5):
    for k in range(4-i):
        print(' ',end=' ')
    for j in range(i):
        print('*',end=' ')
    print()
for i in range(4,0,-1):
    for k in range(5-i):
        print(' ',end=' ')
    for j in range(1,i):
        print('*',end=' ')
    print()

print()

for i in range(65,71):
    for j in range(65,i+1):
        print(chr(j),end=' ')
    print()
for i in range(70,64,-1):
    for j in range(65,i):
        print(chr(j),end=' ')
    print()

print()

for i in range(6):
    for j in range(i):
        print(i-j,end=' ')
    print()

print()

for i in range(104,96,-1):
    for k in range(104-i):
        print(' ',end='')
    for j in range(97,i):
        print(chr(j),end=' ')
    print()

print()

for i in range(97,102):
    for j in range(102-i):
        print(chr(i),end=' ')
    print()
for i in range(70,75):
    for j in range(70,i+1):
        print(chr(i),end=' ')
    print()

print()

for i in range(3):
    for j in range(1,4):
        print(i*3+j,end=' ')
    print()

print()

for i in range(65,69):
    for k in range(68-i):
        print(' ',end=' ')
    for j in range(65,i+1):
        print(chr(i),end=' ')
    print()
for i in range(101,104):
    for k in range(i-100):
        print(' ',end=' ')
    for j in range(104-i):
        print(chr(i),end=' ')
    print()

print()

for i in range(7,0,-1):
    for j in range(7,i-1,-1):
        print(j,end=' ')
    print()