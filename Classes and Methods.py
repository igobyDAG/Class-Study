#Classes and Methods

class Time(object):
    '''Represents the time of the day'''

    def __init__(self, hour = 0, minute = 0, second = 0):
        self.hour = hour
        self.minute = minute
        self.second = second

    #The first parameter of a method must be called "self".
    #Commented out to demonstrate the __str__ method
    # def print_time(self):
        #print ('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second))

    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)


    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    #increment writen as a method
    def increment(self,seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)

    def is_after(self, other):
        '''Returns bool. Pass other to compare if it happens after self'''
        return self.time_to_int() > other.time_to_int()


time = Time(2,35,33)
print(time)




#Initialization of time class and defining values.
start = Time()
start.second = 0
start.minute = 45
start.hour = 9

def int_to_time(seconds):
        time = Time()
        minutes, time.second = divmod(seconds, 60)
        time.hour, time.minute = divmod(minutes, 60)
        return time



#Directly referencing the class
#Time.print_time(start)
#Calling a method on the object. Returns the same result
#start.print_time()
end = start.increment(1337)
#end.print_time()

print(end.is_after(start))

