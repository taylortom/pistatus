#!/usr/bin/env python3
import requests

def checkSite(url):
    try:
        res = requests.get(url)
        return res.status_code == 200
    except:
        return False;
