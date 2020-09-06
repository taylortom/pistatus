import re, subprocess, time, writer
from unicornhatmini import UnicornHATMini

def checkStrength():
    results = str(subprocess.check_output(["/sbin/iwconfig", "wlan0"]))
    m = re.search('ESSID:"(.+)"', results)
    ssid = m.group(1)
    m = re.search('Link Quality=(\d+)/(\d+)', results)
    width = round((float(m.group(1))/float(m.group(2)))*17)
    w = writer.Writer()
    w.scroll(ssid)
    draw(width)

def getColour(width):
    p = (width/17)*100
    if p > 70: return [0,255,0]
    if p > 60: return [100,255,0]
    if p > 50: return [255,100,0]
    if p > 40: return [255,30,0]
    return [255,0,0]

def draw(width):
    uni = UnicornHATMini()
    uni.clear()
    uni.set_rotation(0)
    uni.set_brightness(0.1)

    display_width, display_height = uni.get_shape()

    r, g, b = getColour(width)

    for x in range(display_width):
        for y in range(display_height):
            if width > x: uni.set_pixel(x, y, r, g, b)
            else: uni.set_pixel(x, y, 0, 0, 0)

    uni.show()
    time.sleep(3)
    uni.clear()
    uni.show()

