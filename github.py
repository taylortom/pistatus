#!/usr/bin/env python3
import requests

def getContributions():
    url = 'http://192.168.1.94:5000/api/github'
    r = requests.get(url).json()
    return int(r["contributions"])
