import datetime
import pytz
import random
flight_time=10
all_timezones=pytz.all_timezones
tz1=pytz.timezone(all_timezones[random.randint(0,len(all_timezones))])
tz2=pytz.timezone(all_timezones[random.randint(0,len(all_timezones))])
print(tz1,tz2)
time1=datetime.datetime.now(tz1)
time2=datetime.datetime.now(tz2)
a=datetime.timedelta(hours=time1.hour-time2.hour)
new = datetime.datetime(2024,11,14,10,time1.minute,time1.second)
print(time1,time2)
print(new+a)






