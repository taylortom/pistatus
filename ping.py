#!/usr/bin/env python3
import os
import requests
import sys
import time

from PIL import Image, ImageDraw, ImageFont
from unicornhatmini import UnicornHATMini

data = []

def getData():
    global data
    if len(data) == 17: data = []
    try:
        res = requests.get('http://tomtaylor.name')
        data.append(1 if res.status_code == 200 else 0)
    except:
        data.append(0)
    return data

def draw():
    uni = UnicornHATMini()
    uni.clear()
    uni.set_rotation(0)
    uni.set_brightness(0.1)

    display_width, display_height = uni.get_shape()

    interval = 60/17
    interval = 5

    while True:
        data = getData()
        for x in range(display_width):
            if x >= len(data):
                r = g = 0
            else:
                r = 255 if data[x] == 0 else 0
                g = 255 if data[x] == 1 else 0

            for y in range(display_height):
                uni.set_pixel(x, y, r, g, 0)

        uni.show()
        time.sleep(interval)

draw()
