#!/usr/bin/env python3
import os
import sys
import time

from colorsys import hsv_to_rgb
from PIL import Image, ImageDraw, ImageFont
from unicornhatmini import UnicornHATMini

class Writer():
    def __init__(self):
        self.uni = UnicornHATMini()
        self.uni.clear()
        self.uni.set_rotation(0)
        self.uni.set_brightness(0.1)

        display_width, display_height = self.uni.get_shape()

        self.display_width = display_width
        self.display_height = display_height
        self.font = ImageFont.truetype(os.path.dirname(os.path.realpath(__file__)) + "/5x7.ttf", 8)

    def drawText(self, text):
        text_width, text_height = self.font.getsize(text)
        image = Image.new('P', (text_width + self.display_width + self.display_width, self.display_height), 0)
        draw = ImageDraw.Draw(image)
        draw.text((self.display_width, -1), text, font=self.font, fill=255)
        return image

    def getColour(self, s):
        if s == "Rainbow": return s

        mapValue = {
            "Red": "255,10,0",
            "Green": "0,255,10",
            "Blue": "0,10,255",
            "White": "255,255,255",
            "Black": "0,0,0"
        }[s]

        try: r, g, b = mapValue.split(",")
        except NameError: r, g, b = s.split(",")

        return [int(r), int(g), int(b)]


    def scroll(self, text, colour = "Rainbow", show_total = 1):
        image = self.drawText(text)

        show_count = 0
        offset_x = 0

        if colour != "Rainbow": r, g, b = self.getColour(colour)

        while show_count < show_total:
            for y in range(self.display_height):
                for x in range(self.display_width):
                    hue = (time.time() / 10.0) + (x / float(self.display_width * 2))

                    if colour == "Rainbow": r, g, b = [int(c * 255) for c in hsv_to_rgb(hue, 1.0, 1.0)]

                    if image.getpixel((x + offset_x, y)) == 255: self.uni.set_pixel(x, y, r, g, b)
                    else: self.uni.set_pixel(x, y, 0, 0, 0)

            offset_x += 1
            if offset_x + self.display_width > image.size[0]:
                offset_x = 0
                show_count = show_count+1

            self.uni.show()
            time.sleep(0.05)

    def clear(self):
        self.uni.clear()
        self.uni.show()
        time.sleep(0.05)

