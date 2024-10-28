# word='hello world'
# print(word)
# print()

##---> string concatenation
# a='hello'
# b='world'
# print(a+b)
# print(a+' '+b) #if we add int + strng the it will seen type error
# print()

##---> element accessing
# print(word[2])
# print(word[6])
# print()

##---> string slicing
# it access a part of a sequence
# print(word[0:5])
# print(word[6:11])
# print(word[:5])
# print(word[6:])
# print(word[:])
# print(word[0:5:2])
# print(word[::-1])
# print()

##--->string iteration
# for i in word:
#     print(i)
# print()

##--->find the length of the string input by the user without using len()
# a=input('enter a word:')
# count=0
# for i in a:
#     count+=1
# print('length of',a,'is',count)

##---> find the last index position of string imput by user
# a=input('enter a woerd:')
# for i in a:
#     count+=1
# print(count-1)

##---> write a program to remove spaces fome the string input by user
# a=input('enter a word:')
# b=''
# for i in a:
#     if i!=' ':
#         b+=i
#         print(i,end='')

##--->write a program to reverse a string input by the user with out using slice operation
# a=input('enter a string:')
# b=''
# for i in a:
#     b=i+b
# print(b)

##-->write aprogram to check a string inpot by th e user is palindrom or not
# a=input('enter a string:')
# b=''
# for i in a:
#     b=i+b
# if b==a:
#     print('it is palindrom')
# else:
#     print('it is not palindrom')

##-->input a string from user find the total count of vowels
# a=input('enter a string:')
# count=0
# for i in a:
#     if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
#     # if(i=='a'or'e'or'i'or'o'or'u'):
#         count+=1
# print(count)
# a=input('enter a string:')
# v="AEIOUaeiou"
# count=0
# for i in a:
#     if i in v:
#         count+=1
#         print(i,end='')
# print('\n',count)

##input the string and print the vowels
# a=input('enter a string:')
# for i in a:
#     if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
#         print(i,end='')

##---> 1 .upper()
# a='///hello WORLD///'
# print(a.upper())

##---> 2 .lower()
# print(a.lower())

##---> 3 title() : to convert each 1st character of word to upper case
# print(a.title())

##---> 4 capitalize():to convert only the 1st character to upper case
# print(a.capitalize())

##---> 5 swapcase():swaping l to u and u to l
# print(a.swapcase())

##---> 6 find():to return thr specif position of the character/if the character not in the word the return the value -1
# print(a.find('R'))

##---> 7 index() : it raises an error when the element not found
# print(a.index('R'))

##---> 8 replace() :
# print(a.replace('hello','hi'))

##---> 9 split()
# print(a.split())

##---> 10 strip():to trim the word left and right/lstrip(),rstrip()
# print(a.strip('/'))

##---> 11 count():returns the number of time a specific value occurred
# print(a.count('l'))

##--->##---> string chekers
##--->      1.isupper()
##--->      2.islower()
##--->      3.isalnum()
##--->      4.isalpha()
##--->      5.isnumeric()
##--->      6.isdigit()
##--->      7.isspace()
##--->      8.istitle()


##---> input a string from user and disply the total count of numbers and alphabest
# a=input('enter a input:')
# b=0
# c=0
# for i in a:
#     if(i.isalpha()):
#         b+=1
#     else:
#         c+=1
# print('Alphabets:',b)
# print('Numbers:',c)

##---> take input from the user and remove duplication
# a=input('enter a input:')
# b=''
# for i in a:
#     if(i in b):
#         continue
#     else:
#         b+=i
# print(b)

##---> for num,char in enumerater(text)
# for i,ch in enumerate(input('enter a input:')):
#     print(ch,':',i)

##---> input a string from user and conver even index to upper case and odd to lover
# a=input('enter a input:')
# for i ,ch in enumerate(a):
#     if(i%2==0):
#         print(ch.upper(),end='')
#     else:
#         print(ch.lower(),end='')
Fa