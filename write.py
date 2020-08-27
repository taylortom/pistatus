#!/usr/bin/env python3
import time
import sys

from colorsys import hsv_to_rgb
from PIL import Image, ImageDraw, ImageFont
from unicornhatmini import UnicornHATMini

default_colour = "255,255,255"
default_show_total = 2

def strToColour(s):
   r, g, b = s.split(",")
   return [int(r), int(g), int(b)]

def init_unicorn():
    unicornhatmini = UnicornHATMini()
    unicornhatmini.clear()
    unicornhatmini.set_rotation(180)
    unicornhatmini.set_brightness(0.1)
    return unicornhatmini;

def scroll(text, colour = "255,255,255", show_total = 2):
    uni = init_unicorn()

    display_width, display_height = uni.get_shape()
    font = ImageFont.truetype("5x7.ttf", 8)
    text_width, text_height = font.getsize(text)
    image = Image.new('P', (text_width + display_width + display_width, display_height), 0)
    draw = ImageDraw.Draw(image)
    draw.text((display_width, -1), text, font=font, fill=255)

    show_count = 0
    offset_x = 0
    r, g, b = strToColour(colour)

    while show_count < show_total:
        for y in range(display_height):
            for x in range(display_width):
                hue = (time.time() / 10.0) + (x / float(display_width * 2))
                if image.getpixel((x + offset_x, y)) == 255:
                    uni.set_pixel(x, y, r, g, b)
                else:
                    uni.set_pixel(x, y, 0, 0, 0)

        offset_x += 1
        if offset_x + display_width > image.size[0]:
            offset_x = 0
            show_count = show_count+1

        uni.show()
        time.sleep(0.05)

