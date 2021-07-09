import datetime as dt

# hora:minuto:segundo.microsegundo
print(dt.time(12, 6, 21, 7))

# ano-mes-dia
print(dt.date(2020, 4, 25))

# ano-mes-dia hora:minuto:segundo.microsegundo
print(dt.datetime(2020, 4, 25, 12, 6, 21, 7 ))

natal = dt.date(2020, 12, 25)
reveillon = dt.date(2021, 1, 1)

print(reveillon - natal)
print((reveillon - natal).days)
print((reveillon - natal).seconds)
print((reveillon - natal).microseconds)

d = dt.date(2001, 9, 11)
tday = dt.date.today()
print(tday, d)

# datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)

tdelta = dt.timedelta(hours=12)
print(tday + tdelta)

bday = dt.date(2016, 9, 24)
till_bday = bday - tday
print(till_bday.days)

dt_agora = dt.datetime.now()
print(dt_agora.strftime('%B %d, %Y'))

dt_str = 'July 24, 2016'
dt = dt.datetime.strptime(dt_str, '%B %d, %Y')
print(dt)

# strftime - Datetime para String
# strptime - String para Datetime
