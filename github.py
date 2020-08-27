#!/usr/bin/env python3
import requests
import write

contributions = 0

def update():
    url = 'http://localhost:5000/api/github'
    r = requests.get(url).json()
    if contributions != contributions: 
        contributions = r["contributions"]
        write(contributions)
