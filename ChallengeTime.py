import time

print("time(): {}".format(time.get_clock_info('time')))
print("perf_counter(): {}".format(time.get_clock_info('perf_counter')))
print("monotonic(): {}".format(time.get_clock_info('monotonic')))
print("process_time(): {}".format(time.get_clock_info('process_time')))
