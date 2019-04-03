'''Use an incrementation device

'''
daycount =[None,31,28,31,30,31,30,31,31,30,31,30,31]
leapdaycount= [None,31,29,31,30,31,30,31,31,30,31,30,31]     
class mdate():
    def __init__(self,day,month,year,daycount = 0):
        self.day = day
        self.month = month
        self.year = year
        self.daycount = daycount
    def update(self,days):
        # Generate while loop to do checking daily
        i = 0
        while i < days:
        # Run a check if it's the leap year once a year
            if self.year % 100 == 0:
                isleapyear = (self.year % 400 == 0)
            else:
                isleapyear = (self.year % 4 == 0) 
            self.day += 1
            self.daycount = (self.daycount + 1) % 7
            # Checks for month and year
            if isleapyear == True:
                if self.day > leapdaycount[self.month]:
                    self.day = 1
                    self.month += 1
                    if self.month > 12:
                        self.month = 1
                        self.year += 1
                    else:
                        pass
            else:
                if self.day > daycount[self.month]:
                    self.day = 1
                    self.month += 1
                    if self.month > 12:
                        self.month = 1
                        self.year += 1
                    else:
                        pass
            i += 1
        return (self.day,self.month,self.year, self.daycount)
    def problem(self,days,set_day = 6):
        # Generate while loop to do checking daily
        i = 0
        count  = 0
        while i < days:
        # Run a check if it's the leap year once a year
            if self.year % 100 == 0:
                isleapyear = (self.year % 400 == 0)
            else:
                isleapyear = (self.year % 4 == 0) 
            self.day += 1
            # Adds to daycount and takes modulus
            self.daycount = (self.daycount + 1) % 7
            # Checks for month and year
            if isleapyear == True:
                if self.day > leapdaycount[self.month]:
                    self.day = 1
                    self.month += 1
                    if self.month > 12:
                        self.month = 1
                        self.year += 1
                    else:
                        pass
            else:
                if self.day > daycount[self.month]:
                    self.day = 1
                    self.month += 1
                    if self.month > 12:
                        self.month = 1
                        self.year += 1
                    else:
                        pass
            i += 1
            if (self.daycount == set_day) and  (self.day == 1):
                count += 1
        return count
date1 = mdate(1,1,1901,2)
print(date1.update(36524))
print(date1.problem(36524))

