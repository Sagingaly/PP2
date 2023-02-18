
#print(datetime.date.today())
#print(datetime.datetime(2022,10,26,10,30,21))
#td_object=datetime.timedelta(days=5,seconds=3,weeks=5,microseconds=5,milliseconds=5,hours=2,minutes=3)
#print(td_object)
"""
date=datetime.datetime.today()+datetime.timedelta(days=7)
print(date)
date=datetime.datetime.today()-datetime.timedelta(days=7)
print(date)

import datetime
ds1='Friday,April 1,2022'
ds2='4/1/22'
ds3='04-01-2022'
dt1=datetime.datetime.strptime(ds1,'%A,%B,%d,%Y')
dt2=datetime.datetime.strptime(ds2,'%m/%d/%y')
dt3=datetime.datetime.strptime(ds3,'%m-%d-%Y')
print(dt1)
print(dt2)
print(dt3)

import datetime
date_1=datetime.date(2022,5,15)
date_2=datetime.date(2022,5,6)
print(date_1-date_2)

1)import datetime
date_5=datetime.date.today()-datetime.timedelta(days=5)
print(date_5)

2)import datetime
dt1= datetime.date.today()
print(dt1)
dt2=datetime.date.today()-datetime.timedelta(days=1)
print(dt2)
dt3=datetime.date.today()+datetime.timedelta(days=1)
print(dt3)

3)import datetime
d=datetime.datetime.today().replace(microsecond=0)
print(d)

4)import datetime
dt1 = datetime.datetime(2022, 3, 1, 12, 0, 0)
dt2 = datetime.datetime(2022, 3, 1, 12, 1, 30)

time_difference = (dt2 - dt1).total_seconds()

print("The time difference between the two dates is", time_difference, "seconds.")
"""