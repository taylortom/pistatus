#!/usr/bin/env python3
import requests

def getData():
    url = 'http://192.168.1.94:5000/api/github'
    try:
        return requests.get(url).json()
    except:
        return False

def getContributions():
    d = getData()
    if d == False:
        return d
    return int(d["contributions"])

def getStatus():
    d = getData()
    if d == False:
        return d
    return d["status"]["message"]

