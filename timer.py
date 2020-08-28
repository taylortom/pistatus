#!/usr/bin/env python3
import datetime
import time

class Timer:
    def __init__(self):
        self.TIMER_LENGTH = 45 * 60
        self.start = time.time()
        self.end = self.start + self.TIMER_LENGTH

    def getRemaining(self):
        left = time.localtime(self.end - time.time());
        return [left.tm_min, left.tm_sec]

    def getRemainingStr(self):
        [m, s] = self.getRemaining()
        return str(m) + ":" + str(s)

    def getRemainingProgress(self):
        return round(((self.end - time.time())/self.TIMER_LENGTH)*100)
        

def getTime():
    return datetime.datetime.now().strftime("%H:%M")

def createTimer():
    return Timer()