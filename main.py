import time
from utility import s2ms

# -------------------------------------- Conffig --------------------------------------
WORK_TIME = 1 * 60
SHORT_BREAK = 5 * 60
LONG_BREAK = 15 * 60
MAX_CYCLE = 4


# ---------------------------------------- Main ----------------------------------------
class Pomodoro:
    def __init__(self):
        self.cycle = 0                        # counter of seseions before Long Break
        self.work_time = WORK_TIME            # Hold Work time by secinds
        self.short_break_time = SHORT_BREAK   # Hold Short break time
        self.long_break_time = LONG_BREAK     # Hold long Break timer
        self.max_cycle = MAX_CYCLE            # Maximum short break
        self.type = "work"                    # Hold Current type of session
        # init some var to use in pomodoro

    def timer(self, time, type, msg):
        while time:
            time -= time
            print(msg)
            time.sleep(1)
            remaining_time = s2ms(time)

    def start_pomo(self):
        self.type = "work"
        self.timer(self.work_time, self.type, self.msg)
        self.type = self.update(self.type)
