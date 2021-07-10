import calendar

def goCalendar():
    c = calendar.TextCalendar(calendar.SUNDAY)
    str = c.formatmonth(2021, 7)
    print(str)