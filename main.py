import calendar 

print(calendar.weekheader(3))

print(calendar.firstweekday())

print(calendar.month(2020, 11, w=3))

print(calendar.monthcalendar(2020, 11))

a = calendar.weekday(2020, 11, 2)

print(a)

b = calendar.isleap(2020)

print(b)