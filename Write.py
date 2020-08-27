#!/usr/bin/env python3
import time
import sys

from colorsys import hsv_to_rgb
from PIL import Image, ImageDraw, ImageFont
from unicornhatmini import UnicornHATMini

def setup(text, colour, show_total):
    unicornhatmini = UnicornHATMini()

    unicornhatmini.set_rotation(180)
    unicornhatmini.set_brightness(0.1)

    display_width, display_height = unicornhatmini.get_shape()
    font = ImageFont.truetype("5x7.ttf", 8)
    text_width, text_height = font.getsize(text)
    image = Image.new('P', (text_width + display_width + display_width, display_height), 0)
    draw = ImageDraw.Draw(image)

    draw.text((display_width, -1), text, font=font, fill=255)

def static(text, colour = "255,255,255", show_total = 2):
    setup(text, colour, show_total);
    unicornhatmini.show()

def scroll(text, colour = "255,255,255", show_total = 2):
    setup(text, colour, show_total);

    show_count = 0
    offset_x = 0
    r, g, b = colour.split(",")

    while show_count < show_total:
        for y in range(display_height):
            for x in range(display_width):
                hue = (time.time() / 10.0) + (x / float(display_width * 2))
                if image.getpixel((x + offset_x, y)) == 255:
                    unicornhatmini.set_pixel(x, y, r, g, b)
                else:
                    unicornhatmini.set_pixel(x, y, 0, 0, 0)

        offset_x += 1
        if offset_x + display_width > image.size[0]:
            offset_x = 0
            show_count = show_count+1

        unicornhatmini.show()
        time.sleep(0.05)
