import actions;
import buttons;
import config;
import github;
import sites;
import timer;
import writer;
from animations import render;

class App:
    def __init__(self):
        self.config = config.Config()
        self.timer = False
        self.writer = writer.Writer()
        render("swirl")
        buttons.listen(self.on_press)

    def on_press(self, button_name):
        if button_name == "A": self.handleContributions()
        elif button_name == "B": self.handleSites()
        elif button_name == "X": self.handleActions()
        elif button_name == "Y": self.handleStatus()

    def handleActions(self):
        actions.check()

    def handleContributions(self):
        c = github.getContributions(self.config)
        if c == False: self.writeError("conn fail")
        elif c < 3000: self.writeError(c)
        else: self.write(c)

    def handleSites(self):
        self.handleSite("taylorhub", "http://192.168.1.94:5000")
        self.handleSite("reactions", "http://reactions.tomtaylor.name")

    def handleSite(self, name, url):
        if sites.checkSite(url): self.writeSuccess(name)
        else: self.writeError(name)

    def handleStatus(self):
        s = github.getStatus(self.config)
        if s == False: self.writeError("conn fail")
        else: self.write(s)

    def handleTime(self):
        self.write(timer.getTime())

    def handleTimer(self):
        if self.timer != False: 
            return self.write(self.timer.getRemainingStr())
        self.timer = timer.createTimer()
        self.write("Timer started")

    def write(self, message, colour="Rainbow"):
        self.writer.clear()
        self.writer.scroll(str(message), colour)

    def writeError(self, message):
        self.write(message, "Red")

    def writeSuccess(self, message):
        self.write(message, "Green")

App()
