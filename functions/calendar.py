import calendar

def goCalendar():
    c = calendar.TextCalendar(calendar.SUNDAY)
    # - el calendario empieza en domingo
    str = c.formatmonth(2021, 7)
    # - el calendario pertenecerá al año 2021 y al mes de julio. Se puede cambiar al que prefieras
    print(str)