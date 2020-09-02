#!/usr/bin/env python3
import os
import requests
import sys
import time

from unicornhatmini import UnicornHATMini

def getData():
    try:
        res = requests.get('https://api.github.com/repos/taylortom/adapt-authoring/actions/workflows/2374946/runs')
        runs = res.json()['workflow_runs']
        if(len(runs) > 17): runs = runs[0:17]
	for i in range(len(runs)): runs[i] = 1 if runs[i]['conclusion'] == 'success' else 2
        return runs[::-1]
    except:
        return []

def draw(data):
    uni = UnicornHATMini()
    uni.clear()
    uni.set_rotation(0)
    uni.set_brightness(0.1)

    display_width, display_height = uni.get_shape()

    for x in range(display_width):
        r = g = 0
        if len(data) > x:
            if data[x] == 1: g = 255
            elif data[x] == 2: r = 255
            elif data[x] == 3:
                r = 255
                g = 150

        for y in range(display_height):
            uni.set_pixel(x, y, r, g, 0)

    uni.show()
    time.sleep(3)
    uni.clear()
    uni.show()

def check():
    draw(getData())
