import buttons;
import github;
import timer;
import write;

TARGET_CONTRIBUTIONS = 3000

class App:
    def __init__(self):
        self.timer = False
        write.scroll("(^.^)", "Rainbow", 1)
        buttons.listen(self.on_press)

    def on_press(self, button_name):
        if button_name == "A":
            c = github.getContributions()
            message = str(c)
	    if c < TARGET_CONTRIBUTIONS:
                colour = "Red"
            else:
                colour = "Rainbow"
                message = message + " *(^_^)*"
            write.scroll(message, colour)
        elif button_name == "B":
            write.scroll(github.getStatus())
        elif button_name == "X":
            write.scroll(timer.getTime())
        elif button_name == "Y":
            if self.timer == False:
                self.timer = timer.createTimer()
                write.scroll("Timer started")
            else: 
                write.scroll(self.timer.getRemainingStr(), "255,0,0", 1)

App()
