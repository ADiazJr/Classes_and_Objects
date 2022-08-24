class Alarm_clock():
    def __init__(self):
        self.current_time = ''
        self.is_alarm_set = False
        self.alarm_time = ''
    
    def set_current_time(self):
        self.current_time = input("What is the current time?:")
        print(self.current_time)
    
    def set_alarm_on(self):
        self.is_alarm_set = input("Want the alarm to be on or off? True/False:")

    def set_alarm_time(self):
        self.alarm_time = input("What time would you like the alarm to be?:")
