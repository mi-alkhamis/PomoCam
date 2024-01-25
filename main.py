import time
from utility import s2ms

# -------------------------------------- Conffig --------------------------------------
WORK_TIME = 25 * 60
SHORT_BREAK = 5 * 60
LONG_BREAK = 15 * 60
MAX_CYCLE = 4 * 60
WORK_MSG = "Work time"
BREAK_MSG = "Take a Break"


# ---------------------------------------- Main ----------------------------------------
class Pomodoro:
    def __init__(self):
        self.cycle = 0  # counter of seseions before Long Break
        self.work_time = WORK_TIME  # Hold Work time by secinds
        self.short_break_time = SHORT_BREAK  # Hold Short break time
        self.long_break_time = LONG_BREAK  # Hold long Break timer
        self.max_cycle = MAX_CYCLE  # Maximum short break
        self.session_type = "work"  # Hold Current type of session
        self.msg = WORK_TIME
        # init some var to use in pomodoro

    def timer(self, timer, session_type, msg):
        while timer:
            timer -= 1
            time.sleep(1)
            remaining_time = s2ms(timer)
            print(f"{msg}: {remaining_time[0]}:{remaining_time[1]}")
        self.update(session_type)

    def start_pomo(self):
        self.session_type = "work"
        self.msg = "Work time"
        self.timer(self.work_time, self.session_type, self.msg)
        self.type = self.update(self.type)

    def time_break(self, session_type):
        self.session_type = session_type
        if self.session_type == "short":
            self.msg = BREAK_MSG
            self.timer(self.short_break_time, self.session_type, self.msg)
        elif self.session_type == "long":
            self.msg = BREAK_MSG
            self.timer(self.long_break_time, self.session_type, self.msg)
        self.type = self.update(self.type)

    def update(self, session_type):
        match session_type:
            case "work":
                self.cycle += 1
                if self.cycle >= self.max_cycle:
                    self.time_break("long")
                else:
                    self.time_break("short")
            case "short":
                self.start_pomo()
            case "long":
                self.cycle = 0
                self.start_pomo()


pomo = Pomodoro()
pomo.start_pomo()
