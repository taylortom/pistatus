import buttons;
import github;
import timer;
import write;

def on_press(button_name):
    if button_name == "A":
        write.scroll(str(github.getContributions()))
    elif button_name == "B":
        write.scroll(github.getStatus())
    elif button_name == "X":
        write.scroll(timer.getTime())
    elif button_name == "Y":
        write.scroll("Y")

buttons.listen(on_press)
