#Q take a integer input from the user if the input false between the range 1 to 10 the program should print hello
a=int(input('enter a number:'))
if(a>=1 and a<=10):
    print('hello')


#Q wright a program to take a char from user  and check whether the chr is vowel or not
char=input('enter the character:')
vowel='a,e,i,o,u'
if(char in vowel):### membership operator
    print(f"yes,{char} is vowel")


#Q even checker
a=int(input('print a number:'))
if(a%2==0):
    print(f"{a} is even number")


#Q odd checker
a=int(input('enter a number:'))
if(a%2==1):
    print(a,'is a odd number')
