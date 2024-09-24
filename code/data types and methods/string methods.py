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

##--->string iteratiom
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
