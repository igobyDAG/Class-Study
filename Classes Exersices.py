class Time(object):
    '''Represents the time of the day
    in hour,minute,second'''

#Initialize time and some values
time = Time()
time.hour = 0
time.minute = 1
time.second = 0

def print_time(time):
    print('%.2d:%.2d:%.2d'%(time.hour,time.minute,time.second))

print_time(time)


def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

print(time_to_int(time))

def int_to_time(seconds):
    t = Time()
    minutes, t.second = divmod(seconds,60)
    t.hour, t.minute = divmod(minutes, 60)
    return t

def add_time(t1, t2):
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)

def increment(time, seconds):
    return int_to_time(time_to_int(time) + seconds)

def mul_time(time,number):
    '''Return product of time and number
    in new time object'''
    t = Time()
    seconds = time_to_int(time)
    t = int_to_time(seconds * number)
    return t


def average_pace(time,distance):
    #distance/time
    t = time_to_int(time)
    pace = t / distance
    return pace


pace = average_pace(time, 100)
print('ran at: ',pace,' mps')