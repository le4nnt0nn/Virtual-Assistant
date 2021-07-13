import calendar
from datetime import datetime

def goCalendar():
    currentMonth = datetime.now().month
    currentYear = datetime.now().year
    c = calendar.TextCalendar(calendar.SUNDAY)
    # - el calendario empieza en domingo
    str = c.formatmonth(currentYear, currentMonth)
    # - el calendario pertenecerá al año y al mes en el que estés
    print(str)