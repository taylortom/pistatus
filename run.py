import buttons;
import github;
import write;

def on_press(button_name):
    if button_name == "A":
        c = github.getContributions()
        print(c)
        write.scroll(str(c))

buttons.listen(on_press)
