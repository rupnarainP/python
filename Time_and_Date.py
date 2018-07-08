import time
from time import time as my_timer
import random
# print(time.gmtime(0))
# # print(time.localtime())
# # print(time.time())
#
# time_here = time.localtime()
# print(time_here)
# #can use a variable but rather use the pre-defined functions for readability
# print("Year: {}, {}".format(time_here[0], time_here.tm_year))
# print("Month: {}, {}".format(time_here[1], time_here.tm_mon))
# print("Day: {}, {}".format(time_here[2], time_here.tm_mday))

input("Press enter to start")

wait_time = random.randint(1, 6)
time.sleep(wait_time)
start_time = my_timer()
input("Press Enter to stop")

end_time = my_timer()

print("Started at: " + time.strftime("%X", time.localtime(start_time)))
print("Ended at: " + time.strftime("%X", time.localtime(end_time)))

print("Your reaction time was {} seconds ".format(end_time-start_time))