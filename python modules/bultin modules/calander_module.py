import calendar

# year=int(input('enter the year:'))
# month=int(input('enter the month:'))
# print(calendar.month(year,month))


# year=int(input('enter year:'))
# print(calendar.calendar(year))

##> isleep()

# print(calendar.isleap(2024))


##> textCalender

a=calendar.TextCalendar(calendar.SUNDAY)
print(a.formatyear(2024))

print(a.formatmonth(2024,10))# perticular mnth

