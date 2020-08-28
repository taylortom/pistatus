#!/usr/bin/env python3
import requests

def getData():
    url = 'http://192.168.1.94:5000/api/github'
    return requests.get(url).json()

def getContributions():
    d = getData()
    return int(d["contributions"])

def getStatus():
    d = getData()
    return d["status"]["message"]

