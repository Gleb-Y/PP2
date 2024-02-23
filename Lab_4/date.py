import datetime
#ex 1
cur_date = datetime.date.today() - datetime.timedelta(days=5)
print(cur_date)

#ex 2
yes_day = datetime.date.today() - datetime.timedelta(days=1)
print('yesterday was: ', yes_day)
tod_day = datetime.date.today()
print('today is: ', tod_day)
tom_day = datetime.date.today() + datetime.timedelta(days=1)
print('tomorrow was: ', tom_day)

#ex 3
dt = datetime.datetime.today().replace(microsecond=0)
print('date and time without microseconds:', dt)

#ex 4
print('put first date in format: year month day hours minutes seconds')
year, month, day, hours, minutes, seconds = [int(x) for x in input().split()]
print('put second date in format: year month day hours minutes seconds')
year2, month2, day2, hours2, minutes2, seconds2 = [int(x) for x in input().split()]
date1 = datetime.datetime(year, month, day, hours, minutes, seconds)
date2 = datetime.datetime(year2, month2, day2, hours2, minutes2, seconds2)
delt = abs(date1 - date2)
print('your difference in seconds is: ', delt.total_seconds())