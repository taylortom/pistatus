#!/usr/bin/env python3
import datetime

class Timer:
    def __init__(self):
        self.time = 0

def getTime():
    return datetime.datetime.now().strftime("%H:%M")

def createTimer():
    return Timer()


