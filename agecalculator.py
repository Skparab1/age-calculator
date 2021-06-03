from datetime import date
from datetime import datetime
birthdate = input('enter your birthdate in the format dd/mm/yyyy > ')
birthmonth,birthday,birthyear = str(birthdate[:2]),str(birthdate[3:4]),str(birthdate[6:])
if int(birthday) < 10:
    birthday.replace('0','')
birthmonth.replace('0','')
birthday,birthmonth,birthyear = int(birthday),int(birthmonth),int(birthyear)
today = date.today()
nowdate,nowmonth,nowyear = int(today.strftime("%d")),int(today.strftime("%m")),int(today.strftime("%y"))
now = datetime.now()
nowhour,nowminute,nowsecond = int(now.strftime("%H")),int(now.strftime("%M")),int(now.strftime("%S"))
nowyear = int(('20'+str(nowyear)))
yearsold = nowyear-birthyear-1
monthsold = (yearsold*12) + ((nowmonth - birthmonth) if birthmonth <= nowmonth else (nowmonth + (13-birthmonth)))
daysold = round(((monthsold*30) + ((nowdate - birthday) if birthday <= nowdate else (birthdate - nowdate))),0)
hoursold = (daysold*24) + nowhour
minutesold = (hoursold*60) + nowminute
secondsold = (minutesold*60) + nowsecond
milisecold = secondsold * 100
print('You are:'),print(yearsold,' years old'),print(monthsold,' months old'),print(daysold,' days old'), print(hoursold,' hours old'),print(minutesold,' minutes old'),print(secondsold,' seconds old'),print(milisecold,' miliseconds old')