class Time(object):
    '''Represents the time of day.
    attributes: hour, minute, second.'''

time = Time()
time.hour = 11
time.minute = 59
time.second = 3

def print_time(time):
    print('%.2d:%.2d:%.2d'%(time.hour,time.minute,time.second))

print('The time is:\t')
print_time(time)


def is_after(t1,t2):
    return t1.hour > t2.hour or t1.minute > t2.minute or t1.second > t2.second

t1 = Time()
t1.hour = 10
t1.minute = 59
t1.second = 3

t2 = Time()
t2.hour = 9
t2.minute = 59
t2.second = 3


print(is_after(t1,t2))

#Pure functions and modifiers
#Development plan: prototype and patch.

#Simple protoype of add_time
def add_time(t1,t2):
    '''Thus pure function does not modifiy any of the objects passed
    to it as arguments. It only returns a value'''
    sum = Time()
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second
    return sum


start = Time()
start.hour = 9
start.minute = 45
start.second = 0

duration = Time()
duration.hour = 1
duration.minute = 35
duration.second = 0

done = add_time(start,duration)
print_time(done)

#Improved version of add_time
def new_add_time(t1,t2):
    sum = Time()
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second

    if sum.second>= 60:
        sum.second -= 60
        sum.minute += 1

    if sum.minute >= 60:
        sum.minute -= 60
        sum.hour += 1

    return sum

done = add_time(start,duration)
print_time(done)


def increment(time, seconds):
    '''Adds a given number of seconds to a Time object'''
    time.second += seconds
    time.minute += time.second//60
    time.hour += time.minute//60
    
    time.second = time.second % 60
    time.minute = time.minute % 60
    time.hour = time.hour % 60
    
    return time



def new_increment(time,seconds):
    from copy import deepcopy
    r = deepcopy(time)

    r.second += seconds
    r.minute += r.second//60
    r.hour += r.minute//60
    
    r.second = r.second % 60
    r.minute = r.minute % 60
    r.hour = r.hour % 60
    
    return r

#Increment function test
print('OG time is: ')
print_time(start)
print('50 sec later: ')
print_time(new_increment(start,50))
print('70 seconds later: ')
print_time(new_increment(start,70))
print('130 seconds later: ')
print_time(new_increment(start,130))


#Time to integers
def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds


#Integer to time
def int_to_time(seconds):
	time = Time()
	minutes, time.second = divmod(seconds, 60)
	time.hour, time.minute = divmod(minutes, 60)
	return time

seconds_to_time = int_to_time(7200)
print(type(seconds_to_time))
print_time(seconds_to_time)

def last_add_time(time1,time2):
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)

    
def last_increment(time, seconds):
    return int_to_time(time_to_int(time) + seconds)