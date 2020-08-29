import buttons;
import github;
import sites;
import timer;
import write;

class App:
    def __init__(self):
        self.timer = False
        self.write("(^.^)")
        buttons.listen(self.on_press)

    def on_press(self, button_name):
        if button_name == "A":
            self.handleContributions()
        elif button_name == "B":
            self.handleSites()
        elif button_name == "X":
            self.handleTime()
        elif button_name == "Y":
            self.handleStatus()

    def handleContributions(self):
        c = github.getContributions()
        if c == False:
            self.writeError("conn fail")
        elif c < 3000:
            self.writeError(c)
        else:
            self.write(c)

    def handleSites(self):
        self.handleSite("taylorhub", "http://192.168.1.94:5000")
        self.handleSite("reactions", "http://reactions.tomtaylor.name")

    def handleSite(self, name, url):
        if sites.checkSite(url):
            self.writeSuccess(name)
        else:
            self.writeError(name)

    def handleStatus(self):
        s = github.getStatus()
        if s == False:
            self.writeError("conn fail")
        else:
            self.write(s)

    def handleTime(self):
        self.write(timer.getTime())

    def handleTimer(self):
        if self.timer == False:
            self.timer = timer.createTimer()
            self.write("Timer started")
        else:
            self.write(self.timer.getRemainingStr())

    def write(self, message):
        write.scroll(str(message), "Rainbow", 1)

    def writeError(self, message):
        write.scroll(str(message), "Red", 1)

    def writeSuccess(self, message):
        write.scroll(str(message), "Green", 1)

App()
