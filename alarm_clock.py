class Alarm_clock():
    def __init__(self, alarm_set):
        self.current_time = ''
        self.is_alarm_set = alarm_set
        self.alarm_time = ''
    
    def set_current_time(self):
        self.current_time = input("What is the current time?:")
        print(self.current_time)
    
    def set_alarm_on(self, alarm_set):
        self.is_alarm_set = alarm_set

    def set_alarm_time(self):
        self.alarm_time = input("What time would you like the alarm to be?:")
