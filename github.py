import json
import requests

def getData(config, query):
    try:
        headers = {"Authorization": "Bearer " + config.get("gitHubToken")
        response = requests.post('https://api.github.com/graphql', json={'query': query}, headers=headers)
        if response.status_code == 200:
            return response.json()
        return False
    except:
        return False

def getContributions(config):
    d = getData(config, "{ viewer { contributionsCollection { contributionCalendar { totalContributions } } } }")
    if d == False:
        return d
    return int(d["data"]["viewer"]["contributionsCollection"]["contributionCalendar"]["totalContributions"])

def getStatus(config):
    d = getData(config, "{ viewer { status { message } } }")
    if d == False:
        return d
    return d["data"]["viewer"]["status"]["message"]
