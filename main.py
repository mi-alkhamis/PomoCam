import time
from utility import s2ms

# -------------------------------------- Conffig --------------------------------------
# WORK_TIME = 25 * 60
WORK_TIME = 5
SHORT_BREAK = 5 * 60
LONG_BREAK = 15 * 60
MAX_CYCLE = 4


# ---------------------------------------- Main ----------------------------------------
class Pomodoro:
    def __init__(self):
        self.cycle = 0  # counter of seseions before Long Break
        self.work_time = WORK_TIME  # Hold Work time by secinds
        self.short_break_time = SHORT_BREAK  # Hold Short break time
        self.long_break_time = LONG_BREAK  # Hold long Break timer
        self.max_cycle = MAX_CYCLE  # Maximum short break
        self.type = "work"  # Hold Current type of session
        self.msg = "Work time"
        # init some var to use in pomodoro

    def timer(self, timer, type, msg):
        while timer:
            timer -= 1
            time.sleep(1)
            remaining_time = s2ms(timer)
            print(f"{msg}: {remaining_time[0]}:{remaining_time[1]}")

    def start_pomo(self):
        self.type = "work"
        self.timer(self.work_time, self.type, self.msg)
        self.type = self.update(self.type)

    def time_break(self,type):
        self.type = type
        if type == "rest":
            self.timer(self.short_break_time,self.type,self.msg)
        elif type == "long":
            self.timer(self.long_break_time,self.type,self.msg)
        self.type = self.update(self.type)

    def update(self, type):
        match type:
            case "work":
                type = "rest"
                if self.cycle == 4:
                    type = "long"
                    self.cycle = 0
                else:
                    self.cycle += 1

            case "rest":
                self.cylce += 1
                self.start_pomo()

            case "long":
                self.cycle = 0
                type = "work"
        return type

    def update(self, type):
        if type == "work":
            self.cycle += 1
            if self.cycle >= self.max_cycle:
                return "long"
            else:
                return "rest"
        elif type == "rest":
            return "work"
        elif type == "long":
            self.cycle = 0
            return "work"


pomo = Pomodoro()
pomo.start_pomo()
