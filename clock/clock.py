class Clock:
    def __init__(self, hour, minute):
        self.hour = (hour * 60 + minute) // 60 % 24
        self.minutes = (hour * 60 + minute) % 60

    def __repr__(self):
        return f"Clock({self.hour}, {self.minutes})"

    def __str__(self):
        return str(self.hour).rjust(2,"0")+":"+str(self.minutes).rjust(2,"0")

    def __eq__(self, other):
        return self.hour == other.hour and self.minutes == other.minutes

    def __add__(self, minutes):
        return Clock(0, self.hour * 60 + self.minutes + minutes)
    
    def __sub__(self, minutes):
        return Clock(0, self.hour * 60 + self.minutes - minutes)