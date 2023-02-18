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
