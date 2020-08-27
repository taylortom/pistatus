#!/usr/bin/env python3
import time
import sys

from colorsys import hsv_to_rgb
from PIL import Image, ImageDraw, ImageFont
from unicornhatmini import UnicornHATMini

unicornhatmini = UnicornHATMini()

unicornhatmini.set_rotation(180)
unicornhatmini.set_brightness(0.1)

pass_text = "build passed (^.^)"
fail_text = "build failed (;-_-)"
pass_colour = [0,200,0]
fail_colour = [200,0,0]
target = sys.argv[1]
status = sys.argv[2]
is_pass = True if sys.argv[2] == "pass" else False
text = target + " " + (pass_text if is_pass else fail_text)

display_width, display_height = unicornhatmini.get_shape()
font = ImageFont.truetype("5x7.ttf", 8)
text_width, text_height = font.getsize(text)
image = Image.new('P', (text_width + display_width + display_width, display_height), 0)
draw = ImageDraw.Draw(image)

show_count = 0
offset_x = 0

draw.text((display_width, -1), text, font=font, fill=255)

while show_count < 2:
    for y in range(display_height):
        for x in range(display_width):
            hue = (time.time() / 10.0) + (x / float(display_width * 2))
            r, g, b = pass_colour if is_pass else fail_colour
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
