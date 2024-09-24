##-----> nested if
##----->     an if statement inside anonther if statment is called nested if
##----->    if(condition):
##----->        if(condition):
##----->            body

##-----> simple calculatar using nested if ?
# print('1,Addition \n2,subtraction \n3,multiplication \n4,division')
# choice=int(input('plz enter ur choice:'))
# if(1<=choice<=4):
#         a=int(input('Enter the first number:'))
#         b=int(input('Enter the second number:'))
#         if(choice==1):
#             print(a,'+',b,'=',a+b)
#         elif(choice==2):
#             print(a,'-',b,'=',a-b)
#         elif(choice==3):
#             print(a,'*',b,'=',a*b)
#         elif(choice==4):
#             print(a,'/',b,'=',a/b)
# else:
#     print('invalid enter')

##-----> accept age gender and number of working days from user and display the wages according to the folloing criterea using nestedif
##----->    age>=18 and <30 male= 700 per day
##----->                    female=750 per day
##----->    age>=30 and<=40 male =800 per day
##----->                       female=850 per day
# gen=input('Enetr ur gender:')
# age=int(input('enter ur age:'))
# days=int(input('Enter ur working days:'))
# if(18<=age<30):
#     if(gen=='male'):
#         print('total wage:',700*days)
#     elif(gen=="female"):
#         print('total wage:',750*days)
# if(30<=age<=40):
#     if(gen=='male'):
#         print('total wage:',800*days)
#     elif(gen=='female'):
#         print('total wage:',850*days)