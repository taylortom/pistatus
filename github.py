#!/usr/bin/env python3
import requests
import write

def writeContributions(contributions):
    url = 'http://192.168.1.94:5000/api/github'
    r = requests.get(url).json()
    newContributions = int(r["contributions"])
    if newContributions != contributions:
        write.scroll(str(newContributions))
        return newContributions
