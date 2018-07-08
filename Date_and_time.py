# import time
#
# print("The epoch on this system starts at " + time.strftime('%C', time.gmtime(0)))
# print("The current timezone is {0} with an offset of {1} ".format(time.tzname[0], time.timezone))
#
# if time.daylight != 0:
#     print('Daylight Savings time is in effect')
#     print('The DST timezone is ' + time.tzname[1])

import datetime

print(datetime.datetime.today())
print(datetime.datetime.now())
print(datetime.datetime.utcnow())

