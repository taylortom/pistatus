#!/usr/bin/env python3

from gpiozero import Button
from signal import pause

def listen(func):
    button_map = { 5: "A", 6: "B", 16: "X", 24: "Y"}

    button_a = Button(5)
    button_b = Button(6)
    button_x = Button(16)
    button_y = Button(24)

    def on_press(button): func(button_map[button.pin.number])

    try:
        button_a.when_pressed = on_press
        button_b.when_pressed = on_press
        button_x.when_pressed = on_press
        button_y.when_pressed = on_press
        pause()

    except KeyboardInterrupt:
        button_a.close()
        button_b.close()
        button_x.close()
        button_y.close()
