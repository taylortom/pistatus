import json

class Config:
    def __init__(self):
        self.config = json.load(open('config.json',))

    def get(self, key):
        return self.config[key]
