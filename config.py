import json
import os

class Config:
    def __init__(self):
        self.config = json.load(open(os.path.dirname(os.path.realpath(__file__)) + '/config.json'))

    def get(self, key):
        return self.config[key]
