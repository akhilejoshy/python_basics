import datetime


# print(datetime.date.today())
# print(datetime.datetime.now())


##> timedelta()
a=datetime.date.today()
a+=datetime.timedelta(days=10)
print(a)


a-=datetime.timedelta(days=20)
print(a)

