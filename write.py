#!/usr/bin/env python3
import os
import sys
import time

from colorsys import hsv_to_rgb
from PIL import Image, ImageDraw, ImageFont
from unicornhatmini import UnicornHATMini

class Colours():
    def __init__(self):
        self.Red = "255,10,0"
        self.Green = "0,255,10"
        self.Blue = "0,10,255"
        self.White = "255,255,255"
        self.Black = "0,0,0"
	self.Rainbow = "Rainbow" # note: special case

    def strToColour(self, s):
	if s == "Rainbow":
            return self.Rainbow

        if s == "Red":
            s = self.Red
        if s == "Green":
            s = self.Green
        if s == "Blue":
            s = self.Blue
        if s == "White":
            s = self.White

        r, g, b = s.split(",")
        return [int(r), int(g), int(b)]

COLOURS = Colours()
DEFAULT_COLOUR = COLOURS.Rainbow
DEFAULT_BRIGHTNESS = 0.1
DEFAULT_ROTATION = 0
DEFAULT_SHOW_TOTAL = 2

def init_unicorn():
    unicornhatmini = UnicornHATMini()
    unicornhatmini.clear()
    unicornhatmini.set_rotation(DEFAULT_ROTATION)
    unicornhatmini.set_brightness(DEFAULT_BRIGHTNESS)
    return unicornhatmini;

def scroll(text, colour = DEFAULT_COLOUR, show_total = DEFAULT_SHOW_TOTAL):
    uni = init_unicorn()

    display_width, display_height = uni.get_shape()
    font = ImageFont.truetype(os.path.dirname(os.path.realpath(__file__)) + "/5x7.ttf", 8)
    text_width, text_height = font.getsize(text)
    image = Image.new('P', (text_width + display_width + display_width, display_height), 0)
    draw = ImageDraw.Draw(image)
    draw.text((display_width, -1), text, font=font, fill=255)

    show_count = 0
    offset_x = 0

    if colour != COLOURS.Rainbow:
        r, g, b = COLOURS.strToColour(colour)

    while show_count < show_total:
        for y in range(display_height):
            for x in range(display_width):
                hue = (time.time() / 10.0) + (x / float(display_width * 2))
                if colour == COLOURS.Rainbow:
                    r, g, b = [int(c * 255) for c in hsv_to_rgb(hue, 1.0, 1.0)]
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
