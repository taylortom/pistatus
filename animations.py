#!/usr/bin/env python3

import colorsys
import math
import time
from unicornhatmini import UnicornHATMini

unicornhatmini = UnicornHATMini()
unicornhatmini.set_brightness(0.1)
unicornhatmini.set_rotation(0)
u_width, u_height = unicornhatmini.get_shape()

# Generate a lookup table for 8-bit hue to RGB conversion
hue_to_rgb = []

for i in range(0, 360):
    hue_to_rgb.append(colorsys.hsv_to_rgb(i / 359.0, 1, 1))


# Twisty swirly goodness
def swirl(x, y, step):
    x -= (u_width / 2)
    y -= (u_height / 2)
    dist = math.sqrt(pow(x, 2) + pow(y, 2)) / 2.0
    angle = (step / 10.0) + (dist * 1.5)
    s = math.sin(angle)
    c = math.cos(angle)
    xs = x * c - y * s
    ys = x * s + y * c
    r = abs(xs + ys)
    r = r * 12.0
    r -= 20
    return (r, r + (s * 130), r + (c * 130))


# Roto-zooming checker board
def checker(x, y, step):
    x -= (u_width / 2)
    y -= (u_height / 2)
    angle = (step / 10.0)
    s = math.sin(angle)
    c = math.cos(angle)
    xs = x * c - y * s
    ys = x * s + y * c
    xs -= math.sin(step / 200.0) * 40.0
    ys -= math.cos(step / 200.0) * 40.0
    scale = step % 20
    scale /= 20
    scale = (math.sin(step / 50.0) / 8.0) + 0.25
    xs *= scale
    ys *= scale
    xo = abs(xs) - int(abs(xs))
    yo = abs(ys) - int(abs(ys))
    v = 0 if (math.floor(xs) + math.floor(ys)) % 2 else 1 if xo > .1 and yo > .1 else .5
    r, g, b = hue_to_rgb[int(step) % 255]
    return (r * (v * 255), g * (v * 255), b * (v * 255))


# Weeee waaaah
def blues_and_twos(x, y, step):
    x -= (u_width / 2)
    y -= (u_height / 2)
    scale = math.sin(step / 6.0) / 1.5
    r = math.sin((x * scale) / 1.0) + math.cos((y * scale) / 1.0)
    b = math.sin(x * scale / 2.0) + math.cos(y * scale / 2.0)
    g = r - .8
    g = 0 if g < 0 else g
    b -= r
    b /= 1.4
    return (r * 255, (b + g) * 255, g * 255)


# Rainbow search spotlights
def rainbow_search(x, y, step):
    xs = math.sin((step) / 100.0) * 20.0
    ys = math.cos((step) / 100.0) * 20.0
    scale = ((math.sin(step / 60.0) + 1.0) / 5.0) + 0.2
    r = math.sin((x + xs) * scale) + math.cos((y + xs) * scale)
    g = math.sin((x + xs) * scale) + math.cos((y + ys) * scale)
    b = math.sin((x + ys) * scale) + math.cos((y + ys) * scale)
    return (r * 255, g * 255, b * 255)


# Zoom tunnel
def tunnel(x, y, step):
    speed = step / 100.0
    x -= (u_width / 2)
    y -= (u_height / 2)
    xo = math.sin(step / 27.0) * 2
    yo = math.cos(step / 18.0) * 2
    x += xo
    y += yo
    if y == 0:
        if x < 0:
            angle = -(math.pi / 2)
        else:
            angle = (math.pi / 2)
    else:
        angle = math.atan(x / y)
    if y > 0:
        angle += math.pi
    angle /= 2 * math.pi  # convert angle to 0...1 range
    hyp = math.sqrt(math.pow(x, 2) + math.pow(y, 2))
    shade = hyp / 2.1
    shade = 1 if shade > 1 else shade
    angle += speed
    depth = speed + (hyp / 10)
    col1 = hue_to_rgb[int(step) % 359]
    col1 = (col1[0] * 0.8, col1[1] * 0.8, col1[2] * 0.8)
    col2 = hue_to_rgb[int(step) % 359]
    col2 = (col2[0] * 0.3, col2[1] * 0.3, col2[2] * 0.3)
    col = col1 if int(abs(angle * 6.0)) % 2 == 0 else col2
    td = .3 if int(abs(depth * 3.0)) % 2 == 0 else 0
    col = (col[0] + td, col[1] + td, col[2] + td)
    col = (col[0] * shade, col[1] * shade, col[2] * shade)
    return (col[0] * 255, col[1] * 255, col[2] * 255)


effects = { "tunnel": tunnel, "rainbow_search": rainbow_search, "checker": checker, "swirl": swirl }

t_start = time.time()

def render(effect_name = "swirl"):
    effect = effects[effect_name]
    try:
        while True:
            t = time.time() - t_start
            step = (t * 50)

            if round(t) >= 3:
                unicornhatmini.clear()
                unicornhatmini.show()
                return

            f = t / 10.0
            fx = int(f) % len(effects)

            for y in range(u_height):
                for x in range(u_width):
                    r, g, b = effect(x, y, step)
                    r = int(max(0, min(255, r)))
                    g = int(max(0, min(255, g)))
                    b = int(max(0, min(255, b)))
                    unicornhatmini.set_pixel(x, y, r, g, b)

            unicornhatmini.show()
            time.sleep(1.0 / 60.0)

    except KeyboardInterrupt:
        pass
