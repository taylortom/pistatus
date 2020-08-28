#!/usr/bin/env python3
import os
import sys
import time

from colorsys import hsv_to_rgb
from PIL import Image, ImageDraw, ImageFont
from unicornhatmini import UnicornHATMini

class Colours():
    def __init__(self):
        self.Red = "255,0,0"
        self.Green = "0,255,0"
        self.Blue = "0,0,255"
        self.White = "255,255,255"
        self.Black = "0,0,0"

    def strToColour(self, s):
        r, g, b = s.split(",")
        return [int(r), int(g), int(b)]

default_colour = "255,255,255"
default_show_total = 2
COLOURS = Colours()


def init_unicorn():
    unicornhatmini = UnicornHATMini()
    unicornhatmini.clear()
    unicornhatmini.set_rotation(0)
    unicornhatmini.set_brightness(0.1)
    return unicornhatmini;

def scroll(text, colour = COLOURS.White, show_total = 2):
    uni = init_unicorn()

    display_width, display_height = uni.get_shape()
    font = ImageFont.truetype(os.path.dirname(os.path.realpath(__file__)) + "/5x7.ttf", 8)
    text_width, text_height = font.getsize(text)
    image = Image.new('P', (text_width + display_width + display_width, display_height), 0)
    draw = ImageDraw.Draw(image)
    draw.text((display_width, -1), text, font=font, fill=255)

    show_count = 0
    offset_x = 0
    r, g, b = COLOURS.strToColour(colour)

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