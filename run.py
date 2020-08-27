import buttons;
import write;

def on_press(button_name):
    write.scroll(str(button_name), "255,0,0", 1)

buttons.listen(on_press)
